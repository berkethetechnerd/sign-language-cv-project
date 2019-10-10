import pysrt
import argparse

# Set command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required = True, help = "Input subtitle file.")
ap.add_argument('-s', '--shift', required = True, help = "Shift amount in seconds.")
ap.add_argument('-o', '--output', required = True, help = "Output subtitle path.")

# Get terminal args, parse it
args = vars(ap.parse_args())
input_file = args['file']
output_file = args['output']
sub_shift = (-1) * int(args['shift'])

# Read file
subs = pysrt.open(input_file, encoding='iso-8859-1')

# Make shift
subs.shift(seconds=sub_shift)

# Save file
subs.save(output_file, encoding='iso-8859-1')
