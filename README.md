# Simultaneous AP and Managed Mode Wifi on Raspberry Pi

###### Special thanks to: https://albeec13.github.io/2017/09/26/raspberry-pi-zero-w-simultaneous-ap-and-managed-mode-wifi/


## Usage

Run as normal user

```sh
git clone https://github.com/raspberrypisig/rpi-wifi
cd rpi-wifi
./rpi-wifi
./rpi-wifi -a <AP_SSID> <AP_password> -c <WIFI_SSID> <WIFI_password>
```

Replace:

* AP_SSID : The SSID of your AP (eg. RPIAP)
* AP_password: AP password
* WIFI_SSID : The normal wifi that you connect with on your pi
* WIFI_password: The password for the wifi

Running the script above will do all the legwork to setup Raspberry Pi as both AP and normal client(managed mode) using the onboard
WIFI chip of the Raspberry Pi 3. It will reboot automatically when done.

When your pi boots again, wait about a minute, then shutoff. Power again, wait 30 seconds, then run

```sh
dmesg
```

You should see the following line:

```text
[RPI AP] Simultaneous WIFI AP Mode started.
```

Now your AP is ready.

# Troubleshooting

### Wifi channel

In dmesg, if you see a lot of errors from the brcmfmac driver, trying using another WIFI channel in /etc/hostapd/hostapd.conf

In Australia, try one of 1,6 or 11



