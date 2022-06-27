# -*- coding: utf-8 -*-

import re
import sys
import xbmc
import auth_helper
import requests
from urlparse import urlparse
from resources.lib.modules import hlshelper
from resources.lib.hlsproxy.simpleproxy import MediaProxy
from resources.lib.modules import control
from resources.lib.modules.util import get_signed_hashes
from resources.lib.modules.globoplay import resourceshelper
import threading
import traceback

HISTORY_URL = 'https://api.user.video.globo.com/watch_history/'
PLAYER_SLUG = 'android'
PLAYER_VERSION = '1.1.24'


class Player(xbmc.Player):
    def __init__(self):
        xbmc.Player.__init__(self)
        self.sources = []
        self.offset = 0.0
        self.isLive = False
        self.m3u8 = None
        self.cookies = None
        self.url = None
        self.item = None
        self.stop_playing_event = None
        self.credentials = None
        self.program_id = None
        self.video_id = None

    def onPlayBackStopped(self):
        control.log("PLAYBACK STOPPED")

        if self.stop_playing_event:
            self.stop_playing_event.set()

    def onPlayBackEnded(self):
        control.log("PLAYBACK ENDED")

        if self.stop_playing_event:
            self.stop_playing_event.set()

    def onPlayBackStarted(self):
        control.log("PLAYBACK STARTED")
        # if self.offset > 0: self.seekTime(float(self.offset))

    def play_stream(self, id, meta, children_id=None):

        meta = meta or {}

        control.log("GloboPlay - play_stream: id=%s | children_id=%s | meta=%s" % (id, children_id, meta))

        if id is None:
            return

        self.isLive = meta.get('livefeed', False)
        stop_event = None

        cdn = control.setting('globo_cdn')
        if cdn:
            cdn = cdn.lower() if cdn.lower() != 'auto' else None

        if self.isLive and meta.get('lat') and meta.get('long'):
            control.log("PLAY LIVE!")

            latitude = meta.get('lat')
            longitude = meta.get('long')

            if not latitude or not longitude:
                code, latitude, longitude = control.get_coordinates(control.get_affiliates_by_id(-1))

            info = self.__getLiveVideoInfo(id, latitude, longitude, cdn)

            if info is None:
                return

            item, self.url, stop_event = self.__get_list_item(meta, info)

        else:
            if not meta.get('router', True) or cdn:
                info = resourceshelper.get_video_info(id, children_id, cdn)
            else:
                info = resourceshelper.get_video_router(id, self.isLive, cdn)
                if not info:
                    info = resourceshelper.get_video_info(id, children_id, cdn)

            if info is None:
                return

            if 'resource_id' not in info:
                control.log("PLAY CHILDREN!")
                items = []
                xbmc.PlayList(1).clear()
                first = True
                for i in info:
                    hash_token, user, self.credentials = self.sign_resource(i['resource_id'], i['id'], i['player'], i['version'], cdn=i['cdn'])
                    i['hash'] = hash_token
                    i['user'] = user
                    item, url, stop_event = self.__get_list_item(meta, i, False)
                    if first:
                        self.url = url
                        first = False
                    items.append(item)
                    control.log("PLAYLIST ITEM URL: %s" % url)
                    xbmc.PlayList(1).add(url, item)
                item = items[0]
            else:
                control.log("PLAY SINGLE RESOURCE!")
                hash_token, user, self.credentials = self.sign_resource(info['resource_id'], info["id"], info['player'], info['version'], meta['anonymous'] if 'anonymous' in meta else False, cdn=info['cdn'])
                info['hash'] = hash_token
                info['user'] = user
                item, self.url, stop_event = self.__get_list_item(meta, info)

        self.offset = float(meta['milliseconds_watched']) / 1000.0 if 'milliseconds_watched' in meta else 0

        self.stop_playing_event = threading.Event()
        self.stop_playing_event.clear()

        self.program_id = info['program_id'] if 'program_id' in info else meta.get('program_id')
        self.video_id = id

        syshandle = int(sys.argv[1])
        control.resolve(syshandle, True, item)

        first_run = True
        last_time = 0.0
        while not self.stop_playing_event.isSet():
            if control.monitor.abortRequested():
                control.log("Abort requested")
                break
            if self.isPlaying():
                if first_run:
                    self.showSubtitles(False)
                    first_run = False

                if not self.isLive:
                    total_time = self.getTotalTime()
                    current_time = self.getTime()
                    if current_time - last_time > 5 or (last_time == 0 and current_time > 1):
                        last_time = current_time
                        percentage_watched = current_time / total_time if total_time > 0 else 1.0 / 1000000.0
                        self.save_video_progress(self.credentials, self.program_id, self.video_id, current_time * 1000, fully_watched=0.9 < percentage_watched <= 1)
            control.sleep(500)

        if stop_event:
            control.log("Setting stop event for proxy player")
            stop_event.set()

        control.log("Done playing. Quitting...")

    def __get_list_item(self, meta, info, pick_bandwidth=True):
        hash_token = info['hash']
        user = info['user']

        query_string = re.sub(r'{{(\w*)}}', r'%(\1)s', info['query_string_template'])

        query_string = query_string % {
            'hash': hash_token,
            'key': 'app',
            'openClosed': 'F' if info['subscriber_only'] and user else 'A',
            'user': user if info['subscriber_only'] and user else '',
            'token': hash_token
        }

        url = '?'.join([info['url'], query_string])

        control.log("live media url: %s" % url)

        parsed_url = urlparse(url)
        if parsed_url.path.endswith(".m3u8"):
            if pick_bandwidth:
                url, mime_type, stop_event, cookies = hlshelper.pick_bandwidth(url)
            else:
                mime_type, stop_event, cookies = None, None, None

        elif parsed_url.path.endswith(".mpd"):
            proxy_handler = MediaProxy()
            url = proxy_handler.resolve(url)
            stop_event = proxy_handler.stop_event
            mime_type = None
            cookies = None

        else:
            mime_type, stop_event, cookies = 'video/mp4', None, None

        if url is None:
            if stop_event:
                control.log("Setting stop event for proxy player")
                stop_event.set()
            control.infoDialog(message=control.lang(34100).encode('utf-8'), icon='ERROR')
            return None, None, None

        control.log("Resolved URL: %s" % repr(url))

        if control.supports_offscreen:
            item = control.item(path=url, offscreen=True)
        else:
            item = control.item(path=url)

        item.setInfo(type='video', infoLabels=control.filter_info_labels(meta))
        item.setArt(meta.get('art', {}))
        item.setProperty('IsPlayable', 'true')

        item.setContentLookup(False)

        user_agent = 'User-Agent=Globo Play/0 (iPhone)'

        if parsed_url.path.endswith(".mpd"):
            mime_type = 'application/dash+xml'
            if control.enable_inputstream_adaptive:
                control.log("Using inputstream.adaptive MPD")
                item.setProperty('inputstream.adaptive.manifest_type', 'mpd')
                item.setProperty('inputstream.adaptive.stream_headers', user_agent)
                item.setProperty('inputstreamaddon', 'inputstream.adaptive')

        if mime_type:
            item.setMimeType(mime_type)
        elif not cookies:
            item.setMimeType('application/vnd.apple.mpegurl')
            if control.enable_inputstream_adaptive:
                control.log("Using inputstream.adaptive HLS")
                item.setProperty('inputstream.adaptive.manifest_type', 'hls')
                item.setProperty('inputstream.adaptive.stream_headers', user_agent)
                item.setProperty('inputstreamaddon', 'inputstream.adaptive')

        encrypted = info.get('encrypted', False)

        if encrypted and not control.is_inputstream_available():
            control.okDialog(control.lang(31200), control.lang(34103).encode('utf-8'))
            return

        if encrypted:
            control.log("DRM: %s" % info['drm_scheme'])
            licence_url = info['protection_url']
            item.setProperty('inputstream.adaptive.license_type', info['drm_scheme'])
            if info['drm_scheme'] == 'com.widevine.alpha' or info['drm_scheme'] == 'com.microsoft.playready':
                item.setProperty('inputstream.adaptive.license_key', licence_url + "||R{SSM}|")

        # if self.offset > 0:
        #     duration = float(meta['duration']) if 'duration' in meta else 0
        #     if duration > 0:
        #         item.setProperty('StartPercent', str((self.offset / duration) * 100))

        # if self.offset > 0:
        #     item.setProperty('resumetime', str(self.offset))
        #     duration = float(meta['duration']) if 'duration' in meta else self.offset
        #     duration = duration * 1000.0
        #     item.setProperty('totaltime', str(duration))

        if 'subtitles' in info and info['subtitles'] and len(info['subtitles']) > 0:
            item.setSubtitles([sub['url'] for sub in info['subtitles']])

        return item, url, stop_event

    def __getLiveVideoInfo(self, id, latitude, longitude, cdn=None):

        proxy = control.proxy_url
        proxy = None if proxy is None or proxy == '' else {
            'http': proxy,
            'https': proxy,
        }

        credentials = auth_helper.get_credentials()

        if credentials is None:
            return None

        post_data = {
            'player': PLAYER_SLUG,
            'version': PLAYER_VERSION,
            'lat': latitude,
            'long': longitude
        }

        if cdn:
            post_data['cdn'] = cdn

        # 4452349
        hash_url = 'http://security.video.globo.com/videos/%s/hash' % id
        control.log('POST %s' % hash_url)
        control.log(post_data)
        response = requests.post(hash_url, cookies=credentials, headers={
                                                                "Accept-Encoding": "gzip",
                                                                "Content-Type": "application/x-www-form-urlencoded",
                                                                "User-Agent": "Globo Play/0 (iPhone)"
                                                            }, data=post_data, proxies=proxy)

        response.raise_for_status()

        hash_json = response.json()

        control.log(hash_json)

        hash_token = get_signed_hashes(hash_json['hash'])[0] if 'hash' in hash_json else hash_json['token']
        querystring_template = hash_json.get('query_string_template') or "h={{hash}}&k={{key}}&a={{openClosed}}&u={{user}}"

        return {
            "id": "-1",
            "title": hash_json["name"],
            # "program": playlistJson["program"],
            # "program_id": playlistJson["program_id"],
            # "provider_id": playlistJson["provider_id"],
            # "channel": playlistJson["channel"],
            # "channel_id": playlistJson["channel_id"],
            "category": 'Live',
            # "subscriber_only": playlistJson["subscriber_only"],
            "subscriber_only": 'true',
            # "exhibited_at": playlistJson["exhibited_at"],
            "player": PLAYER_SLUG,
            "url": hash_json["url"],
            "query_string_template": querystring_template,
            "thumbUri": hash_json["thumbUri"],
            "hash": hash_token,
            "user": hash_json["user"],
            "credentials": credentials,
            "encrypted": False
        }

    def sign_resource(self, resource_id, video_id, player, version, anonymous=False, cdn=None):
        proxy = control.proxy_url
        proxy = None if proxy is None or proxy == '' else {
            'http': proxy,
            'https': proxy,
        }

        if not anonymous:
            # authenticate
            credentials = auth_helper.get_credentials()
        else:
            credentials = None

        hash_url = 'https://security.video.globo.com/videos/%s/hash?resource_id=%s&version=%s&player=%s' % (video_id, resource_id, PLAYER_VERSION, PLAYER_SLUG)
        if cdn:
            hash_url = hash_url + '&cdn=' + cdn

        control.log('GET %s' % hash_url)
        response = requests.get(hash_url, cookies=credentials, headers={"Accept-Encoding": "gzip"}, proxies=proxy)

        response.raise_for_status()

        hash_json = response.json()

        if not hash_json or ('hash' not in hash_json and 'token' not in hash_json):
            message = (hash_json or {}).get('message') or control.lang(34101).encode('utf-8')
            control.log(hash_json or message, control.LOGERROR)
            control.infoDialog(message=message, sound=True, icon='ERROR')
            control.idle()
            sys.exit()

        hash_token = get_signed_hashes(hash_json['hash'])[0] if 'hash' in hash_json else hash_json['token']

        return hash_token, hash_json.get('user'), credentials

    def save_video_progress(self, credentials, program_id, video_id, milliseconds_watched, fully_watched=False):

        try:
            post_data = {
                'resource_id': video_id,
                'milliseconds_watched': int(round(milliseconds_watched)),
                'program_id': program_id,
                'fully_watched': fully_watched
            }

            control.log("--- SAVE WATCH HISTORY --- %s" % repr(post_data))
            control.log('POST %s' % HISTORY_URL)
            response = requests.post(HISTORY_URL, cookies=credentials, headers={
                                                                "Accept-Encoding": "gzip",
                                                                "Content-Type": "application/x-www-form-urlencoded",
                                                                "User-Agent": "Globo Play/0 (iPhone)"
                                                            }, data=post_data)

            response.raise_for_status()

            # import xbmcgui
            # WINDOW = xbmcgui.Window(12006)
            # WINDOW.setProperty("InfoLabelName", "the new value")

        except Exception as ex:
            control.log(traceback.format_exc(), control.LOGERROR)
            control.log("ERROR SAVING VIDEO PROGRESS (GLOBO PLAY): %s" % repr(ex))
            
            
