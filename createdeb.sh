#!/usr/bin/env bash
set -x
fpm --verbose -s dir -t deb -n rpiwifi -p dist src/scripts/=/usr/local/bin dist/elf/rpiwifigui=/usr/local/bin files/wifi.png=/usr/share/pixmaps/wifi.png files/rpi-wifi.desktop=/usr/share/applications/rpi-wifi.desktop files/rpi-wifi-link.desktop=/home/pi/Desktop/rpi-wifi-link.desktop
