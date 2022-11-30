#!/bin/bash

# TVI - update the stream URL of BIG BROTHER

sed -i "/live_tvi\/live_tvi/ c https://video-auth7.iol.pt/live_tvi_direct/live_tvi_direct/edge_servers/tvireality-720_passthrough/chunks.m3u8?wmsAuthSign=$(wget https://services.iol.pt/matrix?userId= -o /dev/null -O -)/" BIG_BROTHER_PORTUGAL_LIVE.m3u8
   
exit 0
