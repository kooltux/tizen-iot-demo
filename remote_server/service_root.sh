#!/bin/bash

rfkill unblock all

. /etc/iot/network.conf

PID=0
trap "echo 'Releasing rfcomm...';rfcomm release $IOT_COMM_SERVER; killall rfcomm >/dev/null 2>&1;kill $PID" STOP INT QUIT EXIT

DIR=$(cd $(dirname $0) && pwd -P)

$DIR/cloud_server &
PID=$!

rfcomm -r watch $IOT_COMM_SERVER 2 $DIR/post_event {} http://localhost:8080/event/post


