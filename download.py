import pytube
import os
from moviepy.editor import *

def download(video_url, extension):
    '''Download the video of youtube

    Parameters
    ----------
    video_url : the youtube video url (str)
    extension : the extension of video, mp4 or mp3 (str)

    '''
    
    # Load url in function youtube
    youtube = pytube.YouTube(video_url)

    # Set streams resolution
    try:
        video = youtube.streams.get_by_itag(18)
    except:
        video = youtube.streams.get_by_itag(140)

    # download video
    path_mp4 = video.download('./musiques')

    if extension == 'mp3':
        # get the base of path
        base = os.path.basename(path_mp4)

        # get the path of mp3
        path_mp3 = './musiques/' + os.path.splitext(base)[0] + '.mp3'

        convert(path_mp4, path_mp3 )

        print('Done')

def convert(path_mp4, path_mp3):
    '''Convert mp4 to mp3

    Parameters
    ----------
    path_mp4 : path of mp4 (str)
    path_mp3 : path of mp3 (str)
    '''

    # check if the path of mp4 exists
    if os.path.exists(path_mp4):

        mp3_file = str(path_mp3)

        videoclip = VideoFileClip(path_mp4)

        audioclip = videoclip.audio

        # convert mp4 to mp3
        audioclip.write_audiofile(mp3_file)

        audioclip.close()
        videoclip.close()

        # remove the mp4
        os.remove(path_mp4)



download('https://www.youtube.com/watch?v=M7X6oYg6iro', 'mp3')