from resources.lib.modules import control
from resources.lib.modules import util
import requests

PLAYER_VERSION = '1.1.24'
DEVICE_ID = "NmExZjhkODljZWE5YTZkZWQ3MTIzNmJhNzg3NQ=="
DEVICE_ID_KEY = "{{deviceId}}"


def get_video_router(video_id, is_live=False, cdn=None):

    proxy = control.proxy_url
    proxy = None if proxy is None or proxy == '' else {
        'http': proxy,
        'https': proxy,
    }

    cdn = cdn or 'globo'

    version = PLAYER_VERSION

    enable_4k = control.is_4k_enabled
    enable_hdr = control.setting('enable_hdr') == 'true'
    prefer_dash = control.setting('prefer_dash') == 'true'

    players_preference = []

    if enable_4k:
        if enable_hdr:
            players_preference.extend([
                'tvos_4k',
                'androidtv_hdr',
                'roku_4k_hdr',
                'webos_4k_hdr'
            ])
        else:
            players_preference.extend([
                'androidtv_sdr'
            ])

    players_preference.extend([
        'androidtv',
        'android',
        'android_native',

    ])

    container = '.mpd' if prefer_dash else None  # '.m3u8'

    selected_player = None

    response = None
    for player in players_preference:
        playlist_url = 'https://router.video.globo.com/cdn?video_id={video_id}&player_type={player}&video_type={video_type}&content_protection=widevine&quality=max&cdn={cdn}'
        final_url = playlist_url.format(video_id=video_id, player=player, video_type='Live' if is_live else 'Video', cdn=cdn)
        control.log('[Globoplay Player] - GET %s' % final_url)
        response = requests.get(final_url, headers={"Accept-Encoding": "gzip"}, proxies=proxy).json()
        control.log(response)
        if response and 'resource' in response:
            if container is None or any(container in source["url"] for source in response['resource']['sources']):
                selected_player = player
                break

    if not response:
        raise Exception("Couldn't find resource")

    resource = response['resource']
    encrypted = resource['drm_protection_enabled']

    if encrypted and resource['content_protection']['type'] != 'widevine':
        control.infoDialog(message='DRM not supported: %s' % resource['content_protection']['type'], sound=True, icon='ERROR')
        return None

    drm_scheme = 'com.widevine.alpha' if encrypted else None
    server_url = resource['content_protection']['server'] if encrypted else None

    source = resource['sources'][0]

    subtitles = []
    if 'subtitles' in source and source['subtitles']:
        for language in source['subtitles']:
            subtitle = source['subtitles'][language]
            subtitles.append({
                'language': subtitle['language'],
                'url': subtitle['url']
            })

    result = {
        "resource_id": resource['_id'],
        "id": video_id,
        "title": None,
        "program": None,
        "program_id": None,
        "provider_id": None,
        "channel": None,
        "channel_id": None,
        "category": None,
        "subscriber_only": True,
        "exhibited_at": None,
        "player": selected_player,
        "version": version,
        "url": source["url"],
        "query_string_template": source['auth_param_templates']["query_string"],
        "thumbUri": None,
        "encrypted": encrypted,
        "drm_scheme": drm_scheme,
        "protection_url": server_url.replace(DEVICE_ID_KEY, DEVICE_ID) if encrypted else None,
        'cdn': source['cdn'],
        'subtitles': subtitles
    }

    control.log(result)

    return result


