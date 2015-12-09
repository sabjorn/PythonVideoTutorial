# Python Video Processing
##Step 2
###Basic Image Processing in Python

Once the video is split up the video (see [Part 1](https://github.com/sabjorn/PythonVideoTutorial/blob/master/tutorial/Part1-SplitVideo.md)) the individual frames can be imported into Python using [PILLOW](https://python-pillow.github.io/) and [Numpy](http://www.numpy.org/).

* *PILLOW* is a fork of a library called PIL. It abstracts the difficult parts of importing images into Python.

* *Numpy* adds *C* like arrays into Python. It is also incredibly efficient because it is actually written in C and accessed through Python. Numpy also includes a tonne of functions for efficiently manipulating these arrays (e.g. np.dot, np.fft).

Here is an example input video frame:

![First Frame - Before Processing](https://github.com/sabjorn/PythonVideoTutorial/blob/master/ExampleImages/image-1.png)

To start off, import Numpy and PILLOW:
```python
import numpy as np
from PIL import Image
```

Next PILLOW is used to open an image. In this example the first image from the video frames will be opened:
```python
temp_image = Image.open("image-1.png")
```

Then, this image is converted into a Numpy array:
```python
image_array = np.asarray(temp_image)
```

Generally, this Numpy array will be of the shape [x, y, 3] where *x* is the number of pixels in the *x dimension*, *y* is the number of pixels in the *y dimension* and *3* is the number of colour layers. For the most part, any image you'll be processing will be made up of 3 layers: **R**ed, **G**reen, and **B**lue. Also, generally, the value of each of these colour pixels will be between [0, 255] inclusive. This constitutes the *RGB* colour space and through mixtures of these three colours a vast amount of different colours can be produced (256^3).

As a trivial example, to access the pixel in the Red layer at `x = 10` and `y = 100`, `image_array[10,100,0]`.

It's important to note this is not necessarily how most video formats store colour (because it's not too efficient) but RGB colour space is easy to work with and FFMPEG will take care of conversion in the final step. For more information about how CODECS and colour spaces work I highly recommend [this](http://xiph.org/video/vid1.shtml) video.

Next, some processing is done. For this example, a trivial process of swapping the different colour layers around:

Then, this image is converted into a Numpy array:
```python
# image_array is read-only so make a copy
# This also acts as a buffer for swapping pixel layers pixel layers
array_copy = np.copy(image_array)

#Replace Red layer with Green layer
array_copy[:,:,0] = image_array[:,:,1]

#Replace Green layer with Blue layer
array_copy[:,:,1] = image_array[:,:,2]

#Replace Blue layer with Red layer
array_copy[:,:,2] = image_array[:,:,0]
```

Notice the *:* in the square brackets. With Numpy this basically means 'Take all the values in this dimension'. Another use is like this: `somearray[10:]` This will use the values from index 10 to the end of the array.

Now that some processing is done, the processed image array needs to be turned back into an image and saved.

```python
output_image = Image.fromarray(np.uint8(array_copy)) #convert back to PIL Image
output_image.save("processed_image-1.png")
```

Here is the post-processed video frame:

![First Frame - After Processing](https://github.com/sabjorn/PythonVideoTutorial/blob/master/ExampleImages/processed_image-1.png)

This last step is easy but a little confusing:

`np.uint8()` takes an array and casts it into a specific type. Because RGB colour space uses values between [0,255], the array is cast as a *uint8* datatype (which is a byte of only positive values ranging from 0 - 255). This step is really only necessary if the processing step pushes the image array outside of this range (otherwise an error occurs)

`Image.fromarray()` takes the Numpy image array and turns it back into a PILLOW Image. This image is stored as a variable called *output_image*.

Finally, `output_image.save()` will take a PILLOW Image and save it to a file.

####[Next Step](https://github.com/sabjorn/PythonVideoTutorial/blob/master/tutorial): Batch Importing and Processing of Images