import tkinter
import tkinter.ttk

# initialize global variable
play_image = None
pause_image = None
loop_image = None
previous_image = None
next_image = None
shuffle_image = None
list_image = None
cancel_image = None

def music_play_button(app):
    """Display the menu with buttons and the background image

    Parameter
    ---------
    app : main window (tkinter)

    Return
    ------
    song_box : returns the list of songs (tkinter)
    """
    #Variables globales car soucis du module PhotoImage (perte de l'image en mémoire)
    global play_image
    global pause_image
    global loop_image
    global previous_image
    global next_image
    global shuffle_image
    global list_image
    global cancel_image

    # Création des images
    play_image = tkinter.PhotoImage(file="./music_player/icones_boutons/play.png")
    pause_image = tkinter.PhotoImage(file="./music_player/icones_boutons/pause.png")
    loop_image = tkinter.PhotoImage(file="./music_player/icones_boutons/replay.png")
    previous_image = tkinter.PhotoImage(file="./music_player/icones_boutons/back.png")
    next_image = tkinter.PhotoImage(file="./music_player/icones_boutons/next.png")
    shuffle_image = tkinter.PhotoImage(file="./music_player/icones_boutons/random.png")
    list_image = tkinter.PhotoImage(file="./music_player/icones_boutons/list.png")
    cancel_image = tkinter.PhotoImage(file="./music_player/icones_boutons/cancel.png")

    # Create song box
    song_box = tkinter.Listbox(app, bg="#151515", fg='#00ffff', width=51, height=23, bd=0, relief='flat', selectbackground='#2ba487', selectforeground='#00ffff')
    
    # Create player control buttons
    mainframe = tkinter.Frame(app, background="#151515")

    play_button = tkinter.Button(mainframe, image=play_image, bg="#151515", borderwidth=0, activebackground="#151515", command=lambda:change_play_and_pause(app, play_button, play_image, pause_image))
    loop_button = tkinter.Button(mainframe, image=loop_image, bg="#151515", borderwidth=0, activebackground="#151515")
    previous_button = tkinter.Button(mainframe, image=previous_image, bg="#151515", borderwidth=0, activebackground="#151515")
    next_button = tkinter.Button(mainframe, image=next_image, bg="#151515", borderwidth=0, activebackground="#151515")
    shuffle_button = tkinter.Button(mainframe, image=shuffle_image, bg="#151515", borderwidth=0, activebackground="#151515")
    list_button = tkinter.Button(mainframe, image=list_image, bg="#151515", borderwidth=0, activebackground="#151515", command=lambda:display_song_box(app, song_box, list_image, cancel_image, list_button))

    volume_button = tkinter.ttk.Scale(mainframe, from_=0, to=100, value=100)

    #### DISPLAY ####
    mainframe.pack(side="bottom", pady=50)

    # Button
    list_button.pack(side="left", padx=10, pady=5)
    shuffle_button.pack(side="left", padx=10, pady=5)
    previous_button.pack(side="left", padx=10, pady=5)
    play_button.pack(side="left", padx=10, pady=5)
    next_button.pack(side="left", padx=10, pady=5)
    loop_button.pack(side="left", padx=10, pady=5)
    volume_button.pack(side="right", padx=10, pady=5)

    # return the status of the listbox
    return song_box

# Display song
def display_song_box(app, song_box, list_image, cancel_image, list_button):
    """Display or not the box of songs in function of his relief

    Parameters
    ----------
    app : main window (tkinter)
    song_box : Listbox with the list of musics (Listbox)
    list_image : image of a list (tkinter (png))
    cancel_image : image of a cross (tkinter (png))
    list_button : button list (tkinter)

    Note
    ----
    warning to the position of the image in the code otherwise the name of `list_button["image"]` changes
    """
    
    # if image list change to cross-hair and bring up the list box else ...
    if list_button["image"] == 'pyimage7':
        song_box.place(x=0, y=80)

        # change image
        list_button.config(image=cancel_image)
        
    else:
        # make the list box disappear
        song_box.place_forget()

        # change image
        list_button.config(image=list_image)


# supprimer quand on commence la musique et remmetre au propre
# la fonction est la juste pour test mais sera combiner avec le lancement ... de la musique
# faire le même pour la couleur de random et replay
def change_play_and_pause(app, play_button, play_image, pause_image):
    '''
    Parameter
    ---------
    app : main window (tkinter)
    '''

    if play_button["image"] == 'pyimage1':
        play_button.config(image=pause_image)

    else:
        play_button.config(image=play_image)