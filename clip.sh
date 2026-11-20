#!/bin/bash
# GTA 6 Clipper - Download, cut vertical clip, add make.fun pitch
set -e

OUTPUT_DIR="${1:-/output}"
mkdir -p "$OUTPUT_DIR"

# Use official GTA 6 Trailer 2 from Rockstar
YT_URL="https://www.youtube.com/watch?v=QdBZY2A1Gpo"

echo "Downloading GTA 6 footage..."
yt-dlp -f "best[height<=1080]" --max-filesize 50M \
  -o /tmp/gta6_footage.mp4 "$YT_URL" 2>&1 | tail -3

# Get duration
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/gta6_footage.mp4 2>/dev/null || echo "120")
START=$(echo "$DUR * 0.2" | bc | cut -d. -f1)

echo "Clipping 30s vertical 9:16..."
ffmpeg -y -ss "$START" -t 30 -i /tmp/gta6_footage.mp4 \
  -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=720:1280,drawtext=text='GTA VI':fontcolor=white:fontsize=72:x=(w-text_w)/2:y=40:shadowcolor=black:shadowx=3:shadowy=3:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf,drawtext=text='MAKE.FUN':fontcolor=#ff2e6e:fontsize=48:x=(w-text_w)/2:y=120:shadowcolor=black:shadowx=3:shadowy=3:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf,drawtext=text='Build your own game':fontcolor=white:fontsize=28:x=(w-text_w)/2:y=180:shadowcolor=black:shadowx=2:shadowy=2:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf,drawtext=text='@make.fun':fontcolor=#ff6b35:fontsize=24:x=(w-text_w)/2:y=h-60:shadowcolor=black:shadowx=2:shadowy=2:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf" \
  -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k \
  "$OUTPUT_DIR/clip.mp4" 2>&1 | tail -3

echo "Clip ready: $OUTPUT_DIR/clip.mp4"
ls -lh "$OUTPUT_DIR/clip.mp4"