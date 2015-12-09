# Python Video Processing
##Step 2
###Basic Image Processing in Python

Once the video is split up the video (see [Part 1](https://github.com/sabjorn/PythonVideoTutorial/blob/master/tutorial/Part1-SplitVideo.md)) the individual frames can be imported into Python using [PILLOW](https://python-pillow.github.io/) and [Numpy](http://www.numpy.org/).

*PILLOW* is a fork of a library called PIL. It abstacts the difficult parts of importing images into Python.

*Numpy* adds *C* like arrays into Python. It is also incredibly efficient because it is actually written in C and accessed through Python. Numpy also includes a tonne of functions for efficiently manipulating these arrays (e.g. np.dot, np.fft).

To start off, import Numpy and PILLOW:
```python
import numpy as np
from PIL import Image
```

Next PILLOW is used to open an image. In this example the first image will be opened:
```python
temp_image = Image.open("image-0.png")
```

Then, this image is converted into a Numpy array:
```python
image_array = np.asarray(temp_image)
```