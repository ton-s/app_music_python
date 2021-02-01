import tkinter

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

    #Création des images
    play_image = tkinter.PhotoImage(file="./music_player/icones_boutons/play.png")
    loop_image = tkinter.PhotoImage(file="./music_player/icones_boutons/replay.png")
    previous_image = tkinter.PhotoImage(file="./music_player/icones_boutons/back.png")
    next_image = tkinter.PhotoImage(file="./music_player/icones_boutons/next.png")
    shuffle_image = tkinter.PhotoImage(file="./music_player/icones_boutons/random.png")
    image_de_fond = tkinter.PhotoImage(file="./music_player/icones_boutons/logo Avengers.png")
    #Affichage de l'image de fond
    label = tkinter.Label(app, image=image_de_fond, relief="flat", borderwidth=0)
    label.pack(pady=20)

    #Créations des boutons
    mainframe = tkinter.Frame(app, width=800, height=600, background="#010123")

    play_button = tkinter.Button(mainframe, image=play_image, width=50, height=50, bg="#010123", borderwidth=0, activebackground="#010123")
    loop_button = tkinter.Button(mainframe, image=loop_image, width=50, height=50, bg="#010123", borderwidth=0, activebackground="#010123")
    previous_button = tkinter.Button(mainframe, image=previous_image, width=50, height=50, bg="#010123", borderwidth=0, activebackground="#010123")
    next_button = tkinter.Button(mainframe, image=next_image, width=50, height=50, bg="#010123", borderwidth=0, activebackground="#010123")
    shuffle_button = tkinter.Button(mainframe, image=shuffle_image, width=50, height=50, bg="#010123", borderwidth=0, activebackground="#010123")

    #Bouton volume
    volume_button = tkinter.Scale(app, length=300, orient="horizontal", label="VOLUME", relief="flat", showvalue=1, troughcolor="#010123", bg="#010123", fg="#ffffff")

    #Affichage (attention à l'ordre)
    volume_button.pack(side="bottom", pady=10)

    mainframe.pack(side="bottom")

    shuffle_button.pack(side="left", pady=0, padx=10)
    previous_button.pack(side="left", pady=0, padx=10)
    play_button.pack(side="left", pady=0, padx=10)
    next_button.pack(side="left", pady=0, padx=10)
    loop_button.pack(side="left", pady=0, padx=10)