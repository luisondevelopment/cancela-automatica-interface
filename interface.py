from tkinter import *
from PIL import ImageTk, Image
import glob, os

var = 0
last_image = ""
counter = 0

def toggle_fullscreen(event=None):
    global var
    if var == 0:
        root.attributes("-fullscreen", True)
        var = 1
    else:
        root.attributes("-fullscreen", False)
        var = 0

def task():
    global last_image
    global counter

    files = glob.glob("./image/*.jpg")

    if len(files) == 0:
        img = ImageTk.PhotoImage(Image.open("./image/default/welcome.png")) 
        panel.config(image = img)
        panel.image = img

    for file in files:
        file = file.replace('\\','/')[2:]
        
        if last_image == file:
            if counter == 2:
                img = ImageTk.PhotoImage(Image.open("./image/default/welcome.png")) 
                panel.config(image = img)
                panel.image = img
                counter = 0
            else:
                counter += 1
        else:
            last_image = file
            print(file)
            img = ImageTk.PhotoImage(Image.open(file))
            panel.config(image = img)
            panel.image = img
    root.after(2000, task)

root = Tk()

root.title("Cancela Automática")
root.after(1000, task)
root.bind("<F11>", toggle_fullscreen)
root.attributes('-fullscreen',True)

panel = Label(root, image=None)
panel.pack(side="bottom", fill="both", expand="yes")
# path = "image/gol1.jpg"
# img = ImageTk.PhotoImage(Image.open(path))
# panel = Label(root, image = img)
# #The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()


