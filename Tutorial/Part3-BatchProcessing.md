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

Next, 

####[Next Step](https://github.com/sabjorn/PythonVideoTutorial/blob/master/Tutorial): Batch Importing and Processing of Images