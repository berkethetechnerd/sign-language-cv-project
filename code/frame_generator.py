import cv2
import sys
import os
import shutil

# Parse the arguments
fileName = sys.argv[1]
startSec = float(sys.argv[2])
endSec = float(sys.argv[3])

# Define the output directory
output_dir = './output_' + str(startSec) + '_' + str(endSec) + '/'

# Clear if the output directory exists
if os.path.exists(output_dir):
    shutil.rmtree(output_dir, ignore_errors = True)

# Create the output directory
os.mkdir(output_dir)

# Open the Video file and define the fps
cap = cv2.VideoCapture(fileName)
fps = float(cap.get(cv2.CAP_PROP_FPS))

# Set the counter limits
frameCount = int(fps * startSec)
frameEnd = int(fps * endSec) - 1

# Set the cap with the starting frame
cap.set(cv2.CAP_PROP_POS_FRAMES, frameCount)

# Process the frames
while(cap.isOpened()):
    # Read the next frame
    ret, frame = cap.read()
    
    # Exit if no frame left
    if ret == False:
        break
    
    # Write the frame into disk
    cv2.imwrite(output_dir + 'frame' + str(frameCount) + '.jpg', frame)
    
    # Exit if limit is reached, increase frameCount otherwise
    if frameCount == frameEnd:
    	break
    else:
        frameCount = frameCount + 1

# Release the video, clean the memory.
cap.release()
cv2.destroyAllWindows()
