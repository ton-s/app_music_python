import tkinter
from PIL import Image

# initialize global variable
anim = None

def gif(app):
    '''Gif initialization

    Parameter
    ---------
    app : main window (tkinter)
    '''
    file="./music_player/icones_boutons/gif_music.gif"

    info = Image.open(file)

    # gives total number of frames that gif contains
    frames = info.n_frames

    # creating list of PhotoImage objects for each frames
    im = [tkinter.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

    gif_label = tkinter.Label(app,image="")
    gif_label.pack(pady=80)

    # display animation 
    animation(app, 0, im, gif_label, frames)

def animation(app, count, im, gif_label, frames):
    '''Image animation

    Parameters
    ----------
    app : main window (tkinter)
    count : number of images for the gif (int)
    im : list of PhotoImage objects for each frames (list)
    gif_label : Label of images (tkinter)
    frames : frames of images (tkinter)

    '''
    global anim
    im2 = im[count]

    gif_label.configure(image=im2, bd=0)
    count += 1
    if count == frames:
        count = 0
    anim = app.after(50,lambda :animation(app, count, im, gif_label, frames))