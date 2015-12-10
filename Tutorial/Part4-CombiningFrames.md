# Python Video Processing
##Step 4
###Putting the Frames Back Together

This is the final step for a simple video processing application. FFMPEG is used to put the processed images back into a movie format.

Open Terminal and input:

```bash
ffmpeg -framerate 30 -i processed_image-%0d.png -pix_fmt yuv420p -c:v libx264\ 
		-preset slow -crf 20 -r 30 ./filename.mov
```

Keep in 
The basic

touch sjkljklajsklfjklasjflkjsa\
tjkjskjdskjkfjs.wav