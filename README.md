# raspi-remote

Raspberry Pi voice-controlled assistant powered by Jasper and LIRC.

This repository contains ansible configurations to install the required things into a
Raspberry Pi with freshly flashed Raspbian.

## Preparations

* install [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) to the RasPi
* install ansible (`pip3 install -r requirements.txt` will do)
* set up your SSH key to the Raspberry Pi

## Install

## Background

This configuration will also set up a secondary LIRC instance because with gpio_ir module it's
not possible to do reception and transmission with same instance. This is based on
[these instructions](http://lirc.org/html/configuration-guide.html#appendix-9).
