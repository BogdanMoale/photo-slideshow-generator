from moviepy.editor import ImageSequenceClip
import os

def create_video_from_photos(photo_folder, output_file, fps=24):
    # Get all files in the photo folder
    files = os.listdir(photo_folder)
    # Sort files in alphanumeric order
    files.sort()

    # Create a list of image paths
    image_paths = [os.path.join(photo_folder, file) for file in files]

    # Create an ImageSequenceClip from the image paths
    video = ImageSequenceClip(image_paths, fps=fps)

    # Set output file format based on extension
    if output_file.endswith(".mp4"):
        output_format = "libx264"
    elif output_file.endswith(".avi"):
        output_format = "mpeg4"
    else:
        raise ValueError("Unsupported output file format. Please use .mp4 or .avi")

    # Write the video to the output file
    video.write_videofile(output_file, fps=fps, codec=output_format)

    print(f"Video saved to: {output_file}")


# Example usage
photo_folder =  input("Enter the path to your photo folder: ")
output_file = photo_folder + "/video.mp4"
fps =  float(input("FPS: "))
print("Proccesing. . . ")
create_video_from_photos(photo_folder, output_file, fps)
print("Done. Video was saved in"+ output_file)
print("Press enter to close the console")
input()

