import tkinter

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
