# raspi-remote

Original idea was a Raspberry Pi web-enabled remote control powered by LIRC, Node-Red and Mosquitto.

In practice this is turning out a collection of ansible roles and bits&pieces to try out with Raspberry Pi.

This repository contains ansible configurations to install the required things into a
Raspberry Pi with freshly flashed Raspbian, and a tiny python web app to display
a user interface.

## Hardware Setup

### Infrared transmitter

Get something like this: https://www.sparkfun.com/products/retired/10732

And connect:
* VCC to 5V (e.g. Pin 4 on Raspberry Pi 3B)
* GND to GND (e.g. Pin 6)
* CTL to GPIO27 (Pin 13) (or whichever you [configure](https://github.com/tfager/raspi-remote/blob/master/ansible/roles/gpio-ir/tasks/main.yml#L13))

### ePaper display

Get this: https://www.waveshare.com/2.7inch-e-paper-hat.htm

In my case, I wanted to connect other things on the RasPi besides the ePaper HAT,
so I used the separate connector with colored wires. In my case it was like this:

HAT|Wire|RasPi
---|:---|---
VCC| Red |17|
GND| Black | 9 |
DIN | Blue | 19 (GPIO10)
CLK | Yellow | 23 (GPIO11)
CS  | Orange | 24 (GPIO8)
DC  | Green | 22 (GPIO25)
RST | White | 11 (GPIO17)
BUSY| Purple | 18 (GPIO24)

### DHT22 humidity sensor

This: https://ihmevekotin.fi/product/262_dht22-digitaalinen-l%C3%A4mp%C3%B6tila-ja-ilmankosteusanturi

And connect (numbers counting from left to right, facing the text on DHT22):
* 1 VCC - 5V (RasPi Pin 2)
* 2 CTL - GPIO21 (RasPi Pin 40)
* 3 not connected
* 4 GND - GND (RasPi Pin 39)

### BangleJS Smartwatch

I found one more thing to integrate in the RasPi-remote, which would be the
[BangleJS smartwatch](https://banglejs.com/). It can be connected to MQTT with
EspruinoHub as explained in [this tutorial](https://www.espruino.com/BLE+Node-RED).

## Software Setup

* install [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) to the RasPi
* install ansible (`cd ansible; pip3 install -r requirements.txt` will do)
* set up your SSH key to the Raspberry Pi

Make sure your pi is accessible via ssh with name "raspberrypi.local" (or modify `inventory/default.yml`).

### Note on LIRC

This configuration will also set up a secondary LIRC instance because with gpio_ir module it's
not possible to do reception and transmission with same instance. This is based on
[these instructions](http://lirc.org/html/configuration-guide.html#appendix-9).

## Install

In ansible directory:

`ansible-playbook -i inventory/default.yml playbook.yml`

