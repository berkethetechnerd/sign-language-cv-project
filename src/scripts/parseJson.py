import json
import sys
import cv2
import numpy as np
import math
class Point(object):
    def __init__(self, x, y, c):
        self.x=x     # x_coordinate of the point
        self.y=y     # y_coordinate of the point
        self.c=c     # confidence of the point

    def __repr__(self):
        return 'x: '+str(self.x)+", y: "+str(self.y)+", c: "+str(self.c)


file_no = sys.argv[1]

with open("./../data/output/"+file_no+".json") as f:
    data = json.loads(f.read())

person = data['people'][0]
pose= person['pose_keypoints_2d']
face = person['face_keypoints_2d']
left_hand = person['hand_left_keypoints_2d']
right_hand = person['hand_right_keypoints_2d']


########## EXTRACT POSE POINTS  ##########
i = 0
pose_points = []
for i in range(0, len(pose), 3):
    temp = Point(pose[i],pose[i+1],pose[i+2])
    pose_points.append(temp)    # add this point to pose point array

########## EXTRACT FACE POINTS  ##########
i = 0
face_points = []
for i in range(0, len(face), 3):
    temp = Point(face[i],face[i+1],face[i+2])
    face_points.append(temp)    # add this point to pose point array
    i+=3


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


w=40
h=20
red = [0,0,255]
white = [255,255,255]
i=0
image = cv2.imread('./berkarak/frame'+file_no+".jpg")
font = cv2.FONT_HERSHEY_PLAIN
"""
for point in pose_points:
    if point.c > 0.5:
        cv2.circle(image, ((int(point.x), int(point.y))), 5, red, -1)
        cv2.putText(image, str(i), (int(point.x)+10, int(point.y)), font, 1, white)
    i+=1

lengt_one = (math.pow(pose_points[5].x-pose_points[6].x,2)+math.pow(pose_points[5].y-pose_points[6].y,2))
lengt_two = (math.pow(pose_points[6].x-pose_points[7].x,2)+math.pow(pose_points[6].y-pose_points[7].y,2))
lengt_three = (math.pow(pose_points[5].x-pose_points[7].x,2)+math.pow(pose_points[5].y-pose_points[7].y,2))

LQ = math.acos((lengt_three - lengt_one -lengt_two)/(-2*math.sqrt(lengt_one)*math.sqrt(lengt_two)))
LQ = (LQ*180/math.pi)

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(image, "L. Angle: "+str(LQ)[0:5], (120,40), font, 1, red)

lengt_one = (math.pow(pose_points[2].x-pose_points[3].x,2)+math.pow(pose_points[2].y-pose_points[3].y,2))
lengt_two = (math.pow(pose_points[3].x-pose_points[4].x,2)+math.pow(pose_points[3].y-pose_points[4].y,2))
lengt_three = (math.pow(pose_points[2].x-pose_points[4].x,2)+math.pow(pose_points[2].y-pose_points[4].y,2))

RQ = math.acos((lengt_three - lengt_one -lengt_two)/(-2*math.sqrt(lengt_one)*math.sqrt(lengt_two)))
RQ = (RQ*180/math.pi)

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(image, "R. Angle: "+str(RQ)[0:5], (120,80), font, 1, red)

if LQ > 100 and RQ > 100:
    cv2.putText(image, "DOWN", (650,40), font, 1, red)
else: 
    cv2.putText(image, "UP", (650,40), font, 1, red)


cv2.imwrite("result.png",image)

"""

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

crop_img_right = image[ry-h:ry+h, rx-w:rx+w]
crop_img_left = image[ly-h:ly+h, lx-w:lx+w]
cv2.imwrite("Right.png", crop_img_right)
cv2.imwrite("Left.png", crop_img_left)


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


# show the image
cv2.rectangle(image, (rx-w,ry-h),(rx+w,ry+h), red, 3)
cv2.rectangle(image, (lx-w,ly-h),(lx+w,ly+h), red, 3)

cv2.putText(image, Rtext, (120,40), font, 1, red)
cv2.putText(image, Ltext, (600,40), font, 1, red)

cv2.imwrite("result.png",image)

key = cv2.waitKey(0)
