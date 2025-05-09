import os
import random
import subprocess
import argparse
from pathlib import Path

CLIP_DURATION = 120  # seconds
NUM_CLIPS = 10



def parse_args():
    parser = argparse.ArgumentParser(description="Process and create a video montage.")
    parser.add_argument("folder", help="Path to the folder containing MP4 files.")
    parser.add_argument("--cleanup", action="store_true", help="Clean up temporary files after completion.")
    parser.add_argument("--autoplay", action="store_true", help="Automatically play the final video using VLC after completion.")
    return parser.parse_args()

def get_video_duration(filepath):
    """Get video duration in seconds using ffprobe. Returns None if fails."""
    try:
        result = subprocess.run(
            [
                'ffprobe', '-v', 'error', '-show_entries',
                'format=duration', '-of',
                'default=noprint_wrappers=1:nokey=1', filepath
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=5
        )
        return float(result.stdout)
    except Exception as e:
        print(f"Invalid or unreadable video skipped: {filepath} ({e})")
        return None

def extract_clip(input_path, start_time, duration, output_path):
    subprocess.run([ 
        "ffmpeg", "-ss", str(start_time), "-i", input_path,
        "-t", str(duration), "-c", "copy", output_path,
        "-y"
    ])

def cleanup_output_folder(output_dir):
    """Remove all files in the output directory."""
    for file in output_dir.glob("*"):
        file.unlink(missing_ok=True)
    print(f"Cleaned up output folder: {output_dir}")

def concatenate_videos(input_clips, output_file):
    """Concatenate multiple clips into a final video."""
    # Create a temporary file list for ffmpeg
    concat_list_file = Path("concat_list.txt")
    
    with open(concat_list_file, 'w') as f:
        for clip in input_clips:
            f.write(f"file '{clip}'\n")
    
    # Run ffmpeg using the concat demuxer method
    concat_command = [
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', 
    '-i', str(concat_list_file), 
    '-c:v', 'libx264', '-preset', 'fast',
    '-c:a', 'aac', '-b:a', '192k', '-ac', '2', '-ar', '44100',
    '-movflags', '+faststart',
    str(output_file)
]

    
    print(f"Concatenating {len(input_clips)} clips into final video...")
    subprocess.run(concat_command, check=True)
    
    # Clean up the temporary list file
    concat_list_file.unlink()

def main(folder_path, cleanup=False, autoplay=False):
    folder = Path(folder_path)
    output_dir = folder / "output"
    
    # Cleanup the output folder before each run
    cleanup_output_folder(output_dir)

    output_dir.mkdir(exist_ok=True)  # Recreate the folder if it doesn't exist
    final_output = output_dir / "final_video.mp4"
    
    all_videos = list(folder.glob("*.mp4"))

    # Filter only valid videos
    valid_videos = []
    for video in all_videos:
        duration = get_video_duration(str(video))
        if duration is not None and duration > 1:
            valid_videos.append((video, duration))
        else:
            print(f"Invalid or unreadable video skipped: {video}")

    if len(valid_videos) < NUM_CLIPS:
        raise ValueError(f"Found only {len(valid_videos)} valid videos (need {NUM_CLIPS}).")

    selected_videos = random.sample(valid_videos, NUM_CLIPS)
    temp_clips = []

    for i, (video, duration) in enumerate(selected_videos):
        start = 0 if duration <= CLIP_DURATION else random.uniform(0, duration - CLIP_DURATION)
        out_clip = output_dir / f"clip_{i}.mp4"
        extract_clip(str(video), start, CLIP_DURATION, str(out_clip))
        temp_clips.append(out_clip)

    # Concatenate clips into the final video
    concatenate_videos(temp_clips, final_output)

    # Optional cleanup
    if cleanup:
        print(f"Cleaning up temporary files...")
        for temp_clip in temp_clips:
            temp_clip.unlink()

    print(f"Final video saved to: {final_output}")

    if autoplay:
        print("Playing final video...")
        try:
            os.startfile(str(final_output))  # Open with default media player
        except Exception as e:
            print(f"Error playing video: {e}")


if __name__ == "__main__":
    args = parse_args()
    main(args.folder, args.cleanup, args.autoplay)
