# Python Video Processing
##Step 1
###Using *FFMPEG* to Convert Video to Images

In order to work on video in Python, you must first convert your video file into a series of image files. Each image will be a single frame of the video. We will use *FFMPEG* to do this.

*FFMPEG* is a powerful and versatile command line tool for manipulating and converting video files. This can include transcoding, re-packaging video (i.e. mov -> mkv), and breaking video into frames.

An important thing to keep in mind is most video codecs do not store video as a series of frames. Depending on the type of compression used ([This](https://docs.cycling74.com/max5/tutorials/jit-tut/jitterappendixa.html) tutorial is fairly helpful for understanding the basics of video compression) the video information can be stored in a couple of different ways.

Fortunatelly, *FFMPEG* abstracts away most of the hard work for breaking a video file into frames.

In terminal navigate to the folder containing your video file and type:

```bash
ffmpeg -i SunsetWavesCloseUpH264.mp4 -r 30 -f image2 /image-%0d.png
```





##Step 2
###Using Python to Manupulate Images
```python
s = "Python syntax highlighting"
print s
```