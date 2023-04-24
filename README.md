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


## Getting Started

1. Clone this repo
2. `python -m venv ail`
3. `source ./ail/bin/activate`
4. `pip install -r requirements`
5. Acquire your source material
    5.1 ex. `yt-dlp youtube.com/w=xxx -f 18`
6. Create a timestamp file
    6.1 Download the srt file from youtube
    6.2 or, use tap_ts.py to create a timestamp file
7. Create a prompt file from your timestamp file
    7.1 `python prompt.py`
    7.2 follow instructions to prefix and suffix the lines
8. Process the prompts through Stable Diffusion
9. Illustrate the material
    9.1 `python -m illustrate.py --lines inputs/your-file.txt --audio inputs/your-file.mp4 --images 'path/to/your/images'`
10. Checkout the result and adjust your timestamps as necessary

## Input material

1. Audio file - mp3 or mp4, etc, 
2. yt-dlp
3. timestamps text
4. srt files
