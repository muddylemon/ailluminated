import os
import argparse
import cv2
import imageio
import numpy as np
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.VideoClip import ImageClip, TextClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.fx.resize import resize
from scipy.interpolate import interp2d

def crossfade_transition(clips, transition_duration):
    """Create crossfade transitions between video clips.

    Args:
        clips (list): A list of video clips.
        transition_duration (int): The duration of the crossfade transition in seconds.

    Returns:
        VideoClip: A concatenated video clip with crossfade transitions.
    """
    faded_clips = []
    for idx, clip in enumerate(clips[:-1]):
        clip_with_transition = clips[idx].crossfadein(transition_duration).crossfadeout(transition_duration)
        faded_clips.append(clip_with_transition.set_start(clips[idx].start))
    # Add the last clip without a transition
    faded_clips.append(clips[-1].set_start(clips[-1].start))
    return concatenate_videoclips(faded_clips)

def convert_timestamp_to_seconds(timestamp):
    """Convert a timestamp string to seconds.

    Args:
        timestamp (str): The timestamp string in 'MM:SS' or 'SS' format.

    Returns:
        int: The timestamp converted to seconds.
    """
    parts = timestamp.split(':')
    if len(parts) == 1:
        return int(parts[0])
    elif len(parts) == 2:
        minutes, seconds = map(int, parts)
        return minutes * 60 + seconds

def extract_timestamps_and_poem_lines(lines):
    """Extract timestamps and poem lines from a text file.

    Args:
        lines (str): The path to the text file containing timestamps and poem lines.

    Returns:
        list: A list of timestamps.
        list: A list of poem lines.
    """
    timestamps = []
    poem_lines = []
    
    with open(lines, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if '\t' in line:
                timestamp_end = line.find('\t')
            else:
                timestamp_end = line.find(' ')
            timestamp = line[:timestamp_end]
            timestamps.append(timestamp)
        poem_line = line[timestamp_end:].strip()
        poem_lines.append(poem_line)

    return timestamps, poem_lines

def create_video(audio, output_file, images, lines, fps):
    """Create a video from a list of image files and an audio file.
    Args:
        audio (str): The path to the audio file.
        output_file (str): The path to the output video file.
        images (str): The path to the folder containing the images.
        lines (str): The path to the text file containing timestamps and poem lines.
        fps (int): The frame rate of the output video.
    """
    transition_duration = 2.5
    audio = AudioFileClip(audio)
    image_files = sorted([os.path.join(images, f) for f in os.listdir(images) if f.endswith('.jpg') or f.endswith('.png')])
    timestamps, poem_lines = extract_timestamps_and_poem_lines(lines)
    seconds_array = [convert_timestamp_to_seconds(ts) for ts in timestamps]
    clips = []

    for idx, image_file in enumerate(image_files):
        img = ImageClip(image_file)

        start_time = seconds_array[idx]
        end_time = seconds_array[idx + 1] if idx + 1 < len(seconds_array) else int(audio.duration)

        img = img.set_duration(end_time - start_time).set_start(start_time)

        clips.append(img)
        print(f"Clip {idx}: start_time = {start_time}, end_time = {end_time}, duration = {end_time - start_time}")

    video = crossfade_transition(clips, transition_duration)
    video = video.set_fps(fps).set_audio(audio)
    video.write_videofile(output_file, codec='libx264')

    print(f"Video created successfully! Output file: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Create a video from images and an audio file.')
    parser.add_argument('--images', type=str, required=True, help='The path to the folder containing the images.')
    parser.add_argument('--audio', type=str, required=True, help='The path to the audio file.')
    parser.add_argument('--lines', type=str, required=True, help='The path to the text file containing timestamps and poem lines.')
    parser.add_argument('--fps', type=int, default=24, help='The frame rate of the output video. Defaults to 24 fps.')

    args = parser.parse_args()

    # Generate the output file name from the images path
    folder_name = os.path.basename(os.path.normpath(args.images))
    output_file = os.path.join("videos", f"{folder_name}.mp4")

    create_video(args.audio, output_file, args.images, args.lines, args.fps)

if __name__ == '__main__':
    main()