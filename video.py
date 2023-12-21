from pytube import YouTube

class VideoDownloader:
    def __init__(self, url) -> None:
        self.url = url
        self.yt = YouTube(url)

    def download_video(self, manzil = '.'):
        try:
            video_stream = self.yt.streams.get_highest_resolution()
            video_stream.download(manzil)
            print(f'Video {manzil} ga muvaffaqiyatli yuklandi')
        except Exception as e:
            print(f'Xatolik: {e}')

if __name__ == "__main__":
    url = 'https://youtu.be/jm3Y_UA2qUo?si=EtIAfUo_CCrFMq4t'
    manzil = '/home/xusanboy/Desktop/python/Projects/videoloyiha/video'
        
    downloader = VideoDownloader(url)
    downloader.download_video(manzil)