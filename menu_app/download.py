import pytube
import os
from moviepy.editor import *

def download_music(video_url, extension):
    '''Download the video of youtube

    Parameters
    ----------
    video_url : the youtube video url (str)
    extension : the extension of video, mp4 or mp3 (str)

    Note
    ----
    Version Windows

    '''
    # Load url in function youtube
    youtube = pytube.YouTube(video_url)

    # get the user of the PC
    user_computer = str(os.environ.get("USERNAME"))
    path_download = 'C:/Users/' + user_computer + '/Music/Musique_Download'

    # Set streams resolution
    try:
        video = youtube.streams.get_by_itag(18)
        # download video
        path_mp4 = video.download(path_download)

    except:
        video = youtube.streams.get_by_itag(140)
        # download video
        path_mp4 = video.download(path_download)
        
        # impossible to convert because it is already audio
        exit()

    if extension == 'mp3':
        # get the path of mp3
        path_mp3 = path_download + '/' + youtube.title + '.mp3'

        # check if the music exists
        if not(os.path.exists(path_mp3)):
            # converter
            convert(path_mp4, path_mp3)
        else:
            # remove the mp4
            os.remove(path_mp4)

        # check if everything is correctly executed
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
        