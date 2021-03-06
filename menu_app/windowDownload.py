import tkinter

### MODULE APP ###
import menu_app.download 

def create_window_download(app):
    '''generates the window and the interface to download music 

    Parameter
    ---------
    app : main window (tkinter)
    '''
    # create window download
    window_download_music = tkinter.Toplevel(app)

    # title of the window
    window_download_music.title('Télécharger musique')

    # window logo
    window_download_music.iconbitmap('./images/logo.ico')

    # dimension of the window
    window_download_music.geometry('510x200')

    # max and min resolution
    window_download_music.maxsize(510, 200)
    window_download_music.minsize(510, 200)

    # call to load the interface
    interface_download(window_download_music)


def interface_download(window_download_music):
    '''download window interface

    Parameter
    ---------
    window_download_music : the download window (tkinter)
    '''
    # Label
    label_title = tkinter.Label(window_download_music, text='Convertisseur Youtube mp3', fg='#1144aa', font=('Calibri', 20))
    label_title.grid(padx=100,pady=8, row=0)

    label_option = tkinter.Label(window_download_music, text='Entrer le lien url de la musique ci-dessous :', font=('Calibri', 12))
    label_option.grid(pady=4, row=1)

    # download information (notif)
    notification = tkinter.Label(window_download_music, font=('Calibri', 12))
    notification.grid(pady=10, row=4)

    # Entry url
    url = tkinter.StringVar()
    entry_url = tkinter.Entry(window_download_music, width=50, borderwidth=2, relief='groove', textvariable=url)
    entry_url.grid(row=2)
    
    # Download button
    download_button = tkinter.Button(window_download_music, width=20, text='Télécharger', font=('Calibri', 12), fg='#ffffff', bg='#316fea', command=lambda: get_url(url, entry_url, notification))
    download_button.grid(pady=5, row=3)

    # also downloads if the "Enter" key is pressed
    window_download_music.bind('<Return>', lambda event:get_url(url, entry_url, notification))

    
def get_url(url, entry_url, notification):
    '''retrieve the url of the text entry

    Parameters
    ----------
    url : the url of the music (str)
    entry_url : the text area (tkinter)
    notification : download information (tkinter)
    '''
    # get the url of the music
    music_url = str(url.get())

    try: 
        # download music 
        menu_app.download.download_music(music_url, 'mp3')

        # modify the information after execution
        notification.config(fg='#2ecc71', text='Téléchargement réussi ✔️')

    except:
        # check the errors
        if 'www.youtube.com' in music_url:
            # modify the information after execution when the url is invalid
            notification.config(fg='red', text='L\'URL n\'existe pas !')

        elif music_url == '':
            # modify the information after execution when the bar is empty
            notification.config(fg='red', text='Merci de saisir une URL valide avant de télécharger')
        
        else:
            # modify the information after execution
            notification.config(fg='red', text='L\'URL n\'est pas valide !')


    # clean the text area
    entry_url.delete(0, 'end')
