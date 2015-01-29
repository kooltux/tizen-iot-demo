#!/bin/bash

rfkill unblock all

. /etc/iot/network.conf

PID=0
trap 'echo "Terminating rfcomm...";kill $PID >/dev/null 2>&1; killall rfcomm >/dev/null 2>&1' STOP INT QUIT EXIT

insmod /usr/bin/low-speed-spidev.ko

( while [ 1 ]; do rfcomm -r connect $IOT_COMM_SENSOR $IOT_ROUTER_BT; sleep 1; done ) &
PID=$!

./sensor_analyzer $IOT_COMM_SENSOR


