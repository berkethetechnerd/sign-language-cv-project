'''
@Params: directory of json files and directory of corresponding frames. Make sure that json files has name like <number>.json
        for example: 897.json and the corresponding image file has name frame_897.jpg

TO RUN
command: python classify_data_by_angle.py -j <json_files_directory> -f <frames_directory>

OUTPUT: two directory: one for up images and the other is for down images
'''

import json
import sys
import cv2
import numpy as np
import math
import os, sys, shutil
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
ap.add_argument('-f', '--frame', required = True, help = "Input frame files.")

args = vars(ap.parse_args())
jsons_dir = args['json']+'/'
frames_dir = args['frame']+'/'

output_dir_up = './output_up/'
output_dir_down = './output_down/'

# Clear if the output directory exists
if os.path.exists(output_dir_up):
    shutil.rmtree(output_dir_up, ignore_errors = True)

if os.path.exists(output_dir_down):
    shutil.rmtree(output_dir_down, ignore_errors = True)

# Create the output directory
os.mkdir(output_dir_up)
os.mkdir(output_dir_down)

for json_file in os.listdir(jsons_dir):

    json_no = str(int(json_file.split('_')[2]))
    with open(jsons_dir+json_file) as f:
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

    is_left_null = False
    is_right_null = False

    # CALCULATE LEFT ARM ANGLE
    lengt_one = (math.pow(pose_points[5].x-pose_points[6].x,2)+math.pow(pose_points[5].y-pose_points[6].y,2))
    lengt_two = (math.pow(pose_points[6].x-pose_points[7].x,2)+math.pow(pose_points[6].y-pose_points[7].y,2))
    lengt_three = (math.pow(pose_points[5].x-pose_points[7].x,2)+math.pow(pose_points[5].y-pose_points[7].y,2))

    if (-2*math.sqrt(lengt_one)*math.sqrt(lengt_two)) == 0:
        continue
    
    LQ = math.acos((lengt_three - lengt_one -lengt_two)/(-2*math.sqrt(lengt_one)*math.sqrt(lengt_two)))
    LQ = (LQ*180/math.pi)

    # CALCULATE RIGHT ARM ANGLE
    lengt_one = (math.pow(pose_points[2].x-pose_points[3].x,2)+math.pow(pose_points[2].y-pose_points[3].y,2))
    lengt_two = (math.pow(pose_points[3].x-pose_points[4].x,2)+math.pow(pose_points[3].y-pose_points[4].y,2))
    lengt_three = (math.pow(pose_points[2].x-pose_points[4].x,2)+math.pow(pose_points[2].y-pose_points[4].y,2))

    RQ = math.acos((lengt_three - lengt_one -lengt_two)/(-2*math.sqrt(lengt_one)*math.sqrt(lengt_two)))
    RQ = (RQ*180/math.pi)

    if pose_points[4].x == 0 and pose_points[4].y == 0 and pose_points[4].c == 0:
        is_right_null = True
    
    if pose_points[7].x == 0 and pose_points[7].y == 0 and pose_points[7].c == 0:
        is_left_null = True

    print(json_no)

    #DOWN
    if (is_right_null and is_left_null) or (is_left_null and RQ > 100) or (is_right_null and LQ > 100) or (LQ > 100 and RQ > 100):
        shutil.copy(frames_dir+"frame_"+json_no+".jpg", output_dir_down, follow_symlinks=True)

    #UP
    else: 
        shutil.copy(frames_dir+"frame_"+json_no+".jpg", output_dir_up, follow_symlinks=True)

key = cv2.waitKey(0)
