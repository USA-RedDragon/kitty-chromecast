import random
import signal
from os import environ

from catt.api import CattDevice
from youtubesearchpython import VideosSearch

castSession = None

def search_videos(limit = 30):
    video_search = VideosSearch('videos for cats to watch', limit = limit, language = 'en', region = 'US')
    video_set = []
    while limit > len(video_set):
        if len(video_set) != 0:
            video_search.next()
        for vid in video_search.result()['result']:
            video_set.append(vid['link'])
    return video_set

def pick_video():
    video_set = search_videos()
    return random.choice(video_set)

def cast_video(video_url, device):
    globals()["castSession"] = CattDevice(name=device)
    globals()["castSession"].volume(0.3)
    print("Playing video: " + video_url)
    globals()["castSession"].play_url(video_url, resolve=True, block=True)

def cast_video_queue(video_urls, device):
    globals()["castSession"] = CattDevice(name=device)
    globals()["castSession"].volume(0.3)
    for video in video_urls:
        print("Playing video: " + video)
        globals()["castSession"].play_url(video, resolve=True, block=True)

def signal_handler(_sig, _stack_frame):
    print("Exiting...")
    if globals()["castSession"] != None:
        globals()["castSession"].stop()
    exit()

if __name__ == "__main__":
    break_loop = False
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    while not break_loop:
        try:
            video_list = search_videos()
            random.shuffle(video_list)
            cast_video_queue(video_list, environ.get("CHROMECAST_NAME", "Cat Room TV"))
        except KeyboardInterrupt:
            break_loop = True
            signal_handler(None, None)
        except Exception as e:
            # Don't crash if there's an error, instead just try again
            print("Error: " + str(e))
            if globals()["castSession"] != None:
                globals()["castSession"].stop()
