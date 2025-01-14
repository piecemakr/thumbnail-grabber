import os
import requests
from pathlib import Path

# List of YouTube URLs
youtube_urls = [
    "https://youtube.com/shorts/donhOsGdo-Q",
    "https://youtube.com/shorts/HBUmiUsOIYw",
    "https://youtube.com/shorts/J-UXEqUsQGQ",
    "https://youtube.com/shorts/LSNI6UOH1Qc",
    "https://youtube.com/shorts/WLWTRxYKLkY",
    "https://youtube.com/shorts/r4zHV4eFA3M",
    "https://youtube.com/shorts/Z12Hzwzy9ZU",
    "https://youtube.com/shorts/jgE_fqrIBR4",
    "https://youtube.com/shorts/y-tppSYqzwI",
]

# Get the desktop path
desktop_path = Path.home() / "Desktop"
output_folder = desktop_path / "thumbnails"
os.makedirs(output_folder, exist_ok=True)

def get_thumbnail_url(video_url):
    """Extracts video ID and generates thumbnail URLs."""
    if "youtube.com/shorts/" in video_url:
        video_id = video_url.split("shorts/")[-1].split("?")[0]
    elif "youtube.com/watch?v=" in video_url:
        video_id = video_url.split("v=")[-1].split("&")[0]
    else:
        raise ValueError(f"Invalid YouTube URL format: {video_url}")
    
    resolutions = ["maxresdefault.jpg", "sddefault.jpg", "hqdefault.jpg", "mqdefault.jpg", "default.jpg"]
    return [f"https://img.youtube.com/vi/{video_id}/{res}" for res in resolutions], video_id

def download_thumbnail(thumbnail_urls, output_path):
    """Attempts to download the thumbnail from available resolutions."""
    for url in thumbnail_urls:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {output_path}")
            return
    print(f"Failed to download: {thumbnail_urls[0]}")

# Process each YouTube URL
for url in youtube_urls:
    try:
        thumbnail_urls, video_id = get_thumbnail_url(url)
        output_path = output_folder / f"{video_id}.jpg"
        download_thumbnail(thumbnail_urls, output_path)
    except Exception as e:
        print(f"Error processing {url}: {e}")
