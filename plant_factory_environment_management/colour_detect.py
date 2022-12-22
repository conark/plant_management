#!/usr/bin/env python3
import os
from PIL import Image
import numpy as np
import requests
import os
from dotenv import load_dotenv

# load .env　file
load_dotenv()


image_dir = 'image/'
files = sorted(os.listdir(image_dir), key=lambda x: os.path.getctime(os.path.join(image_dir, x)))
latest_file = files[-1]
print(latest_file)

# Open image and ensure RGB
im = Image.open('image/'+latest_file).convert('RGB')
print (im)
# for specific photo
# im = Image.open('image/TomatoY.jpg').convert('RGB')

# Make into Numpy array
na = np.array(im)

# Get colours and corresponding counts
colours, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=1)

# Filter out colours that are not red
red_colours = colours[(colours[:,0] == 255) & (colours[:,1] <= 79) & (colours[:,2] <= 71)]
red_counts = counts[(colours[:,0] == 255) & (colours[:,1] <= 79) & (colours[:,2] <= 71)]

# Print the number of red pixels
print (red_colours)
print (red_counts)
print(red_counts.sum())

if red_counts.sum() >= 1:
    print ("found red")
    requests.get("https://blynk.cloud/external/api/logEvent?token="+(os.environ['BLYNK_AUTH'])+"&code=harvest_info")
else :
    print ("no detected")

