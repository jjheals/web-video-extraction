# web-video-extractor

## Description

A collection of scripts to extract videos from websites. 

*Right now, only the [youtube-scraper](./youtube/main.py) is implemented.*

## Usage

### Youtube

Step 1: Open [youtube/main.py](./youtube/main.py)

Step 2: Run main file

```
python main.py
```

Step 3: Follow prompts in the terminal

Step 4: Done. 

**Notes:** If you are using a text file as input, make sure the file exists and it is a .txt file. Additionally, the URLs should be separated by newlines. For example: 

```text 
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=QdezFxHfatw&pp=ygUJcmljayByb2xs 
https://www.youtube.com/watch?v=XGxIE1hr0w4&pp=ygUJcmljayByb2xs
```

### Extracting Frames

The main file in the [break-video directory](./break-video/main.py) will extract the frames from a video and output them as .png files to a specified directory. At runtime you will be prompted for an input file (the video, as mp4) and an output directory. Note that the output directory will be created if it doesn't exist. The frames will be dumped to the output directory as PNGs. 
