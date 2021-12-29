import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size

video = ffmpeg_streaming.input("/mnt/hdd3/Videos/Untitled Project.mp4")

_360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
_480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
_720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
_1080p  = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))

hls = video.hls(Formats.h264())
hls.representations(_720p)
#hls.auto_generate_representations()
hls.output('/var/www/html/stream/hls.m3u8')
