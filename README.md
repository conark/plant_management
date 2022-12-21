
# plant_factory_environment_management
![greenhouse-g005435a15_1920](https://user-images.githubusercontent.com/62657957/201473476-76da5457-6719-4da1-8280-bd0b45de6ff4.jpg)


# **Plant Factory - Environment Management** 


# New Agriculture Style
Smart & Sustanable 

Due to the population increasing, it is said that a food crisis will occur throughout the world within the near future. In Ireland, a country which relies on importing  most of its food, vegetable and fruit farming is not the thriving industry that it is in other countries due to problems with weather and soil. 

Today, various technologies have been incorporated into agriculture. This creates an environment in which vegetables and fruits can be grown even in suboptimal conditions. One option we can examine is a plant  factory. In a plant factory, plants are grown indoors so they are not affected by the weather. In addition,  since the factory does not use soil, food can be grown anywhere by hydroponics or film cultivation. Plant  factories are easier to manage using technology, so we can counter any atypical growing environment to  cultivate efficient and clean farming.

# Environmental Management with IoT

The environmental control system requires using cameras to monitor and record multiple growth factors such as temperature, humidity, light. Timers indicate when to open and close pipe valves. 

**Programming languages**

- Python

**Proposed tech – Software**

- Firebase (Storage, Web hosting)
- Blynk (temp, humidity, notification/alarm)
- Youtube (Live streaming)

**Proposed tech - Hardware**

- Raspberry Pi
- Sensor hat
- Raspberry Pi Camera module
- USB connect Web camera (Logicool HD720p)
- A Box as Factory 

# **Functions**

1. Shine the LED light on the plant - set it to alternate between red and green light every 12 seconds. (Originally every 12 hours)
2. Measure and display temperature/humidity on Blynk
3. Feed timing alarm every 12 seconds on Blynk (originally every 12 hours).
4. Real-time monitoring with Web camera on youtube.
5. Send a notification/message to the phone if the temp/humidity is outside of expected range.
6. Schedule for taking photo for Recognition of harvest time (e.g. if tomato became red) not implemented code for recognition of harvest time
7. Web hosting for latest updated photo


# **Prepareraion**

• Rasberry pi 

 - Attach the sense hat, camera module, and webcam (USB port) to the raspberry pi.
<img src="https://user-images.githubusercontent.com/62657957/209018247-5441610a-aa4c-4e98-b1f4-00bba3289a25.jpg"width="200" height="400" />
![PXL_20221221_224914983](https://user-images.githubusercontent.com/62657957/209018247-5441610a-aa4c-4e98-b1f4-00bba3289a25.jpg)
 - Configure the Raspberry Pi to use VS Code with SSH connection.
 - Raspberry Pi config setting  - Camera enable on

• Blynk
 - Create template
![Screenshot 2022-12-21 at 15 42 19](https://user-images.githubusercontent.com/62657957/209017081-c1e28274-f1a5-4554-a6f2-84836ac75100.png)

 -Datastreams setting - Virtual Pin
![Screenshot 2022-12-21 at 15 49 50](https://user-images.githubusercontent.com/62657957/209016904-0e57990b-ace3-466c-9605-75c96a4e37f0.png)
![Screenshot 2022-12-21 at 15 45 00](https://user-images.githubusercontent.com/62657957/209016854-320c52f3-fc65-4815-bdda-4ac062c91792.png)

 - Create Events
![Screenshot 2022-12-21 at 15 45 18](https://user-images.githubusercontent.com/62657957/209016745-2347bff6-0384-49d4-b714-6ace0b2b6e52.png)
![Screenshot 2022-12-21 at 15 45 25](https://user-images.githubusercontent.com/62657957/209016785-81237ce4-ab17-40c2-bfee-86f66c95ff5c.png)
![Screenshot 2022-12-21 at 15 45 09](https://user-images.githubusercontent.com/62657957/209016556-e3d23ee9-9056-45c2-a893-c7f257fc02a6.png)

 - Web dashboad set up (Youtube URL added on Video widget, Datastream setting on Gauge and chart)
![Screenshot 2022-12-21 at 16 03 22](https://user-images.githubusercontent.com/62657957/209016407-e2d938e1-beb3-478e-acf8-62f1bea6d2f8.png)
![Screenshot 2022-12-21 at 16 05 02](https://user-images.githubusercontent.com/62657957/209016288-b81ce3cb-8b5f-405c-a126-c229bd045069.png)
![Screenshot 2022-12-21 at 16 05 13](https://user-images.githubusercontent.com/62657957/209015912-3157addb-cefd-4a1d-8786-843902d0fbd5.png)
![Screenshot 2022-12-21 at 16 05 02](https://user-images.githubusercontent.com/62657957/209015923-fe7920ea-7422-444f-999a-92e1d832399e.png)

 - download mobile app and set up widget
![Screenshot_20221221-160028](https://user-images.githubusercontent.com/62657957/209016028-c4d56f8c-6867-4c63-82bc-ca480aee31d6.png)
![Screenshot_20221221-160042](https://user-images.githubusercontent.com/62657957/209016101-199a5adf-23bc-446f-9bd7-f276de59f78c.png)


• Youtube (Live streaming)

 - Request access to live stream on Youtube Studio
 - Create Live schedule and get stream key
 - install FFmpeg on Raspberry pi

• Firebase
 - install firebase tool to Raspberry pi
 - Create project on Firebase console
 ![Screenshot 2022-12-21 at 16 20 13](https://user-images.githubusercontent.com/62657957/209015707-ad96432a-11a2-4aa5-845b-87b41ce09252.png)


# **Overview**

**temp_humid.py:**

To Run type in the command: python3 temp_humid.py

(1) Get temperature and humidity with Sense Hat and communicate with Blynk.

(2) If the temperature is above or below the set temperature, send a logEvent request with a code of either temp_too_high or temp_too_low to the Blynk server. Similarly, if the humidity is above or below the configured humidity, it will send a logEvent request with either the code humidity_too_high or humidity_too_low to the Blynk server. This will notify you via popup and email in the Blynk application.

**schedule_pi.py:**

To Run type in the command: python3 schedule_pi.py

It schedules light lighting and light color switch schedule, feeding time alarm, and image capture.

(1) The LED light of the sense hat is set with the python schedule library that it lights up in red or green at a set time.
(2) Capture an image at a set time and automatically save it to Firebase storage using the storeFileFB.py function. During image capture, turn off the lights (there is a white setting if it's dark) and save a color correct photo for color recognition.
(3) Send an HTTP GET request to the URL and send a log event to the API endpoint using Python's requests library to notify the feeding time of water etc. Blynk's Event settings will send push notifications and emails.

**storeFileFB.py**

Upload files to Google Cloud Storage and push filenames to Realtime Database

**streaming.py**

To Run type in the command: python3 streaming.py

Using Python's subprocess module to run the streaming.sh script

**streaming.sh**

A script that uses ffmpeg commands to start YouTube Live streaming.
If don't use streaming.py, able to run with ./streaming.sh

**Web hosting**

firebase-hosting: https://plant-factory-d18f0.web.app/
glitch: https://plant-factory-project.glitch.me/

Use Firebase's Realtime Database and Cloud Storage to get the URL of the latest image and display it


![Project Diagram 1](https://user-images.githubusercontent.com/62657957/208902142-462367e2-2f95-464f-8d08-ee4d7120a22b.png)


