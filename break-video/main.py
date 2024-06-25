import cv2
import os


def extract_frames(video_path, output_dir):
    """Extracts the frames from a video. 
        
        Args 
            video_path (str): path to the input video.
            output_dir (str): path to output the images.

        Returns
            None: writes the frames from the video as .png files to the output dir. 
    """    
    # Check if the input file exists 
    if not os.path.exists(video_path): 
        print(f'\033[91mERROR: \033[90mvideo path "{video_path}" does not exist. Exiting.')
        return 
    
    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Capture video
    cap = cv2.VideoCapture(video_path)
    
    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        print(f'Processing {frame_count}/{total_frames}')
        
        # Break when done
        if not ret:
            break
        
        # Write the frame to the output directory
        frame_filename = os.path.join(output_dir, f'frame_{frame_count:05d}.png')
        cv2.imwrite(frame_filename, frame)
        
        frame_count += 1
    
    # Release the video capture object
    cap.release()
    
    # Info print
    print(f'Extracted {frame_count} frames from {video_path}')

# Path to the video file
video_path = input('\033[92mEnter the path to the input file (.mp4): \033[90m')

# Output directory to save frames
output_dir = input('\033[92mEnter the output directory (will be created if it does not exist): \033[90m')

# Extract frames from video
extract_frames(video_path, output_dir)
