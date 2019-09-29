# Original code from https://github.com/yobibyte/yobiface

# The MIT License (MIT)

# Copyright (c) 2016 yobi byte

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
import tensorflow as tf
import cv2
import argparse

'''
We load data and convert it to BGR,
in order to show pic, we want to convert it back.
'''
def imshow(fig, pic, rows=1, cols=1, pos=1):
  ax = fig.add_subplot(rows,cols,pos)
  ax.axes.get_xaxis().set_visible(False)
  ax.axes.get_yaxis().set_visible(False)
  ax.imshow(cv2.cvtColor(pic,cv2.COLOR_BGR2RGB));

def preproc(im):
  im = cv2.resize(im, (160,160))
  return im.astype(np.float32)/255

def get_random_color():
    return [np.random.random() for i in range(3)]