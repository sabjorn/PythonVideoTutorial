#Example code used to batch process images.
#Step by step is available here: 
#https://github.com/sabjorn/PythonVideoTutorial/blob/master/Tutorial/Part3-BatchProcessing.md

import numpy as np
from PIL import Image
import glob

files = glob.glob("/pathToImage/image-*.png")

count = len(files) #creates a variable with the number of files

for i in range(1,count+1):
	#open image
	temp_image = Image.open("/pathToImage/image-"+str(i)+".png")
	image_array = np.asarray(temp_image)

	#make buffer
	array_copy = np.copy(image_array)

	#do some processing here

	#convert array back to image and save
	output_image = Image.fromarray(np.uint8(array_copy))
	output_image.save("/pathToImage/processed_image-"+str(i)+".png")
