# 2DLinearRegressionAnimation
Animation of 2D Linear Regression

This is my first ever git repository upload so I'll work on the README if there is any interest in this particular repo, but I wanted to share a few points I had trouble with while putting this together (this code is inspired by Lesson 2 of Fast AI 2019 part 1).

In order to run this code properly, you must import PyTorch, Matplotlib and NumPy through regular pip or conda installs (message me if you have any questions).

It is very important if you want the animation to download install ffmpeg and to specifically point to the path where your "ffmpeg.exe" is located (see below, but replace 'C:\\ProgramData\\... etc' with your own file directory). 
```
import matplotlib.pyplot as plt
import tensorflow, torch
from matplotlib import animation, rc
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
rc('animation', html='html5')

plt.rcParams['animation.ffmpeg_path'] = 'C:\\ProgramData\\Anaconda3\\pkgs\\ffmpeg-4.2-h6538335_0\\Library\\bin\\ffmpeg.exe'
writer = animation.FFMpegWriter()
```
