import tkinter as tk
from tkinter import ttk

def setmenu(window):

    # Canvas
    canvas = tk.Canvas(window,bg="#111111",bd=0,highlightthickness=0,relief="flat")
    canvas.pack(side="top",expand=True,fill="both")

    #   Grid configuration
    canvas.columnconfigure(0,weight=1)
    canvas.columnconfigure(1,weight=3)
    canvas.columnconfigure(2,weight=1)
    canvas.rowconfigure(0,weight=1)
    canvas.rowconfigure(1,weight=1)
    canvas.rowconfigure(2,weight=1)

    # Center text
    label = tk.Label(canvas,text="Python in C++",fg="#ffffff",bg="#111111",bd=0,font=('Arial',25))
    label.grid(column=1,row=1,padx=15)