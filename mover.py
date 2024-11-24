import os
import shutil

# Define the source and destination directories
source_dir = 'C:/Users/timva/Desktop/PhotoStats/SleutelstamFotoArchief'
destination_dir = 'C:/Users/timva/Desktop/PhotoStats/vids'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Define a list of video file extensions
video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']

# Walk through the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Check if the file is a video file
        if any(file.lower().endswith(ext) for ext in video_extensions):
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Move the file to the destination directory
            print(file_path)
            shutil.move(file_path, destination_dir)
            # print(f'Moved: {file_path} to {destination_dir}')