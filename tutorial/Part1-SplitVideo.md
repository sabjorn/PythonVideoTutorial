# Python Video Processing
##Step 1
###Using *FFMPEG* to Convert Video to Images

In order to work on video in Python, you must first convert your video file into a series of image files. Each image will be a single frame of the video. We will use *FFMPEG* to do this.

*FFMPEG* is a powerful and versatile command line tool for manipulating and converting video files. This can include transcoding, re-packaging video (i.e. mov -> mkv), and breaking video into frames.

An important thing to keep in mind is most video codecs do not store video as a series of frames. Depending on the type of compression used ([This](https://docs.cycling74.com/max5/tutorials/jit-tut/jitterappendixa.html) tutorial is fairly helpful for understanding the basics of video compression) the video information can be stored in a couple of different ways.

Fortunatelly, *FFMPEG* abstracts away most of the hard work for breaking a video file into frames.

In terminal navigate to the folder containing your video file and type:

```bash
ffmpeg -i SunsetWavesCloseUpH264.mp4 -r 30 -f image2 image-%0d.png
```

The above command does a couple things:

* `-i SunsetWavesCloseUpH264.mp4` selects sets the input (-i) file to SunsetWavesCloseUpH264.mp4

* `-r 30` sets the frame rate to 30 frames/second. It is best to match this with the frame rate of your video file (FFMPEG may do this automatically without the -r or it might just set it to some preset value). This value also tells you how many frames you'll end up with at the end of this process (30frames/s * length of video (in seconds)).

* `-f image2 image-%0d.png` sets the output files to be a sequence of images with the prefix `image-` followed by a sequence of digits. `%0d` sets the sequence of number to be without any leading zeros. Alternatively, you can set it to `%03d` which will make sure the filename always has *at least* 3 numerical digits.

  * For example: 
    * `%0d` will cause the filenames to be: image-0.png, image-1.png, ..., image-n.png (where n is the number of frames contained in the video).
    * `%03 d` will cause the fienames to be: image-000.png, image-001.png, ..., image-n.png.
    * Other image filetypes can be used by changing the file extension (.png -> .jpg). FFMPEG handles making the right files automatically.

**Extra Notes**:
* The filename (image-%0d.png) can really be named anything. e.g. waves-%0d.png, image%0d.png. I do not know the best filetype to use for this process. I'm just partial to .pngs.
* It is probably best to make a folder and have the frames output to this folder (e.g. `-f image2 subfoldername/image-%0d.png) otherwise you'll have a big mess on your hands (i.e. 10,000 frames on your desktop).

###[Next Step](https://github.com/sabjorn/PythonVideoTutorial/blob/master/tutorial/Part2-BasicImageProcessing.md): Importing and Processing Images