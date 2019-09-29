import cv2
import sys
import os
import shutil

# Parse the arguments
fileName = sys.argv[1]
startSec = float(sys.argv[2])
endSec = float(sys.argv[3])
fpsSec = int(sys.argv[4])

# Define the output directory
output_dir = './output_' + str(startSec) + '_' + str(endSec) + '_' + str(fpsSec) + 'fps/'

# Clear if the output directory exists
if os.path.exists(output_dir):
    shutil.rmtree(output_dir, ignore_errors = True)

# Create the output directory
os.mkdir(output_dir)

# Open the Video file and define the fps
cap = cv2.VideoCapture(fileName)
fpsOfVideo = float(cap.get(cv2.CAP_PROP_FPS))

# Set the counter limits
frameCount = int(fpsOfVideo * startSec)
frameEnd = int(fpsOfVideo * endSec) - 1

# Set the cap with the starting frame
cap.set(cv2.CAP_PROP_POS_FRAMES, frameCount)

# Determine frame length
fpsCount = int(fpsOfVideo / fpsSec)
i = 0

# Process the frames
while(cap.isOpened()):
    # Read the next frame
    ret, frame = cap.read()
    
    # Exit if no frame left
    if ret == False:
        break
    
    # Write the frame into disk
    if (i == fpsCount):
        cv2.imwrite(output_dir + 'frame' + str(frameCount) + '.jpg', frame)
        i = 0
    else:
        i = i + 1
    
    # Exit if limit is reached, increase frameCount otherwise
    if frameCount == frameEnd:
    	break
    else:
        frameCount = frameCount + 1

# Release the video, clean the memory.
cap.release()
cv2.destroyAllWindows()
