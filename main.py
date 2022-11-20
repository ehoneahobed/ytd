#!/usr/bin/python3
"""Download YouTube videos with a Python script"""
from pytube import YouTube
import pytube.request
import traceback

pytube.request.default_range_size = 337184

def download(video):
	try:
		yt = YouTube(video, on_progress_callback=progress_bar)
		yt = yt.streams.filter(progressive=True, file_extension='mp4')
		yt = yt.order_by('resolution')
		yt = yt.desc()
		yt = yt.first()
		yt = yt.download()
		return (1)
	except Exception:
		traceback.print_exc()
		return (0)


def progress_bar(stream, chunk, bytes_remaining):
	size = stream.filesize
	# print(bytes_remaining)
	percent_downloaded = (float(size - bytes_remaining)/float(size)) * 100
	print(f"Downloaded: {round(percent_downloaded, 2)}%")
	return percent_downloaded

# video = "https://www.youtube.com/shorts/L0DWAVbdEaM"
# download(video)