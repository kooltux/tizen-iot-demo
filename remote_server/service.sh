#!/bin/bash

rfkill unblock all

. /etc/iot/network.conf

trap "echo 'Releasing rfcomm...';rfcomm release $IOT_COMM_ROUTER; killall rfcomm >/dev/null 2>&1" STOP INT QUIT EXIT

DIR=$(cd $(dirname $0) && pwd -P)
rfcomm -r watch $IOT_COMM_SERVER 1 $DIR/post_event {} http://localhost:8080/event

