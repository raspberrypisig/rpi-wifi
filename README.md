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
