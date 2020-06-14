# based on example code from the ffmpeg-python git repo
# https://github.com/kkroening/ffmpeg-python/blob/master/examples/tensorflow_stream.py

import argparse
import ffmpeg
import logging
import numpy as np
import os
import subprocess
from imagefilter import imagefilter


parser = argparse.ArgumentParser(description='Example streaming ffmpeg numpy processing')
parser.add_argument('in_filename', help='Input filename')
parser.add_argument('out_filename', help='Output filename')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_video_info(filename):
    logger.info('Getting video size for {!r}'.format(filename))
    probe = ffmpeg.probe(filename)
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    
    width = int(video_info['width'])
    height = int(video_info['height'])
    
    framerate = video_info['r_frame_rate'].split("/")
    framerate = float(framerate[0])/float(framerate[1])

    return width, height, framerate


def start_ffmpeg_process1(in_filename):
    logger.info('Starting ffmpeg process1')
    args = (
        ffmpeg
        .input(in_filename)
        .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        .compile()
    )
    return subprocess.Popen(args, stdout=subprocess.PIPE)


def start_ffmpeg_process2(out_filename, width, height, framerate):
    logger.info('Starting ffmpeg process2')
    args = (
        ffmpeg
        .input('pipe:', format='rawvideo', pix_fmt='rgb24', framerate='{}'.format(framerate), s='{}x{}'.format(width, height))
        .output(out_filename, pix_fmt='yuv420p')
        .overwrite_output()
        .compile()
    )
    return subprocess.Popen(args, stdin=subprocess.PIPE)


def read_frame(process1, width, height):
    logger.debug('Reading frame')

    # Note: RGB24 == 3 bytes per pixel.
    frame_size = width * height * 3
    in_bytes = process1.stdout.read(frame_size)
    if len(in_bytes) == 0:
        frame = None
    else:
        assert len(in_bytes) == frame_size
        frame = (
            np
            .frombuffer(in_bytes, np.uint8)
            .reshape([height, width, 3])
        )
    return frame


def process_frame_simple(frame):
    '''Simple processing example: darken frame.'''
    return frame * 0.3


def write_frame(process2, frame):
    logger.debug('Writing frame')
    process2.stdin.write(
        frame
        .astype(np.uint8)
        .tobytes()
    )


def run(in_filename, out_filename, imagefilter):
    width, height, framerate = get_video_info(in_filename)
    process1 = start_ffmpeg_process1(in_filename)
    process2 = start_ffmpeg_process2(out_filename, width, height, framerate)

    coefficient = .3 # [0,1]
    frame_delay = read_frame(process1, width, height)
    while True:
        in_frame = read_frame(process1, width, height)

        if in_frame is None:
            logger.info('End of input stream')
            break

        logger.debug('Processing frame')
        out_frame = np.copy(in_frame)
        out_frame = (in_frame * coefficient) + (frame_delay * (1 - coefficient))
        frame_delay = np.copy(in_frame)
        
        # out_frame = imagefilter(in_frame)
        

        write_frame(process2, out_frame)

    logger.info('Waiting for ffmpeg process1')
    process1.wait()

    logger.info('Waiting for ffmpeg process2')
    process2.stdin.close()
    process2.wait()

    logger.info('Done')


if __name__ == '__main__':
    args = parser.parse_args()
    run(args.in_filename, args.out_filename, imagefilter)
