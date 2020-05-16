#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
#picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import board
import adafruit_dht

logging.basicConfig(level=logging.DEBUG)

# Initial the dht device, with data pin connected to:
logging.info("Starting DHT22 humidity sensor")
dhtDevice = adafruit_dht.DHT22(board.D21)

logging.info("Starting ePaper Displayer")
epd = epd2in7.EPD()

def center_text(draw, text, width, y, font):
    w, h = draw.textsize(text, font=font)
    x = int(width/2 - w/2)
    draw.text((x,y), text, font=font, fill=0)

def read_humidity_sensor():
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        return { "temperature_c": temperature_c, "humidity": humidity }
    except Exception as e:
        logging.error(e)
        return None

def update_display():
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    font18 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    font32 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)

    logging.info("Drawing date and time")
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    datetxt = time.strftime("%d.%m.%Y", time.localtime())
    # In horizontal mode height is sort of width
    center_text(draw, datetxt, epd.height, 10, font18)
    timetxt = time.strftime("%H:%M", time.localtime())
    center_text(draw, timetxt, epd.height, 34, font32)

    sensor = read_humidity_sensor()
    if sensor is not None:
        temptxt = "{:.1f} °C".format(sensor["temperature_c"])
        center_text(draw, temptxt, epd.height, 80, font32)
        humtxt = "Hum. {:.1f} %".format(sensor["humidity"])
        center_text(draw, humtxt, epd.height, 120, font32)

    epd.display(epd.getbuffer(image))
    time.sleep(2)

    logging.info("Goto Sleep...")
    epd.sleep()

try:
    while True:
        update_display()
        time.sleep(180)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()