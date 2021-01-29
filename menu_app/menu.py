import tkinter
import windowDownload  # Module app music

#### Main Menu ####

def main_menu(app):
    '''Main window menu

    Parameter
    ---------
    app : main window (tkinter)
    '''

    # initialize the menu bar
    menu_bar = tkinter.Menu(app, activebackground='#1144aa', activeforeground='#1144aa')

    # create the first menu
    first_menu = tkinter.Menu(menu_bar, tearoff=0)
    first_menu.add_command(label="Ajouter")
    first_menu.add_command(label="Playlist")
    first_menu.add_command(label="Quitter", command=app.quit)

    # cascade first menu
    menu_bar.add_cascade(label="Fichier", menu=first_menu)

    # create the second menu
    second_menu = tkinter.Menu(menu_bar)
    
    # menu boutton simple
    menu_bar.add_command(label="Télécharger musique", command=lambda: windowDownload.create_window_download(app))


    # associated the menu to the window
    app.config(menu=menu_bar)




