#Example code used to batch process images.
#Step by step is available here: 
#https://github.com/sabjorn/PythonVideoTutorial/blob/master/Tutorial/Part3-BatchProcessing.md

import os
import numpy as np
from PIL import Image

# create FIFOS and Processes
os.mkfifo("ffmpegOut")
# ffmpeg -i SunsetWavesCloseUpH264.mp4 -r 30 -f image2 pipe:1 > ffmpegOut

os.mkfifo("ffmpegIn")
# ffmpeg -framerate 30 -i ffmpegIn -pix_fmt yuv420p -c:v libx264 -preset slow -crf 20 -r 30 ./processed_video.mov

with open('ffmpegOut', 'r', 0) as inpipe:
    #open image
    temp_image = Image.open(inpipe)
    image_array = np.asarray(temp_image)

    #make buffer
    array_copy = np.copy(image_array)

    #do some processing here

    #convert array back to image and save
    output_image = Image.fromarray(np.uint8(array_copy))
    output_image.save("ffmpegIn", "PNG")
