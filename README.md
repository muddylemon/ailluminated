# AIlluminated

The other day I was inspired by the concrete imagery of the poem Howl
and the power of stable diffusion and automation to produce some
interesting interpretations of the poem in video form. 

In retrospect I shouldn't have started with a 20 minute poem. 

Nevertheless, I've assembled the tools I gather together to make
these videos in this repo. 

## A tool to illuminate poems, songs and text

<iframe width="560" height="315" src="https://www.youtube.com/embed/PF0YYZi3R3I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/NTzZsg4wp6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/WtNr4xjv6TQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


<iframe width="560" height="315" src="https://www.youtube.com/embed/PpQOb_Dgvr0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


<iframe width="560" height="315" src="https://www.youtube.com/embed/B-qyqCi8TAA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


<iframe width="560" height="315" src="https://www.youtube.com/embed/PNXCImQ86vQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


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
