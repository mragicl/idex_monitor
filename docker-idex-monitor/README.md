# Docker Image with InfluxDB and Grafana, with preconfigured Dashboard to monitor idex stats

Based on the persistent influxdb and grafana docker image, see https://hub.docker.com/r/philhawthorne/docker-influxdb-grafana/


## Quick Start

To start the container with persistence you can use the following:

```sh
docker create grafana-storage
docker create influxdb-storage
docker run -d \
  --name docker-idex-monitor \
  -p 3003:3003 \
  -p 3004:8083 \
  -p 8086:8086 \
  -v influxdb-storage:/var/lib/influxdb \
  -v grafana-storage:/var/lib/grafana \
  mragicl/docker-idex-monitor:latest
```

To stop the container launch:

```sh
docker stop docker-idex-monitor
```

To start the container again launch:

```sh
docker start docker-idex-monitor
```

## Mapped Ports

```
Host		Container		Service

3003		3003			grafana
3004		8083			chronograf
8086		8086			influxdb
```
## SSH

```sh
docker exec -it <CONTAINER_ID> bash
```

## Grafana

Open http://localhost:3003

```
Username: root
Password: root
```

Open the dashboard idex_monitoring.


## InfluxDB

The python script in the github repository (https://github.com/mragicl/idex_monitor ) is used to write
idex monitor data to the influxdb, which is then displayed in grafana.