# raspi-remote

Raspberry Pi web-enabled remote control powered by LIRC, Node-Red and Mosquitto.

This repository contains ansible configurations to install the required things into a
Raspberry Pi with freshly flashed Raspbian, and a tiny python web app to display
a user interface.

## Preparations

* install [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) to the RasPi
* install ansible (`cd ansible; pip3 install -r requirements.txt` will do)
* set up your SSH key to the Raspberry Pi

Make sure your pi is accessible via ssh with name "raspberrypi.local" (or modify `inventory/default.yml`).

## Install

In ansible directory:

`ansible-playbook -i inventory/default.yml playbook.yml`

## Background

This configuration will also set up a secondary LIRC instance because with gpio_ir module it's
not possible to do reception and transmission with same instance. This is based on
[these instructions](http://lirc.org/html/configuration-guide.html#appendix-9).
