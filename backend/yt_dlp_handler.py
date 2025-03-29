
import subprocess

def get_yt_dlp_command(url: str):
    if "youtube.com" in url:
        return f"yt-dlp -f 'bv*[vcodec=h264][height=720]+ba/b' --merge-output-format mp4 -o '/downloads/{url.split('/')[-1]}.mp4' {url}"
    return f"yt-dlp -f best -o '/downloads/{url.split('/')[-1]}.mp4' {url}"

def download_video(command: str, path: str):
    subprocess.run(command, shell=True, check=True)
    