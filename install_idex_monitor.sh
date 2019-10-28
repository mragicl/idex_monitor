#!/bin/bash
docker create grafana-storage
docker create influxdb-storage
docker pull mragicl/docker-idex-monitor
docker run -d   --name docker-idex-monitor   -p 3003:3003   -p 3004:8888   -p 8086:8086   -v influxdb-storage:/var/lib/influxdb   -v grafana-storage:/var/lib/grafana   mragicl/docker-idex-monitor
