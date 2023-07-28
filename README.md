# photo-slideshow-generator

Python script that takes a folder containing photos as input, creates a video from those photos, and saves the resulting video file in either .mp4 or .avi format. The script uses the MoviePy library to achieve this functionality. Let me explain the code step by step:

1. The script imports necessary modules: ImageSequenceClip from moviepy.editor for creating the video and os for file operations.

2. It defines a function called create_video_from_photos, which takes the photo_folder (path to the folder containing photos), output_file (path to the output video file), and fps (frames per second for the video) as input arguments.

3. The function reads all files in the photo_folder and sorts them in alphanumeric order.

4. It creates a list called image_paths, which contains the full paths to each image in the folder.

5. Using ImageSequenceClip, the function creates a video from the list of image paths with the specified fps.

6. The script determines the output video format based on the file extension of output_file. If it's ".mp4", the output format will be "libx264", and if it's ".avi", the output format will be "mpeg4". If the file extension is not supported, it raises a ValueError.

7. Finally, the video is written to the output_file with the chosen output format and specified fps.

8. After the video is created, the script prints the location where the video is saved.

9. The script then waits for the user to press enter before closing the console.

10. The script demonstrates example usage by taking the photo_folder path and desired fps from the user and saving the video with the name "video.mp4" in the photo_folder.

Note: Before running this code, you'll need to have the MoviePy library installed. If you don't have it, you can install it using the following command: pip install moviepy

After installing MoviePy, you can run the script and follow the prompts to create a video from your photos.

