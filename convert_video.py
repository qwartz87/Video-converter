import subprocess

def convert_to_h264(input_file, output_file):
    """
    Convert video to H.264 (MPEG4) with specified resolution, frame rate, and bitrate.

    Args:
        input_file (str): Path to the input video.
        output_file (str): Path to the output video.
    """
    try:
        command = [
            "ffmpeg",
            "-i", input_file,
            "-c:v", "libx264",
            "-b:v", "2247k",
            "-vf", "scale=1920:1080,fps=25",
            "-preset", "medium",
            "-c:a", "aac",
            "-b:a", "128k",
            output_file
        ]
        subprocess.run(command, check=True)
        print(f"Conversion successful! File saved as: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("FFmpeg is not installed. Please install it to use this script.")

# Example usage
input_video = "input.mp4"
output_video = "output_h264.mp4"
convert_to_h264(input_video, output_video)