def get_video_info(video_id, children_id=None, cdn=None):
    playlist_url = 'http://api.globovideos.com/videos/%s/playlist'
    playlist_json = requests.get(playlist_url % video_id, headers={"Accept-Encoding": "gzip"}).json()

    if not playlist_json or playlist_json is None or 'videos' not in playlist_json or len(playlist_json['videos']) == 0:
        message = (playlist_json or {}).get('message') or control.lang(34101).encode('utf-8')
        control.infoDialog(message=message, sound=True, icon='ERROR')
        return None

    control.log(playlist_json)

    playlist_json = playlist_json['videos'][0]

    play_children = control.setting('play_children') == 'true' or children_id is not None

    if play_children and 'children' in playlist_json and len(playlist_json['children']) > 0 and 'cuepoints' in playlist_json and len(playlist_json['cuepoints']) > 0:
        # resources = next((children for children in playlist_json['children'] if children['id]']==children_id), playlist_json['children'][0])
        return [_select_resource(children['id'], children['resources'], playlist_json, children['title'], cdn=cdn) for children in playlist_json['children']]
    else:
        return _select_resource(video_id, playlist_json['resources'], playlist_json, cdn=cdn)


def _select_resource(video_id, resources, metadata, title_override=None, cdn=None):
    resource = None
    encrypted = False
    player = 'android'
    drm_scheme = None

    enable_4k = control.is_4k_enabled
    enable_hdr = control.setting('enable_hdr') == 'true'
    prefer_dash = control.setting('prefer_dash') == 'true'
    prefer_smoothstreaming = control.setting('prefer_smoothstreaming') == 'true'
    prefer_playready = control.setting('prefer_playready') == 'true'

    if prefer_smoothstreaming:
        for node in resources:
            if 'players' in node and 'encrypted' in node and node['encrypted'] and any('smoothstreaming' in s for s in node['players']) and any('playready' in s for s in node['content_protection']):
                encrypted = True
                resource = node
                player = 'android_native'
                drm_scheme = 'com.microsoft.playready'
                server_url = resource['content_protection']['playready']['server']
                break

    if prefer_playready and not resource:
        try_player = 'androidtv_hdr' if enable_hdr else 'androidtv_sdr' if enable_4k else 'androidtv'
        for node in resources:
            if 'players' in node and 'encrypted' in node and node['encrypted'] and any(try_player in s for s in node['players']) and any('playready' in s for s in node['content_protection']):
                encrypted = True
                resource = node
                player = try_player
                drm_scheme = 'com.microsoft.playready'
                server_url = resource['content_protection']['playready']['server']
                break
        if not resource:
            for node in resources:
                if 'players' in node and 'encrypted' in node and node['encrypted'] and any('android_native' in s for s in node['players']) and any('playready' in s for s in node['content_protection']):
                    encrypted = True
                    resource = node
                    player = 'android_native'
                    drm_scheme = 'com.microsoft.playready'
                    server_url = resource['content_protection']['playready']['server']
                    break

    if not resource:
        for node in resources:
            if 'players' in node and 'encrypted' in node and node['encrypted'] and any('android_native' in s for s in node['players']) and any('widevine' in s for s in node['content_protection']):
                encrypted = True
                resource = node
                player = 'android_native'
                drm_scheme = 'com.widevine.alpha'
                server_url = resource['content_protection']['widevine']['server']
                break

    if not resource and enable_4k and prefer_dash:
        for node in resources:
            if 'players' in node and any('tv_4k_dash' in s for s in node['players']):
                resource = node
                player = 'tv_4k_dash'
                break

    if not resource and prefer_dash:
        for node in resources:
            if 'players' in node and any('tv_dash' in s for s in node['players']):
                resource = node
                player = 'tv_dash'
                break

    if not resource and enable_4k and (not prefer_dash or not control.is_inputstream_available()):
        for node in resources:
            if 'players' in node and any('tvos_4k' in s for s in node['players']) and '2160' in node['_id'] and not node.get('encrypted', False):
                resource = node
                player = 'tvos_4k'
                break

    if not resource and enable_4k and enable_hdr:
        for node in resources:
            # if 'players' in node and 'height' in node and node['height'] == 2160 and any('androidtv_hdr' in s for s in node['players']):
            if 'players' in node and any('androidtv_hdr' in s for s in node['players']):
                resource = node
                player = 'androidtv_hdr'
                break

    if not resource and enable_4k:
        for node in resources:
            # if 'players' in node and 'height' in node and node['height'] == 2160 and any('androidtv_sdr' in s for s in node['players']):
            if 'players' in node and any('androidtv_sdr' in s for s in node['players']):
                resource = node
                player = 'androidtv_sdr'
                break

    #Prefer MP4 when available
    if not resource:
        for node in resources:
            if 'players' in node and 'height' in node and node['height'] == 720 and any('desktop' in s for s in node['players']):
                resource = node
                player = 'android'
                break

    if not resource:
        for node in resources:
            if 'players' in node and any('androidtv' in s for s in node['players']):
                resource = node
                player = 'androidtv'
                break

    if not resource:
        for node in resources:
            if 'players' in node and any('android' in s for s in node['players']):
                resource = node
                player = 'android'
                break

    if (resource or None) is None:
        control.infoDialog(message=control.lang(34102).encode('utf-8'), sound=True, icon='ERROR')
        return None

    control.log('Selected resource for video %s: %s' % (video_id, resource['_id']))

    subtitles = []
    for subtitle in resources:
        if 'type' in subtitle and subtitle['type'] == 'subtitle':
            control.log('Found Subtitle: %s' % subtitle['url'])
            subtitles.append({
                'language': subtitle['language'],
                'url': subtitle['url']
            })

    cdn_data = resource['cdns'][cdn] if cdn in resource['cdns'] else None
    if cdn_data:
        domain = cdn_data['domain']
        query_string_template = cdn_data['query_string_template']
        path = resource['paths']['max']
        url = domain + path
    else:
        query_string_template = resource["query_string_template"]
        url = resource["url"]
        cdn = 'globo'

    result = {
        "resource_id": resource['_id'],
        "id": video_id,
        "title": title_override or metadata["title"],
        "program": metadata["program"],
        "program_id": metadata["program_id"],
        "provider_id": metadata["provider_id"],
        "channel": metadata["channel"],
        "channel_id": metadata["channel_id"],
        "category": metadata["category"],
        "subscriber_only": metadata["subscriber_only"],
        "exhibited_at": metadata["exhibited_at"],
        "player": player,
        "version": PLAYER_VERSION,
        "url": url,
        "cdn": cdn,
        "query_string_template": query_string_template,
        "thumbUri": resource["thumbUri"] if 'thumbUri' in resource else None,
        "encrypted": encrypted,
        "drm_scheme": drm_scheme,
        "protection_url": server_url.replace(DEVICE_ID_KEY, DEVICE_ID) if encrypted else None,
        'subtitles': subtitles
    }

    control.log(result)

    return result


