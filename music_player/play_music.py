import pygame

### MODULE APP ###

def load_music_download(song_box, download_song):
    '''Load music from the listbox

    Parameters
    ----------
    song_box : the list of song (tkinter -> listbox)
    download_song : the path to the music download folder (str)
    '''
    # get the name and the path of music
    music = song_box.get(song_box.curselection())
    music = f"{download_song}/{music}.mp3"

    pygame.mixer.music.load(music)
    pygame.mixer.music.play()


def play_pause_song(play_button, play_image, pause_image):
    '''
    Parameters
    ----------
    play_button : button to start the music (tkinter)
    play_image : image of the play button (tkinter)
    pause_image : image of the pause button (tkinter)
    
    '''

    if play_button["image"] == 'pyimage1':
        # change the image
        play_button.config(image=pause_image)

        # play song
        pygame.mixer.music.unpause()

    else:
        # change the image
        play_button.config(image=play_image)

        # pause song
        pygame.mixer.music.pause()




