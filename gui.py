#!/usr/bin/python3
"""YouTube downloader"""
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
from tkinter import filedialog
from main import download, progress_bar
import time

yt_app = tk.Tk()
yt_app.title('My YouTube Downloader')
yt_app.geometry('500x400')
yt_app.resizable(height=False, width=False)

def get_link():
	# grab value from the entry
	video = link_entry.get()
	path = path_entry.get()
	result = download(video, path)
	link_entry.delete(0, 'end')
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

def get_directory():
	global directory_path
	filepath = filedialog.askdirectory()
	directory_path.set(filepath)

# ********** Layout m****************
link_label = tk.Label(yt_app, text="Video Link")
link_label.place(x=70, y=100)

link_entry = tk.Entry(yt_app, width=30)
link_entry.place(x=160, y=100)


# label and entry for destination directory
path_label = tk.Label(yt_app, text="Download to:")
path_label.place(x=70, y=140)

directory_path = tk.StringVar()
path_entry = tk.Entry(yt_app, width=20, textvariable=directory_path)
path_entry.place(x=160, y=140)
# browse files button
browse_btn = tk.Button(yt_app, text="browse", command=get_directory)
browse_btn.place(x = 330, y = 135)

download_btn = tk.Button(yt_app, text="Download", command=get_link)
download_btn.place(x = 200, y = 180)

progress_bar_label = tk.Label(yt_app, text="Downloading:")
progress_bar_label.place(x = 70, y =240)

progress_bar_main = ttk.Progressbar(yt_app, length='250', mode="determinate", orient=tk.HORIZONTAL)
progress_bar_main.place(x= 170, y = 240)
# increment()

yt_app.mainloop()