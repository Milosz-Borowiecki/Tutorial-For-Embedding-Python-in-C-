import tkinter as tk
import MyScripts.setgui as setg

def main():
    menu = tk.Tk()    

    menu.geometry("400x400+300+300")
    menu.resizable(False,False)
    menu.title("It works")
    menu.config(bg="#111111",bd=0)

    setg.setmenu(menu)

    menu.mainloop()

main()