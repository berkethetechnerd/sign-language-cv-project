import shutil
import cv2
import os

frame_input_dir = '/Users/berkeesmer/Desktop/titanik_data/MVI_8191/'
video_output_dir = './output/'

start_index = 664
end_index = 697
repeatfor = 30
font = cv2.FONT_HERSHEY_SIMPLEX

if os.path.exists(video_output_dir):
    shutil.rmtree(video_output_dir, ignore_errors = True)
    
os.mkdir(video_output_dir)

frame_arr = []
for i in range(end_index - start_index + 1):
    frame_index = start_index + i
    frame_file = frame_input_dir + 'frame_' + str(frame_index) + '.jpg'
    frame_read = cv2.imread(frame_file)
    cv2.putText(frame_read, str(frame_index), (30,100), font, 2, (255, 50, 50), 1, cv2.LINE_AA)

    frame_arr.append(frame_read)

height, width, layers = frame_arr[0].shape
fourcc = cv2.VideoWriter_fourcc(*'mpeg')
size = (width, height)
fps = 30.0

video_path = video_output_dir + 'video_' + str(start_index) + '_' + str(end_index) + '.mp4'
cap = cv2.VideoWriter(video_path, fourcc, fps, size)

for i in range(len(frame_arr)):
    for j in range(repeatfor):
        cap.write(frame_arr[i])

cap.release()   

