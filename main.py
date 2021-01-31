import random
from os import environ

from catt.api import CattDevice
from youtubesearchpython import VideosSearch

def search_videos(limit = 30):
    video_search = VideosSearch('videos for cats to watch', limit = limit, language = 'en', region = 'US')
    video_set = []
    while limit > len(video_set):
        if len(video_set) != 0:
            video_search.next()
        for vid in video_search.result()['result']:
            video_set.append(vid['link'])
            print(f"{vid['title']} - {vid['link']}")
    return video_set

def pick_video():
    video_set = search_videos()
    return random.choice(video_set)

def cast_video(video_url, device):
    cast = CattDevice(name=device)
    cast.volume(0.0)
    cast.play_url(video_url, resolve=True, block=True)

def cast_video_queue(video_urls, device):
    cast = CattDevice(name=device)
    cast.volume(0.0)
    for video in video_urls:
        cast.play_url(video, resolve=True, block=True)

if __name__ == "__main__":
    break_loop = False
    while not break_loop:
        try:
            video_list = search_videos()
            random.shuffle(video_list)
            
            cast_video_queue(video_list, environ.get("CHROMECAST_NAME", "Cat Room TV"))
        except KeyboardInterrupt:
            break_loop = True
