#!/usr/bin/env bash

sudo rm /etc/xdg/autostart/startAP.desktop
sudo rm /etc/udev/rules.d/70-persistent-net.rules
sudo systemctl disable dnsmasq
sudo cp /etc/network/interfaces_original /etc/network/interfaces
sudo bash -c 'cat<<EOF > /etc/systemd/system/dhcpcd.service

[Unit]
Description=dhcpcd on all interfaces
Wants=network.target
Before=network.target

[Service]
Type=forking
PIDFile=/run/dhcpcd.pid
ExecStart=/sbin/dhcpcd5

[Install]
WantedBy=multi-user.target
Alias=dhcpcd5.service
EOF
'
sudo systemctl enable dhcpcd
sudo reboot
