import threading
from tkinter import *
from PIL import Image, ImageTk
from _thread import *
import os 


def Client():
	from UDPclient import main
	entered_text = textentry.get()
	file = current_dir + "\\" + entered_text
	print(file)
	t1 = threading.Thread(target = main, args =[file])
	t1.start()

def Server():
	from UDPserver import main
	entered_text = textentry.get()
	file = current_dir + "\\" + entered_text
	print(file)
	t2 = threading.Thread(target = main, args =[file])
	t2.start()

def Exit():
	exit()

image = 'server2.png'
current_dir = os.getcwd()

#### main
window = Tk()
window.title("UDP Server")
window.configure(background = "black")
window.geometry("550x450") 

#### photo 
photol = PhotoImage(file = current_dir+'\\'+image)
image_1 = Label(window, image = photol, bg = "black") .grid(row =0, column = 0,sticky = W)

#### buttons for server, client, exit 
Button (window, text = "Client", width = 6, command = Client) .grid(row = 4, column = 0, padx = 5, pady= 5)
Button (window, text = "Server", width = 6, command = Server) .grid(row = 3, column = 0)
Button (window, text = "Exit", width = 6, command = Exit) .grid(row = 5, column = 0)

#### text entry for image path
Label (window, text="Specify Image to send:",bg ="black", fg ="white", font = "none 12 bold") .grid(row = 0, column = 4)

#### create a text entry
textentry = Entry(window, width = 20, bg="white")
textentry.grid(row = 0,column = 5, sticky = W)  


#### run the main loop
window.mainloop()

