
import time
import redis
from backend.yt_dlp_handler import download_video

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

while True:
    job = redis_client.lpop('download_queue')
    if job:
        url = job.decode('utf-8')
        command = f"yt-dlp -f best -o '/downloads/{url.split('/')[-1]}.mp4' {url}"
        download_video(command, f"/downloads/{url.split('/')[-1]}.mp4")
        redis_client.lrem('download_queue', 0, job)
    time.sleep(5)
    