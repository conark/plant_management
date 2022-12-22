#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Import necessary libraries
import os
from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep
import time
import datetime
import schedule
import requests
import storeFileFB
import json
from dotenv import load_dotenv
import os

# load .env　file
load_dotenv()

BLYNK_AUTH = os.getenv ('BLYNK_AUTH')

# Initialize the camera and sensehat
sense = SenseHat()
camera = PiCamera()

# Set camera settings
camera.resolution = (1280, 720)  # Set resolution
camera.framerate = 30  # Set frame rate
camera.start_preview()


 # for test pourpose, instead of use schedule, use set time.sleep for 12 seconds   #time.sleep(12) #12 sec
def green_light():
  sense.clear(0, 255, 0)
  #time.sleep(12) #12 sec
  time.sleep(1)


def red_light():
  sense.clear(255, 0, 0)
  #time.sleep(12) #12 sec
  time.sleep(1)

def off_light():
  sense.clear()
  time.sleep(1)


def imageCap():
  # turn off light and take a picture
  sense.clear()
  # sense.clear(255,255,255) #for white light
  # set the location of image file and current time
  currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  image = f'/home/pi/plant_management/plant_factory_environment_management/image/{currentTime}.jpg'
  camera.capture(image)
  #camera.capture('image/image.jpg')
  print(f'pic taken at {currentTime}') # print frame number to console
  # store to firebase
  storeFileFB.store_file(image)
  storeFileFB.push_db(image, currentTime)
  print('Image stored and location pushed to db')
  time.sleep(5)

#####################################################
# schedule everyday at 7:55am take pic, 8am and 8pm lights turn on

# schedule.every().day.at("7:55").do(imageCap)
# schedule.every().day.at("8:00").do(red_light)
# schedule.every().day.at("20:00").do(green_light)
######################################################
# test schedule
schedule.every().day.at("10:50").do(imageCap)
schedule.every().day.at("10:51").do(red_light)
schedule.every().day.at("10:52").do(green_light)
schedule.every().day.at("10:55").do(off_light)

# notification for feeding time
def feedMorning():
  requests.get("https://blynk.cloud/external/api/logEvent?token="+(os.environ['BLYNK_AUTH'])+"&code=feed_morning")  

def feedEvening():
  requests.get("https://blynk.cloud/external/api/logEvent?token="+(os.environ['BLYNK_AUTH'])+"&code=feed_evening")  

#####################################################
# schedule everyday at 9:00am,18:00am send notification
#schedule.every().day.at("9:00").do(feedMorning)
#schedule.every().day.at("18:00").do(feedEvening)
#####################################################
# test schedule
schedule.every().day.at("10:53").do(feedMorning)
schedule.every().day.at("10:54").do(feedEvening)


while True:

  schedule.run_pending()
  time.sleep(1)
  
#when not using schedule
  # sense.clear()
  # imageCap()  
  # red_light()
  # green_light()



