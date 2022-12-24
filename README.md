
# Plant Factory Environment Management
![greenhouse-g005435a15_1920](https://user-images.githubusercontent.com/62657957/201473476-76da5457-6719-4da1-8280-bd0b45de6ff4.jpg)


# **Plant Factory - Environment Management** 


# New Agriculture Style
Smart & Sustanable 

Due to the population increasing, it is said that a food crisis will occur throughout the world within the near future. In Ireland, a country which relies on importing  most of its food, vegetable and fruit farming is not the thriving industry that it is in other countries due to problems with weather and soil. 
 food can be grown anywhere by hydroponics or film cultivation. Plant  factories are easier to manage using technology, so we can counter any atypical growing environment to  cultivate efficient and clean farming.

# Environmental Management with IoT

The environmental control system requires using cameras to monitor and record multiple growth factors such as temperature, humidity, light. Timers indicate when to open and close pipe valves. 

# **Project Diagram**

![Project Diagram 1 (2)](https://user-images.githubusercontent.com/62657957/209211790-c93e678e-9315-4b24-b421-242028f87410.png)


🧚 **Programming languages**

- Python
- Javascript

🧚 **Proposed tech – Software**

- Firebase (Storage, Web hosting)
- Blynk (temp, humidity, notification/alarm)
- Youtube (Live streaming)

🧚 **Proposed tech - Hardware**

- Raspberry Pi 4B
- Sense hat
- Raspberry Pi Camera module
- USB connect Web camera (Logicool HD720p)
- A Box as Factory 

# **Functions**

1. Shine the LED light on the plant - set it to alternate between red and green light every 12 seconds. (Originally every 12 hours)
2. Measure and display temperature/humidity on Blynk
3. Feed timing alarm every 12 seconds on Blynk (originally every 12 hours).
4. Real-time monitoring with Web camera on youtube.
5. Send a notification/message to the phone if the temp/humidity is outside of expected range.
6. Schedule for taking photo for Recognition of harvest time 
7. Recognition of harvest time (e.g. if tomato became red) 
7. Web hosting for latest updated photo


# **Prepareraion**

🧚 **Rasberry pi**

 - Attach the sense hat, camera module, and webcam (USB port) to the raspberry pi.
<img src="https://user-images.githubusercontent.com/62657957/209018247-5441610a-aa4c-4e98-b1f4-00bba3289a25.jpg" width="420" height="280">
 
 - Configure the Raspberry Pi to use VS Code with SSH connection.
 
 - Raspberry Pi config setting  - Camera enable on

🧚 **Blynk**

 - Install Blynk Library

 - Create template
<img src="https://user-images.githubusercontent.com/62657957/209017081-c1e28274-f1a5-4554-a6f2-84836ac75100.png" width="420" height="280">

 - Datastreams setting - Virtual Pin
 
<img src="https://user-images.githubusercontent.com/62657957/209016904-0e57990b-ace3-466c-9605-75c96a4e37f0.png" width="420" height="280">

<img src="https://user-images.githubusercontent.com/62657957/209016854-320c52f3-fc65-4815-bdda-4ac062c91792.png" width="420" height="280">

 - Create Events
<img src="https://user-images.githubusercontent.com/62657957/209016745-2347bff6-0384-49d4-b714-6ace0b2b6e52.png" width="420" height="280">

<img src="https://user-images.githubusercontent.com/62657957/209016785-81237ce4-ab17-40c2-bfee-86f66c95ff5c.png" width="420" height="280">

<img src="https://user-images.githubusercontent.com/62657957/209016556-e3d23ee9-9056-45c2-a893-c7f257fc02a6.png" width="420" height="280">

 - Web dashboad set up (Youtube URL added on Video widget, Datastream setting on Gauge and chart)
<img src="https://user-images.githubusercontent.com/62657957/209016407-e2d938e1-beb3-478e-acf8-62f1bea6d2f8.png" width="420" height="280">
<img src="https://user-images.githubusercontent.com/62657957/209016288-b81ce3cb-8b5f-405c-a126-c229bd045069.png" width="420" height="280">
<img src="https://user-images.githubusercontent.com/62657957/209015912-3157addb-cefd-4a1d-8786-843902d0fbd5.png" width="420" height="280">
<img src="https://user-images.githubusercontent.com/62657957/209015923-fe7920ea-7422-444f-999a-92e1d832399e.png" width="420" height="280">

 - download mobile app and set up widget
 
<img src="https://user-images.githubusercontent.com/62657957/209016028-c4d56f8c-6867-4c63-82bc-ca480aee31d6.png" width="150" height="280">
<img src="https://user-images.githubusercontent.com/62657957/209016101-199a5adf-23bc-446f-9bd7-f276de59f78c.png" width="150" height="280">


🧚 **Youtube (Live streaming)**

 - Request access to live stream on Youtube Studio
 - Create Live schedule and get stream key
 - install FFmpeg on Raspberry pi

🧚 **Firebase**
 - install firebase tool to Raspberry pi
 - Create project on Firebase console

<img src="https://user-images.githubusercontent.com/62657957/209023745-1749ed97-eab7-49e3-b7e2-bc41cf333850.png" width="420" height="280">


# **Overview**

🌱 **temp_humid.py:**

To Run type in the command: python3 temp_humid.py

(1) Get temperature and humidity with Sense Hat and communicate with Blynk.

(2) If the temperature is above or below the set temperature, send a logEvent request with a code of either temp_too_high or temp_too_low to the Blynk server. Similarly, if the humidity is above or below the configured humidity, it will send a logEvent request with either the code humidity_too_high or humidity_too_low to the Blynk server. This will notify you via popup and email in the Blynk application.

🌱 **schedule_pi.py:**

To Run type in the command: python3 schedule_pi.py

It schedules light lighting and light color switch schedule, feeding time alarm, and image capture.

(1) The LED light of the sense hat is set with the python schedule library that it lights up in red or green at a set time.

(2) Capture an image at a set time and automatically save it to Firebase storage using the storeFileFB.py function. During image capture, turn off the lights (there is a white setting if it's dark) and save a color correct photo for color recognition.

(3) Send an HTTP GET request to the URL and send a log event to the API endpoint using Python's requests library to notify the feeding time of water etc. Blynk's Event settings will send push notifications and emails.

🌱 **storeFileFB.py**

Upload files to Google Cloud Storage and push filenames to Realtime Database

🌱 **streaming.py**

To Run type in the command: python3 streaming.py

Using Python's subprocess module to run the streaming.sh script

🌱 **streaming.sh**

A script that uses ffmpeg commands to start YouTube Live streaming.
If don't use streaming.py, able to run with ./streaming.sh

🌱 **colour_detect.py**

To Run type in the command: python3 colour_detect.py 

Recognition of harvest time (e.g. if tomato became red) 

Send a notification to Blynk if  a red color in the latest image.

🌱 **Web hosting**

👉 firebase-hosting: https://plant-factory-d18f0.web.app/

👉 glitch: https://plant-factory-project.glitch.me/

Use Firebase's Realtime Database and Cloud Storage to get the URL of the latest image and display it




