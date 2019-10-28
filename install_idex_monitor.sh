#!/bin/bash

#just in case virtualenv is not installed
sudo apt install -y python-virtualenv
docker pull mragicl/docker-idex-monitor
docker volume create grafana-storage
docker volume create influxdb-storage
docker run -d   --name docker-idex-monitor   -p 3003:3003   -p 3004:8888   -p 8086:8086   -v influxdb-storage:/var/lib/influxdb   -v grafana-storage:/var/lib/grafana   mragicl/docker-idex-monitor

virtualenv -p python3.6 venv/idex_monitor
source venv/idex_monitor/bin/activate
pip install -r python/requirements.txt
