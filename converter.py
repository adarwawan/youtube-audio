import pafy
import os
from pydub import AudioSegment

SERVER_URL = 'https://www.youtube.com/watch?v='
# SERVER_URL = 'http://52.232.85.160/'

def download_video(video_id):
    if not video_id:
        return {"status": False, "error": "Video id not specified"}
    url = get_song(video_id)

    if url:
        return {"status": True, "url": url}

    try:
        video = pafy.new(str(video_id))
    except ValueError as e:
        print(e)
        return {"status": False, "error": "Invalid video id specified"}

    streams = video.streams
    if len(streams) > 0:
        filename = video.getbest().download(filepath="./dist", quiet=False)
        video_url = SERVER_URL + video_id
        return {"status": True, "url": video_url} 

    return {"status": False, "error": "No video streams found"}

def download_audio(video_id):
    if not video_id:
        return {"status": False, "error": "Video id not specified"}
    url = get_song(video_id)

    if url:
        return {"status": True, "url": url}

    try:
        video = pafy.new(str(video_id))
    except ValueError as e:
        print(e)
        return {"status": False, "error": "Invalid video id specified"}

    streams = video.audiostreams
    if len(streams) > 0:
        filename = video.getbestaudio().download(filepath="./dist", quiet=False)
        baseName = os.path.basename(filename)
        name = os.path.splitext(baseName)[0]
        convert_to_mp3(filename, name)
        os.remove(filename)
        song_url = SERVER_URL + video_id
        return {"status": True, "url": song_url} 

    return {"status": False, "error": "No audio streams found"}


def get_audio_url(vId):
    try:
        video = pafy.new(vId)
        url = video.getbestaudio(preftype='m4a').url
        return {"status": True, "url": url}
    except:
        return {"status": False, "error": "No audio streams found"}

def get_song(vid):
    path = './dist/' + vid + '.mp3'
    if(os.path.exists(path)):
        return SERVER_URL + vid
    
    return None

def convert_to_mp3(path, vid):
    AudioSegment.from_file(path).export("./dist/" + vid + ".mp3", format="mp3")