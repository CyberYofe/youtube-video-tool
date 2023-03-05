import tkinter as tk
from pytube import YouTube

def download_video():
    try:
        # get the url from the user input
        url = url_input.get()

        # create a YouTube object and get the video stream with the highest resolution
        youtube_obj = YouTube(url)
        video_stream = youtube_obj.streams.get_highest_resolution()

        # set the download location
        download_location = download_location_input.get()

        # download the video
        video_stream.download(download_location)

        # show a success message
        status_label.config(text="Download successful!")
    except Exception as e:
        # show an error message if the download fails
        status_label.config(text="Error: " + str(e))

# create the Tkinter window
window = tk.Tk()
window.title("YouTube Downloader")

# set the window size
window.geometry("200x200")

# create the URL input field and label
url_label = tk.Label(window, text="Enter the URL of the YouTube video:")
url_label.pack()
url_input = tk.Entry(window)
url_input.pack()

# create the download location input field and label
download_location_label = tk.Label(window, text="Enter the path to store the video:")
download_location_label.pack()
download_location_input = tk.Entry(window)
download_location_input.pack()

# create the download button
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

# create the status label
status_label = tk.Label(window, text="")
status_label.pack()

#credits
label = tk.Label(text="Made by yofe#1285")
label.pack()

# start the Tkinter event loop
window.mainloop()
