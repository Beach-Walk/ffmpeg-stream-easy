# FFmpeg Stream Easy
Start streaming media files over IP via UDP using ffmpeg. Script is specifically made to make it easier to pretranscode video files for low power machines that cannot do live transcoding. Playback tested on VLC

## Limitations
- Exiting via CLI is troublesome

## Requirements
- FFmpeg in PATH (FFmpeg should be usable from your terminal)

## How It Works
- Pick an option
  - Stream media
    - Stream will start based on options provided below
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
2. Add FFmpeg to PATH
3. Open terminal in udp-stream-easy directory and run:
    - python3 main.py
## Common Issues
 - Sometimes VLC multicast playback wont work correctly. To fix, disable VM interfaces (VMware, VirtualBox)
## To Do
  - More customizability 
  - Cleanup
