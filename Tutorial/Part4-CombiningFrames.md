# Python Video Processing
##Step 4
###Putting the Frames Back Together

This is the final step for a simple video processing application. FFMPEG is used to put the processed images back into a movie format.

Open Terminal, navigate to the folder with the processed frames, and input:

```bash
ffmpeg -framerate 30 -i processed_image-%0d.png -pix_fmt yuv420p -c:v libx264 \
-preset slow -crf 20 -r 30 ./processed_video.mov
```

Like the command in [Part 1](https://github.com/sabjorn/PythonVideoTutorial/blob/master/Tutorial/Part1-SplitVideo.md), the above command calls FFMPEG to do the heavy lifting for re-assembling but this time in reverse (taking the frames and putting them into a movie format).

Here's a bit of an analysis of the command:

* `-framerate 30` sets the framerate to 30frames/s. `-r 30` also does this. As far as I can tell, `-r` sets the framerate of the output video while `-framerate` defines how long each input image is kept on screen. If these two values don't match an effect similar to stop motion animation will (likely) happen. Also, apparently order of these two flags is important.

* `-i processed_image-%0d.png` defines the input images which will be used to create the output video.

* `-pix_fmt yuv420p` sets the output video to use [YUV](https://en.wikipedia.org/wiki/YUV) colour space. This is what Apple MOV files use. VLC will play a MOV without this flag set but it doesn't work too well otherwise.

* `-c:v libx264` sets the video codec to [H264](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC). It seems to work well and is a widely used codec.

* `-preset slow` and `-crf 20` are somewhat a mystery. H264 has compression and these two flags adjust the compression values. More info can be found [here](https://trac.ffmpeg.org/wiki/Encode/H.264). Feel free to play with these values.

* `./processed_video.mov` sets the name of the output file. FFMPEG seems to automatically handle different filetypes. So, `.mp4`, `.mkv`, etc should work.

