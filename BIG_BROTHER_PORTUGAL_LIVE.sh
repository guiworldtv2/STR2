#!/bin/bash

# TVI Reality - update the stream URL of TVI Reality

sed -i "/live_tvi_direct/ c https://video-auth4.iol.pt/live_tvi_direct/live_tvi_direct/edge_servers/tvireality-720_passthrough/playlist.m3u8?wmsAuthSign=$(wget https://services.iol.pt/matrix?userId= -o /dev/null -O -)/" m3upt.m3u

exit 0
