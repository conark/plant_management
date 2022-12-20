#!/bin/bash

# ./.env Read the env file so that it can be referenced as a variable
source ./.env


NUM=`ps aux | grep ffmpeg | grep -v grep | wc -l`
if [ $NUM -gt 0 ]; then
        echo "Already running."
        exit
fi

ffmpeg \
        -f alsa -thread_queue_size 8192 \
        -i plughw:1 -f v4l2 \
        -thread_queue_size 8192 \
        -input_format yuyv422 -video_size 640x480 \
        -framerate 30 -i /dev/video0 \
        -vsync 1 -g 16 \
        -c:a aac -b:a 128k -ar 44100 -af "volume=5dB" \
        -f flv rtmp://a.rtmp.youtube.com/live2/${YOUTUBE}
        