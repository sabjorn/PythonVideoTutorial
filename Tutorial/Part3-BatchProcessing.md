# Python Video Processing
##Step 3
###Batch Processing

Now that basic input/output and processing is accomplished, the final step for processing video is to go through every frame produced in [Part 1](https://github.com/sabjorn/PythonVideoTutorial/blob/master/tutorial/Part1-SplitVideo.md) and process these images. This batch processing is relatively straightforward.


The code for this section is available in [../ExampleCode/](https://github.com/sabjorn/PythonVideoTutorial/blob/master/tutorial/Part2-BasicImageProcessing.md)

The first step for processing large number of images is to calculate the number of images that Python will be processing. This will be saved as a variable and allow the script to loop from the first to last frame in sequence.

the `glob` module will be used to assist with finding the number of files in the target directory:
```python
import glob
```

Next, glob is used to create a list of all the files in the directory:

```python
filelocation = "/pathToImage/image-*.png" #a variable for pointing to the files
files = glob.glob(filelocation)
```

Using `image-*.png` will select every file in the directory with `image-` and `.png` since the `*` is a wildcard and is replaced by every number of file.

Next, the number of files is calculated to be looped through later:

```python
count = len(files) #creates a variable with the number of files
```

Finally, a `for loop` is used to open, process, and save every image. The loop with be nearly identical to the steps in [Part 2](https://github.com/sabjorn/PythonVideoTutorial/blob/master/Tutorial/Part2-BasicImageProcessing.md).

```python
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
```

In essence, by having the `for loop` count from `1` (the first integer value of our images) to `count` (the last integer value of our series of images), each frame can be opened, processed and output.

**Note**: `range(n,m)` will list values from `n` to `n-1`, this is why it is necessary to have `count+1` or else it will miss the last frame.

There are many ways to improve the above code for ease of use and efficiency. First, variables can be used to store the filepath information. Second, `array_copy` is created every loop. This is usually unnecessary and with a bit of work a buffer can be made outside of the *for loop* and continuously reused.

####[Next Step](https://github.com/sabjorn/PythonVideoTutorial/blob/master/Tutorial/Part3-BatchProcessing.md): Putting the Frames Back Together