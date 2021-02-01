import tkinter
import pygame
import menu_app.menu  # Module app music
import music_player.Menu_music_play

def main():
    ''' Main function
    '''
    ### window initialization and settings ###
    app = tkinter.Tk()
    app.title("MusicApp")
    app.configure(background="#01011d")# Background

    # window logo
    app.iconbitmap('./images/logo.ico')

    ## center the window ##

    # get  the resolution
    screen_x = int(app.winfo_screenwidth())
    screen_y = int(app.winfo_screenheight())
    window_x = 1000
    window_y = 720

    # calculation to center the window
    position_x = (screen_x // 2) - (window_x // 2)
    position_y = (screen_y // 2) - (window_y // 2)

    # create the dimension of the window
    geo = f"{window_x}x{window_y}+{position_x}+{position_y}"
    app.geometry(geo)

    # change size
    # app.resizable(False, False)
    
    ### function call ###

    # Main Menu
    menu_app.menu.main_menu(app)

    # Menu music player
    music_player.Menu_music_play.music_play_button(app)

    # end of the loop
    app.mainloop()



if __name__ == '__main__':
    main()
