import tkinter

### MODULE APP ###
import menu_app.windowDownload
import fichiers.add_song

#### Main Menu ####

def main_menu(app, song_box):
    '''Main window menu

    Parameter
    ---------
    app : main window (tkinter)
    song_box : a list of song (tkinter)
    '''
    # initialize the menu bar
    menu_bar = tkinter.Menu(app, activebackground='#1144aa', activeforeground='#1144aa')

    # create the first menu
    first_menu = tkinter.Menu(menu_bar, tearoff=0)

    # cascade first menu
    menu_bar.add_cascade(label="Fichier", menu=first_menu)

    # named the cascading menu
    first_menu.add_command(label="Ajouter une musique")
    first_menu.add_command(label="Ajouter un dossier")
    first_menu.add_command(label="Créer une playlist")
    first_menu.add_separator()
    first_menu.add_command(label="Musique téléchargée", command=lambda:fichiers.add_song.add_musique_download(app, song_box))
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=app.quit)

    # create the second menu
    second_menu = tkinter.Menu(menu_bar)
    
    # menu boutton simple
    menu_bar.add_command(label="Télécharger musique", command=lambda: menu_app.windowDownload.create_window_download(app))


    # associated the menu to the window
    app.config(menu=menu_bar)




