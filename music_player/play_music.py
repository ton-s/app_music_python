import pygame

### MODULE APP ###

def load_music_download(song_box, path_folder):
    '''Load music from the listbox

    Parameters
    ----------
    song_box : the list of song (tkinter -> listbox)
    path_folder : the path to the music folder (str)
    '''
    # get the name and the path of music
    music = song_box.get(song_box.curselection())
    music = f"{path_folder}/{music}.mp3"

    pygame.mixer.music.load(music)

    pygame.mixer.music.play()
    print(song_box.get('active'))


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


def set_volume(volume_button):
    '''Set the music volume

    Parameter
    ---------
    volume_button : value of scale button (float)
    '''

    # value between 0.0 and 1.0
    volume_button = float(volume_button) / 100

    # adjusts the volume of the music
    pygame.mixer.music.set_volume(volume_button)


def set_replay(loop_button, loop_image, loop_activate_image):
    '''Loop the music once

    Parameters
    ----------
    loop_button : button to loop the music (tkinter)
    loop_image : image of loop button (tkinter)
    loop_activate_image : image of loop activate button (tkinter)
    '''
    pygame.mixer.music.rewind()
