#!/usr/bin/python3
#Kendal Goevert
#2-10-2020
'''GUI verson of the gamelibary'''
import tkinter as tk
from tkinter import scrolledtext
import pickle

TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)


##MAIN

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Game Library",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky ="news")
        self.btn_add = tk.Button(text = "Add", font = BUTTON_FONT)
        self.btn_add.grid(row = 1, column = 0)
        self.btn_add = tk.Button(text = "Edit", font = BUTTON_FONT)
        self.btn_add.grid(row = 2, column = 0)
        self.btn_add = tk.Button(text = "Search", font = BUTTON_FONT)
        self.btn_add.grid(row = 3, column = 0)        
        


if __name__ == "__main__":
    data_file = open("game_library", "rb")
    games = pickle.load(data_file)
    data_file.close()
    root = tk.Tk()
    root.title("Game Lib")
    root.geometry("500x500")
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0)

         
         
          
    root.mainloop()
    