import tkinter
import download

def create_window():
    '''generates the window and the interface to download music 
    '''
    
    # create window
    window_download_music = tkinter.Tk()

    # title of the window
    window_download_music.title('télécharger musique')

    # window logo
    #window_download_music.iconbitmap('../images/logo2.ico')

    # dimension of the window
    window_download_music.geometry('480x200')

    # max and min resolution
    window_download_music.maxsize(480, 200)
    window_download_music.minsize(480, 200)

    # call to load the interface
    interface_download(window_download_music)

    window_download_music.mainloop()


def interface_download(window_download_music):
    '''download window interface

    Parameter
    ----------
    window_download_music : the download window (tkinter)
    '''
    # Label
    label_title = tkinter.Label(window_download_music, text='Download Youtube music', fg='#192a56', font=('Calibri', 20))
    label_title.grid(padx=100,pady=8, row=0)

    label_option = tkinter.Label(window_download_music, text='Entrer le lien de la musique :', font=('Calibri', 12))
    label_option.grid(pady=4, row=1)

    # download information (notif)
    notification = tkinter.Label(window_download_music, font=('Calibri', 12))
    notification.grid(pady=10, row=4)

    # Entry url
    url = tkinter.StringVar()
    entry_url = tkinter.Entry(window_download_music, width=50, textvariable=url)
    entry_url.grid(row=2)
    
    # Download button
    download_button = tkinter.Button(window_download_music, width=20, text='Télécharger', font=('Calibri', 12), fg='#ffffff', bg='#2e86de', command=lambda: get_url(url, entry_url, notification))
    download_button.grid(pady=5, row=3)

    
def get_url(url, entry_url, notification):
    '''retrieve the url of the text entry

    Parameters
    ---------
    url : the url of the music (str)
    entry_url : the text area (tkinter)
    notification : download information (tkinter)
    '''
    # get the url of the music
    music_url = str(url.get())

    try: 
        # download music 
        download.download_music(music_url, 'mp3')

        # modify the information during execution
        notification.config(fg='#2ecc71', text='Téléchargement réussi !')

    except:
        # modify the information during execution
        notification.config(fg='#e74c3c', text='Téléchargement impossible !')

    # clean the text area
    entry_url.delete(0, 'end')




create_window()


