# AIlluminated

The other day I was inspired by the concrete imagery of the poem Howl
and the power of stable diffusion and automation to produce some
interesting interpretations of the poem in video form. 

In retrospect I shouldn't have started with a 20 minute poem. 

Nevertheless, I've assembled the tools I gather together to make
these videos in this repo. 

## A tool to illuminate poems, songs and text

[![Somewhere I have never travelled...](https://img.youtube.com/vi/PF0YYZi3R3I/0.jpg)](https://www.youtube.com/watch?v=PF0YYZi3R3I "Somewhere I have never travelled...")

[![JCole - j hope](https://img.youtube.com/vi/NTzZsg4wp6M/0.jpg)](https://www.youtube.com/watch?v=NTzZsg4wp6M "JCole - j hope")

[![Liz Miele - comedy bit](https://img.youtube.com/vi/WtNr4xjv6TQ/0.jpg)](https://www.youtube.com/watch?v=WtNr4xjv6TQ "Liz Miele - comedy bit")

[![A Supermarket in California by Allen Ginsberg](https://img.youtube.com/vi/PpQOb_Dgvr0/0.jpg)](https://www.youtube.com/watch?v=PpQOb_Dgvr0 "A Supermarket in California by Allen Ginsberg")

[![Do not go gentle into that good night by Dylan Thomas](https://img.youtube.com/vi/B-qyqCi8TAA/0.jpg)](https://www.youtube.com/watch?v=B-qyqCi8TAA "Do not go gentle into that good night by Dylan Thomas")

[![Howl by Allen Ginsberg](https://img.youtube.com/vi/PNXCImQ86vQ/0.jpg)](https://www.youtube.com/watch?v=PNXCImQ86vQ "Howl by Allen Ginsberg")


# Ailluminated

Ailluminated is a Python-based video creation tool that combines images, audio, and subtitles into captivating videos with smooth crossfade transitions. It is designed to be versatile and user-friendly, suitable for various applications such as artistic videos, educational content, or memory preservation.

## Features

- Timestamp-based image and subtitle integration
- Crossfade transitions between images
- Customizable frame rate and output format

## Installation

1. Clone the repository:

```
git clone https://github.com/muddylemon/ailluminated.git
```

2. Change to the `ailluminated` directory:

```
cd ailluminated
```

3. Install the required Python libraries:

```
pip install -r requirements.txt
```

## Usage

1. Prepare your images, audio, and a text file with timestamps and corresponding subtitles. Place the images in a folder and ensure they are named sequentially (e.g., `img01.jpg`, `img02.jpg`).

2. Use the `convert_srt.py` script to convert an SRT subtitle file into a timestamp-based text file:

```
python convert_srt.py <input_srt_file> <output_timestamps_file>
```

Example:

```
python convert_srt.py inputs/my-video.srt inputs/my-video.txt
```

3. Run the `illustrate.py` script to create your video:

```
python illustrate.py --images <path_to_images_folder> --audio <path_to_audio_file> --lines <path_to_text_file_with_timestamps> [--fps <frame_rate>]
```

Example:

```
python illustrate.py --images images_folder --audio audio.mp3 --lines timestamps.txt --fps 24
```

4. The output video will be saved in the `videos` folder with the same name as the images folder.

## Contributing

We welcome contributions to improve Ailluminated! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch with your changes
3. Submit a pull request

We will review your changes and merge them if they are suitable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

