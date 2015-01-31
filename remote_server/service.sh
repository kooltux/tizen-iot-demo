#!/bin/bash

DIR=$(cd $(dirname $0) && pwd -P)
echo "Starting auto-yes-agent"
killall auto-yes-agent
PYTHONPATH=/usr/lib64/bluez/test/ $DIR/auto-yes-agent &

sleep 1

echo "Running as root..." >&2
exec sudo $DIR/service_root.sh

