from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import argparse

# Set command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required = True, help = "Input video file.")
ap.add_argument('-s', '--start', required = True, help = "Start time")
ap.add_argument('-e', '--end', required = True, help = "End time")

# Get terminal args, parse it
args = vars(ap.parse_args())
file = args['file']
start_time = int(args['start'])
end_time = int(args['end'])

output_file = "cut_" + str(start_time) + "_" + str(end_time) + ".mp4"

ffmpeg_extract_subclip(file, start_time, end_time, targetname=output_file)
