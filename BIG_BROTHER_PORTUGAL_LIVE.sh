#!/bin/bash

# TVI Reality - update the stream URL of TVI Reality

# Verifica se o arquivo BIG_BROTHER_PORTUGAL_LIVE.M3U8 existe
if [ ! -f BIG_BROTHER_PORTUGAL_LIVE.M3U8 ]; then
    echo "Arquivo BIG_BROTHER_PORTUGAL_LIVE.M3U8 não encontrado."
    exit 1
fi

# Obtém o token de autenticação
auth_sign=$(wget https://services.iol.pt/matrix?userId= -o /dev/null -O -)

# Verifica se o comando wget retornou sucesso
if [ $? -ne 0 ]; then
    echo "Erro ao obter o token de autenticação."
    exit 1
fi

# Atualiza a URL da transmissão
sed -i "/live_tvi_direct/ c https://video-auth4.iol.pt/live_tvi_direct/live_tvi_direct/edge_servers/tvireality-720_passthrough/playlist.m3u8?wmsAuthSign=${auth_sign}/" BIG_BROTHER_PORTUGAL_LIVE.M3U8

# Verifica se o comando sed retornou sucesso
if [ $? -ne 0 ]; then
    echo "Erro ao atualizar a URL da transmissão."
    exit 1
fi

exit 0