def get_geofence_video_info(video_id, latitude, longitude, credentials, cdn=None):

    if credentials is None:
        return None

    proxy = control.proxy_url
    proxy = None if proxy is None or proxy == '' else {
        'http': proxy,
        'https': proxy,
    }

    version = PLAYER_VERSION

    # enable_4k = control.is_4k_enabled
    # enable_hdr = control.setting('enable_hdr') == 'true'

    players_preference = []

    # if enable_4k:
    #     if enable_hdr:
    #         players_preference.extend([
    #             'androidtv_hdr',
    #         ])
    #     else:
    #         players_preference.extend([
    #             'androidtv_sdr'
    #         ])

    players_preference.extend([
        # 'androidtv',
        'android',
        # 'android_native',

    ])

    selected_player = players_preference[0]

    post_data = {
        'player': selected_player,
        'version': version,
        'lat': latitude,
        'long': longitude,
        'cdn': cdn or 'globo'
    }

    # tz:       00:00
    # player:  ios_native
    # cdn:     globo
    # ts:      1613693205
    # udid:    bbec61e5f3a06ca54624e84accc232b5d49971a6
    # version: 10.25.0
    # lat:     51.49502563476562
    # long:    -0.03278398965019131

    hash_url = 'http://security.video.globo.com/videos/%s/hash' % video_id
    control.log('POST %s' % hash_url)
    control.log(post_data)
    control.log(credentials)
    response = requests.post(hash_url, cookies=credentials, headers={
                                                            "Accept-Encoding": "gzip",
                                                            "Content-Type": "application/x-www-form-urlencoded",
                                                            "User-Agent": "Canais Globo (Globosat Play)/444 (iPhone)"
                                                        }, data=post_data, proxies=proxy)

    response.raise_for_status()

    hash_json = response.json()

    control.log(hash_json)

    return {
        "id": video_id,
        "title": hash_json.get("name"),
        "category": 'Live',
        "subscriber_only": True,
        "channel": None,
        "player": selected_player,
        "url": hash_json.get("url"),
        "query_string_template": hash_json.get('query_string_template') or "h={{hash}}&k={{key}}&a={{openClosed}}&u={{user}}",
        "thumbUri": hash_json.get("thumbUri"),
        "hash_token": util.get_signed_hashes(hash_json.get('hash'))[0] if 'hash' in hash_json else hash_json.get('token'),
        "user": hash_json.get("user"),
        "credentials": credentials,
        "encrypted": hash_json.get('encrypted', False)
    }


def get_session(video_id, token):
    proxy = control.proxy_url
    proxy = None if proxy is None or proxy == '' else {
        'http': proxy,
        'https': proxy,
    }

    url = 'https://playback.video.globo.com/v1/video-session'
    data = {
        'content_protection': "widevine",
        'player_type': "app",  # "desktop",
        'quality': "max",
        'video_id': video_id
    }

    headers = {
                "Accept-Encoding": "gzip",
                "authorization": "Bearer " + token,
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Canais Globo (Globosat Play)/444 (iPhone)"
            }

    requests.post(url, json=data, headers=headers, proxies=proxy)
    
    
    
    
    #! /usr/bin/python3
import requests
import os

def grab(url):
    response = requests.get(url, timeout = 15).text
    if '.m3u8' not in response:
        print("https://bit.ly/3xRjEnQ")
        return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end - tuner : end]:
            link = response[end - tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

with open('./GLOBO.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('##'):
            continue
        if not line.startswith('https:'):
            line = line.split('-')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            print(f'\n#EXTM3U')
            print(f'\n#EXTINF:-1 group-title="{grp_title}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
