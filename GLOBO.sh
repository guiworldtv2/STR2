#!/bin/bash

echo $(dirname $0)

python -m pip install requests

cd $(dirname $0)/scripts/

python GLOBO.py > ../GLOBO.m3u

echo m3u grabbed
