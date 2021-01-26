import tkinter
import pygame 

### window initialization and settings ###
app = tkinter.Tk()
app.title("MusicApp")

# window logo
app.iconphoto(False, tkinter.PhotoImage(file='./images/logo.png'))

## center the window ##

# get  the resolution
screen_x = int(app.winfo_screenwidth())
screen_y = int(app.winfo_screenheight())
window_x = 800
window_y = 600

position_x = (screen_x // 2) - (window_x //2)
position_y = (screen_y // 2) - (window_y //2)

# create the dimension of the window
geo = f"{window_x}x{window_y}+{position_x}+{position_y}"
app.geometry(geo)



'''
les appels de fonction ...
'''




app.mainloop()