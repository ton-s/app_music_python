import tkinter
import os
import pygame

### MODULE APP ###
import menu_app.menu
import music_player.Menu_music_play

def add_musique_download(app, song_box):
    '''Add the music downloads folder in the listbox

    Parameters
    ----------
    app : main window (tkinter)
    song_box : a list of song (tkinter)
    '''

    # get the user of the PC
    user_computer = str(os.environ.get("USERNAME"))

    # path music path download from the application
    download_song = 'C:/Users/' + user_computer + '/Music/Musique_Download'

    # get music available (dispo) in the listbox
    music_available = song_box.get(0, 'end')
    
    if os.path.exists(download_song):

        # get all the music in the folder
        for song in os.listdir(download_song):

            #take only mp3 files because there are hidden files
            if ".mp3" in song:
                
                # remove the '.mp3' (for style)
                song = song.replace(".mp3", "")

                # checkcheck music duplication
                if not(song in music_available):
            
                    song_box.insert('end', song)

    
    song_box.bind('<<ListboxSelect>>', lambda event: test(song_box, download_song))

def test(song_box, download_song):

    print(song_box.curselection())  # get index of the music in listbox
    musique = song_box.get(song_box.curselection())
    musique = f"{download_song}/{musique}.mp3"

    pygame.mixer.music.load(musique)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)


