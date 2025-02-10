import yt_dlp
import os

class DownloadHelper:

    def __init__(self, url):
        self.url = url

    def download(self):
        dir = os.getcwd()
        output_path = os.path.join(dir, 'temp/video_file.mpeg') 
        ydl_opts = {
        'format': 'best',  
        'outtmpl': output_path 
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
        return output_path





