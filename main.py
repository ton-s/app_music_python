import tkinter

### MODULE APP ###
import menu_app.menu  
import music_player.Menu_music_play
import music_player.background_animation

def main():
    ''' Main function
    '''
    ### window initialization and settings ###
    app = tkinter.Tk()
    app.title("MusicApp")
    app.configure(background="#151515")

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

    # dimension min
    app.minsize(1000, 720)
    
    ### function call ###

    # Menu music player and interface
    song_box = music_player.Menu_music_play.music_play_button(app)
    music_player.background_animation.gif(app)

    # Main Menu
    menu_app.menu.main_menu(app, song_box)

    # end of the loop
    app.mainloop()



if __name__ == '__main__':
    main()
