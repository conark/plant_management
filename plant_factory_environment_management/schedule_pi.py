# Import necessary libraries
from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep
import time
import datetime
import schedule
import requests
import storeFileFB
import json

# Initialize the camera and sensehat
sense = SenseHat()
camera = PiCamera()

# Set camera settings
camera.resolution = (1280, 720)  # Set resolution
camera.framerate = 30  # Set frame rate
camera.start_preview()


 # for test pourpose, set time.sleep for 12 seconds
def green_light():
  sense.clear(0, 255, 0)
  #time.sleep(12 * 60) #12 min
  #time.sleep(12) #12 sec
  time.sleep(1)

def red_light():
  sense.clear(255, 0, 0)
  #time.sleep(12 * 60) #12 min
  #time.sleep(12) #12 sec
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
schedule.every().day.at("11:16").do(imageCap)
schedule.every().day.at("11:17").do(red_light)
schedule.every().day.at("11:20").do(green_light)


def feedMorning():
  requests.get("https://blynk.cloud/external/api/logEvent?token=fFBWjj108jcqQ7XmRXeDQ4MCMHJ3os6_&code=feed_morning")  

def feedEvening():
  requests.get("https://blynk.cloud/external/api/logEvent?token=fFBWjj108jcqQ7XmRXeDQ4MCMHJ3os6_&code=feed_evening")  

#####################################################
# schedule everyday at 9:00am,18:00am send notification
#schedule.every().day.at("9:00").do(feedMorning)
#schedule.every().day.at("18:00").do(feedEvening)
#####################################################
# test schedule
schedule.every().day.at("11:18").do(feedMorning)
schedule.every().day.at("11:21").do(feedEvening)


while True:
  sense.clear()
  schedule.run_pending()
  imageCap()  
  red_light()
  green_light()
  time.sleep(1)
  sense.clear()

  ####################################
  #schedule.run_pending()
  #time.sleep(1)
  #sense.clear()
  ####################################



