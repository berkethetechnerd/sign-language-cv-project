'''
@Params: one json file and the corresponding image file

TO RUN
command: python blur_detection.py -j <json_file_path> -i <image_file_path>

OUTPUT: print Left blur or not and Right blur or not and their rate
'''
import json
import sys
import cv2
import numpy as np
import math
import os
import argparse

class Point(object):
    def __init__(self, x, y, c):
        self.x=x     # x_coordinate of the point
        self.y=y     # y_coordinate of the point
        self.c=c     # confidence of the point

    def __repr__(self):
        return 'x: '+str(self.x)+", y: "+str(self.y)+", c: "+str(self.c)

# Set command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-j', '--json', required = True, help = "Input json files.")
ap.add_argument('-i', '--image', required = True, help = "Input image files.")

args = vars(ap.parse_args())
json_dir = args['json']
img_dir = args['image']

with open(json_dir) as f:
    data = json.loads(f.read())

person = data['people'][0]
left_hand = person['hand_left_keypoints_2d']
right_hand = person['hand_right_keypoints_2d']


########## EXTRACT LEFT HAND POINTS  ##########
i = 0
lhand_points = []
for i in range(0, len(left_hand), 3):
    temp = Point(left_hand[i],left_hand[i+1],left_hand[i+2])
    lhand_points.append(temp)    # add this point to pose point array
    i+=3


########## EXTRACT RIGHT HAND POINTS  ##########
i = 0
rhand_points = []
for i in range(0, len(right_hand), 3):
    temp = Point(right_hand[i],right_hand[i+1],right_hand[i+2])
    rhand_points.append(temp)    # add this point to pose point array
    i+=3


#######    BLUR DETECTION   #########

# import the necessary packages
from imutils import paths
import argparse
import cv2
 
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

rcenter = rhand_points[9]
lcenter = lhand_points[9]

ry = int(rcenter.y)
rx = int(rcenter.x)
ly = int(lcenter.y)
lx = int(lcenter.x)
h=50
w=50


# crop left and right hand
image = cv2.imread(img_dir)
crop_img_right = image[ry-h:ry+h, rx-w:rx+w]
crop_img_left = image[ly-h:ly+h, lx-w:lx+w]
#cv2.imwrite("Right.png", crop_img_right)
#cv2.imwrite("Left.png", crop_img_left)

gray = cv2.cvtColor(crop_img_right, cv2.COLOR_BGR2GRAY)

fm = variance_of_laplacian(gray)
Rtext = "Right Not Blurry: "+ str(fm)[0:6]

# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
if fm < 1000:
    Rtext = "Right Blurry: "+ str(fm)[0:6]

gray = cv2.cvtColor(crop_img_left, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
Ltext = "Left Not Blurry: "+str(fm)[0:6]

# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
if fm < 1000:
    Ltext = "Left Blurry: "+ str(fm)[0:6]

'''
# show the image
cv2.rectangle(image, (rx-w,ry-h),(rx+w,ry+h), red, 3)
cv2.rectangle(image, (lx-w,ly-h),(lx+w,ly+h), red, 3)

cv2.putText(image, Rtext, (120,40), font, 1, red)
cv2.putText(image, Ltext, (600,40), font, 1, red)

cv2.imwrite("result.png",image)
'''
print("Left: "+Ltext+", Right: "+Rtext)
key = cv2.waitKey(0)
