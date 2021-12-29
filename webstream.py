import ffmpeg_streaming
import os, random, threading
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
from dotenv import load_dotenv
import shutil

load_dotenv()
th = ""
webroot = os.getenv('WEBROOT')
print(webroot)
stream_dir = os.path.join(webroot, 'stream/')

def playFile(file):
    try:                                                                                                
        shutil.rmtree(stream_dir)
        os.mkdir(os.path.join(stream_dir, "*"))
    except:
        pass

    video = ffmpeg_streaming.input(file)


    _360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
    _1080p  = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))

    hls = video.hls(Formats.h264(), hls_list_size=1, hls_time=1, hls_playlist_type="event")
    hls.flags('delete_segments')
    #hls.auto_generate_representations()
    hls.representations(_360p)
    hls.fragmented_mp4()
    #dash = video.dash(Formats.h264())
    #dash.auto_generate_representations()
    try:
        print("Playing " + file)
        hls.output(os.path.join(stream_dir, 'hls.m3u8'), None, True, 'ffmpeg', None)
        #dash.output(os.path.join(stream_dir, 'dash.mpd'))
    except:
        return -1
    else:
        return 0



def playDirectory(path, shuffle=0):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if any(s in file for s in ['.avi', '.mkv', '.mp4']):
                files.append(os.path.join(r, file))
    if shuffle == 1:
        random.shuffle(files)
    while True:
        for i in range(len(files)):
            th = threading.Thread(target=playFile(files[i]))
            th.start()
            th.join()
playDirectory("/mnt/hdd3/Videos/The Simpsons", 1)
#print(playFile("/mnt/hdd3/Videos/Untitled Project.mp4"))
