"""
CatPlay
Version 1.0
Jigar Hira
June 2019
"""


import subprocess

# get video stream from camera
def get_video():
    ffmpeg_command = ['ffmpeg',
                      '-f', 'dshow',
                      '-i', 'video=Integrated Webcam',
                      '-f', 'h264',
                      'pipe:']
    ffmpeg = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE)
    return ffmpeg.stdout



















# Unit test
if __name__ == '__main__':
    get_video()

# EOF