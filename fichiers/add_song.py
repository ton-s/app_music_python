import tkinter
import os

### MODULE APP ###
import menu_app.menu
import music_player.Menu_music_play
import music_player.play_music

def add_musique_download(song_box):
    '''Add the music downloads folder in the listbox

    Parameters
    ----------
    song_box : a list of song (tkinter)
    '''

    # get the user of the PC
    user_computer = str(os.environ.get("USERNAME"))

    # path music path download from the application
    path_folder = 'C:/Users/' + user_computer + '/Music/Musique_Download'

    # get music available (dispo) in the listbox
    music_available = song_box.get(0, 'end')
    
    if os.path.exists(path_folder):

        # get all the music in the folder
        for song in os.listdir(path_folder):

            #take only mp3 files because there are hidden files
            if ".mp3" in song:
                
                # remove the '.mp3' (for style)
                song = song.replace(".mp3", "")

                # checkcheck music duplication
                if not(song in music_available):
            
                    song_box.insert('end', song)

    
    song_box.bind('<<ListboxSelect>>', lambda event: music_player.play_music.load_music_download(song_box, path_folder))

# def test(song_box, path_folder):

#     print(song_box.curselection())  # get index of the music in listbox
#     musique = song_box.get(song_box.curselection())
#     musique = f"{path_folder}/{musique}.mp3"

#     pygame.mixer.music.load(musique)
#     pygame.mixer.music.play()
#     pygame.mixer.music.set_volume(1)



