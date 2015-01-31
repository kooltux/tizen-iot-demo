#!/bin/bash

rfkill unblock all

. /etc/iot/network.conf

cat /dev/zero >/dev/fb1

trap "echo 'Releasing rfcomm...';rfcomm release $IOT_COMM_ROUTER; killall rfcomm >/dev/null 2>&1" STOP INT QUIT EXIT

DIR=$(cd $(dirname $0) && pwd -P)
rfcomm -r watch $IOT_COMM_ROUTER 1 $DIR/event_router {} $IOT_COMM_SERVER $IOT_SERVER_BT 2


