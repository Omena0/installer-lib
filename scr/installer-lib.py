import customtkinter as tki
import tkinter
import socket
import sys
from socket import *
import os


tkfont = tki.CTkFont
tkframe = tki.CTkFrame
tkbutton = tki.CTkButton
tklabel = tki.CTkLabel
tkProgressbar = tki.CTkProgressBar


class installer:
    def __init__(self, appName: str, appVer: str,fileServer: tuple,gui: bool):
        """Download files from fileserver.

        Args:
            appName (str): Name of your app, displayed in the inbuilt gui
            appVer (str): App version, displayed in the inbuilt gui
            fileServer (tuple): Address to download files from.
            gui (bool): If you want to use the gui or not.
        """
        self.appName = appName
        self.appVer = appVer

        self.fileServer = fileServer

        self.gui = gui
        
        if not gui: return
        self.app = tki.CTk()
        self.app.title(f'{appName} {appVer} Installer.')
        self.app.geometry('500x500')
        
        self.title = tklabel(master=self.app,text=f'Welcome to {appName} {appVer} installer!',font=tkfont(size=30))
        self.title.grid(row=0, column=0,padx=10,pady=10)
        
        self.progressbar = tkProgressbar(master=self.app,width=350,height=10,corner_radius=20,mode='determinate', determinate_speed=0.1)
        self.progressbar.set(0)
        self.progressbar.grid(column=0, row=1, pady=5, padx=5)
        
        
        self.installButton = tkbutton(master=self.app,text='Install',command=self.install)
        self.installButton.grid(row=2,column=0)
        
        
    def install(self,filepath='.'):
        if self.gui: self.progressbar.start()
        CHUNKSIZE = 1,000,000

        # Make a directory for the received files.
        os.makedirs(filepath,exist_ok=True)

        sock = socket()
        sock.connect(('localhost',5000))
        with sock,sock.makefile('rb') as clientfile:
            index = 0
            while True:
                raw = clientfile.readline()
                if not raw: break # no more files, server closed connection.

                filename = raw.strip().decode()
                length = int(clientfile.readline())
                print(f'Downloading {filename}...\n  Expecting {length:,} bytes...',end='',flush=True)

                path = os.path.join(filepath,filename)
                os.makedirs(os.path.dirname(path),exist_ok=True)

                # Read the data in chunks so it can handle large files.
                with open(path,'wb') as f:
                    while length:
                        chunk = min(length,CHUNKSIZE)
                        data = clientfile.read(chunk)
                        if not data: break
                        f.write(data)
                        length -= len(data)
                    else: # only runs if while doesn't break and length==0
                        # aka when a file is completed
                        print('Complete')
                        if self.gui: self.progressbar.set(index+1)
                        continue
                
                # socket was closed early.
                print('Incomplete')
                break 
        if self.gui: self.progressbar.stop()
        print('Done!')
        
        


    def ui(self):
        """Show the inbuilt gui.
        
        Raises:
            Exception: If gui is not enabled.
        """        
        if self.gui: self.app.mainloop()
        else: raise Exception('GUI not enabled!')

