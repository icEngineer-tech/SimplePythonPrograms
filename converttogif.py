# -*- coding: utf-8 -*-
"""convertToGIF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ivcaz9t6hlO76SvBUA2W5zQORNJFGGNv
"""

from moviepy.editor import VideoFileClip

clp=VideoFileClip('yourVideoHere.mp4')
clp.write_gif('myvideo.gif')