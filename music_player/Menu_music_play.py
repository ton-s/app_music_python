import tkinter
import tkinter.ttk

def music_play_button(app):
    """Display the menu with buttons and the background image

    Parameter
    ---------
    app : main window (tkinter)
    """
    #Variables globales car soucis du module PhotoImage (perte de l'image en mémoire)
    global play_image
    global loop_image
    global previous_image
    global next_image
    global shuffle_image
    global image_de_fond
    global list_image

    # Création des images
    play_image = tkinter.PhotoImage(file="./music_player/icones_boutons/play.png")
    loop_image = tkinter.PhotoImage(file="./music_player/icones_boutons/replay.png")
    previous_image = tkinter.PhotoImage(file="./music_player/icones_boutons/back.png")
    next_image = tkinter.PhotoImage(file="./music_player/icones_boutons/next.png")
    shuffle_image = tkinter.PhotoImage(file="./music_player/icones_boutons/random.png")
    list_image = tkinter.PhotoImage(file="./music_player/icones_boutons/list.png")
    #image_de_fond = tkinter.PhotoImage(file="./music_player/icones_boutons/logo Avengers.png")

    # # Affichage de l'image de fond
    # label = tkinter.Label(app, image=image_de_fond, relief="flat", borderwidth=0)

    # Create song box
    song_box = tkinter.Listbox(app, bg="#151515", fg='#00ffff', width=51, height=23, bd=0, relief='flat', selectbackground='#2ba487', selectforeground='#00ffff')
    
    # Create player control buttons
    mainframe = tkinter.Frame(app, background="#151515")

    play_button = tkinter.Button(mainframe, image=play_image, bg="#151515", borderwidth=0, activebackground="#151515")
    loop_button = tkinter.Button(mainframe, image=loop_image, bg="#151515", borderwidth=0, activebackground="#151515")
    previous_button = tkinter.Button(mainframe, image=previous_image, bg="#151515", borderwidth=0, activebackground="#151515")
    next_button = tkinter.Button(mainframe, image=next_image, bg="#151515", borderwidth=0, activebackground="#151515")
    shuffle_button = tkinter.Button(mainframe, image=shuffle_image, bg="#151515", borderwidth=0, activebackground="#151515")
    list_button = tkinter.Button(mainframe, image=list_image, bg="#151515", borderwidth=0, activebackground="#151515", command=lambda:display_song_box(app, song_box))

    volume_button = tkinter.ttk.Scale(mainframe, from_=0, to=100, value=100)

    #### DISPLAY ####
    mainframe.pack(side="bottom", pady=50)

    # background image
    #label.pack(pady=20)

    # Button
    list_button.pack(side="left", padx=10, pady=5)
    shuffle_button.pack(side="left", padx=10, pady=5)
    previous_button.pack(side="left", padx=10, pady=5)
    play_button.pack(side="left", padx=10, pady=5)
    next_button.pack(side="left", padx=10, pady=5)
    loop_button.pack(side="left", padx=10, pady=5)
    volume_button.pack(side="right", padx=10, pady=5)


# Display song
def display_song_box(app, song_box):
    """Display or not the box of songs in function of his relief

    Parameters
    ----------
    app : main window (tkinter)
    song_box : Listbox with the list of musics (Listbox)
    """
    #Check the relief of the Listbox
    #If it is flat, there is no Listbox, open one
    if song_box["relief"] == "flat":
        song_box.place(x=0, y=80)
        song_box.config(relief="groove")
    #If it is not flat, there is a Listbox, close it
    else:
        song_box.place_forget()
        song_box.config(relief="flat")