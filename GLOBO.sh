#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/

python3 GLOBO.py > ./GLOBO.m3u

echo m3u grabbed
