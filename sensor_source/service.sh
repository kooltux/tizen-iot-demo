#!/bin/bash

rfkill unblock all

. /etc/iot/network.conf

trap "echo 'Releasing rfcomm...'; killall rfcomm" STOP INT QUIT EXIT

insmod /usr/bin/low-speed-spidev.ko

killall -9 mpu9250_sample
DIR=$(cd $(dirname $0) && pwd -P)
$DIR/sensor_analyzer $IOT_COMM_ROUTER $IOT_ROUTER_BT 1


