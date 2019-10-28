#!/bin/bash -e

# We need to ensure this directory is writeable on start of the container
chmod 0777 -R /var/lib/grafana

exec /usr/bin/supervisord
