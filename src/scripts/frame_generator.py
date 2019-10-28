import os, sys, shutil
import cv2
import time
import argparse

# Set command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required = True, help = "Input video file.")

# Get terminal args, parse it
args = vars(ap.parse_args())
file = args['file']

# Define the output directory
output_dir = './all_frames/'

# Clear if the output directory exists
if os.path.exists(output_dir):
    shutil.rmtree(output_dir, ignore_errors = True)

# Create the output directory
os.mkdir(output_dir)

# Open the video file, retrieve the fps
cap = cv2.VideoCapture(file)
v_fps = cap.get(cv2.CAP_PROP_FPS)
v_fps_total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Print information message on processed video
print("Video length: {0:.2f} seconds".format(v_fps_total / v_fps))
print("Total Frames: {} frames".format(v_fps_total))
print("FPS: {0:.2f} frame/second".format(v_fps))

# Define a variable for counting frames
frameCount = 1

# Start the execution timer
exec_timer = time.time()

# Process the frames
while(cap.isOpened()):
    # Read the next frame
    ret, frame = cap.read()
    
    # Exit if no frame left
    if ret == False:
        break
    
    # Write the frame into disk
    cv2.imwrite(output_dir + 'frame_' + str(frameCount) + '.jpg', frame)
    frameCount += 1
    
# Print success message
exec_timer = time.time() - exec_timer
print("Execution is completed succesfully in {0:.2f} seconds.".format(exec_timer))

# Release the video, clean the memory.
cap.release()
cv2.destroyAllWindows()
