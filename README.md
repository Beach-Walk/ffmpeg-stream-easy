# UDP Stream Easy
Start streaming media files via UDP using ffmpeg. Setting are specifically optimized for low power machines and VLC playback

## Limitations


## Requirements
- FFmpeg in PATH (FFmpeg should be usable from your terminal)

## How It Works
- Pick an option
  - Stream media
    - Stream will start based on options provided
    - URL: Output URL for FFmpeg, this could be anything FFmpeg supports
      - ?pkt_size=1316: This is needed for VLC playback
      - ttl=13: This is for multiple multicast hops (optional if not using multicast)
    - Repeat: Will loop through media infinitely
  - Convert media (for faster streaming)
    - This will convert media in the input folder any output them into the output folder
    - Preconverting media will make streaming faster for slower machines that cant live transcode
- Folder structure
  - Input:
    - This folder is for media you would like to transcode before streaming.
    - Transcoding before streaming will have improved performance for low end machines
  - Output:
    - After running the convert operation, media from the input folder will be output here once transcoded
    - Any media in this folder will be streamed by FFmpeg

## To Build & Run (assuming you have Py3)
1. Download ZIP or clone repository 
  - Uncompress the ZIP
2. Open terminal in udp-stream-easy directory and run:
    - python3 main.py
  ## To Do
  - More customizability 
  - Cleanup
