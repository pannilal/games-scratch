
import webbrowser
import tkinter
from tkinter.constants import *

tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
label = tkinter.Label(frame, text="Hello! I  am Praneel ")
frame1 = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame1.pack(fill=BOTH, expand=2)


def na():
    webbrowser.open("www.timesofindia.indiatimes.com")


def nav():
    import spirograph


def navin():
    webbrowser.open("www.dictionary.com")


def navi():
    webbrowser.open("www.amarujala.com")


def n():
    webbrowser.open("www.google.com")


def MANSI():
    webbrowser.open("www.youtube.com")



label.pack(fill=X, expand=1)
button = tkinter.Button(frame1, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
button1 = tkinter.Button(frame, text="Dictionary", command=navin)
button1.pack(side=BOTTOM)
button2 = tkinter.Button(frame, text="News in Hindi", command=navi)
button2.pack(side=BOTTOM)
button = tkinter.Button(frame, text="News in English", command=na)
button.pack(side=BOTTOM)
button = tkinter.Button(frame, text="Entertainment", command=nav)
button.pack(side=BOTTOM)
button = tkinter.Button(frame, text="Google search", command=n)
button.pack(side=BOTTOM)
button = tkinter.Button(frame, text="Youtube", command=MANSI)
button.pack(side=BOTTOM)
button.pack(side=BOTTOM)


tk.mainloop()
