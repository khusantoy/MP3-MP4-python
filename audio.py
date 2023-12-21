from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoToAudioConverter:
    def __init__(self, input_video) -> None:
        self.input_video = input_video

    def convert_to_audio(self, output_audio):
        try:
            video_clip = VideoFileClip(self.input_video)
            audio_clip = video_clip.audio

            audio_clip.write_audiofile(output_audio, codec='mp3')
            print(f'Audio {output_audio} manzilga muvaffaqiyatli joylandi')
        except Exception as e:
            print(f'Xatolik: {e}')

if __name__ == '__main__':
    input_video = '/home/xusanboy/Desktop/python/Projects/videoloyiha/video/Introducing the new Bing in Windows and More.mp4'
    output_audio = '/home/xusanboy/Desktop/python/Projects/videoloyiha/audio/audio.mp3'
    converter = VideoToAudioConverter(input_video)
    converter.convert_to_audio(output_audio)