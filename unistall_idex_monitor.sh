#!/bin/bash
docker stop docker-idex-monitor
docker rm docker-idex-monitor
docker image rm docker-idex-monitor
docker volume rm grafana-storage
docker volume rm influxdb-storage
