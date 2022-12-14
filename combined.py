#!/usr/bin/python3
"""Download YouTube videos with a Python script"""
from pytube import YouTube
import pytube.request
import traceback

import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
import time

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

yt_app = tk.Tk()
yt_app.title('My YouTube Downloader')
yt_app.geometry('500x400')
yt_app.resizable(height=False, width=False)

def get_link():
	# grab value from the entry
	video = link_entry.get()
	result = download(video)
	link_entry.delete(0, 'end')
	progress_bar_main["value"] = 0
	if result == 1:
		# alert your video downloaded successfully
		msg.showinfo("Success", "You have successfully downloaded this video")
	else:
		msg.showerror("Unexpected Error", "An error occured, please try again")

# def increment():
#     for i in range(100):
#         progress_bar_main["value"] = i+1
#         yt_app.update()
#         time.sleep(0.1)

# ********** Layout m****************
link_label = tk.Label(yt_app, text="Video Link")
link_label.place(x=70, y=100)

link_entry = tk.Entry(yt_app, width=30)
link_entry.place(x=160, y=100)



download_btn = tk.Button(yt_app, text="Download", command=get_link)
download_btn.place(x = 200, y = 140)

progress_bar_label = tk.Label(yt_app, text="Downloading:")
progress_bar_label.place(x = 70, y =200)

progress_bar_main = ttk.Progressbar(yt_app, length='250', mode="determinate", orient=tk.HORIZONTAL)
progress_bar_main.place(x= 170, y = 200)


def progress_bar(stream, chunk, bytes_remaining):
	size = stream.filesize
	percent_downloaded = (float(size - bytes_remaining)/float(size)) * 100
	print(f"Downloaded: {round(percent_downloaded, 2)}%")
	progress_bar_main["value"] = percent_downloaded
	yt_app.update()
	return percent_downloaded


yt_app.mainloop()




# video = "https://www.youtube.com/shorts/L0DWAVbdEaM"
# download(video)