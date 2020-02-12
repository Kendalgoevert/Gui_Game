#!/usr/bin/python3
#Kendal Goevert
#2-10-2020
'''GUI verson of the gamelibary'''
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import pickle

TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)


##MAIN

''''class MainMenu(tk.Frame):
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
        self.btn_add = tk.Button(text = "Remove", font = BUTTON_FONT)
        self.btn_add.grid(row = 4, column = 0)
        self.btn_add = tk.Button(text = "Save", font = BUTTON_FONT)
        self.btn_add.grid(row = 5, column = 0)    '''         

'''class Search(tk.Frame): 
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Search",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky ="news")
        #Search bb label
        self.lbl_search_by = tk.Label(text = "Search By", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 0, sticky ="news")
        #Search by entry box
        self.entry = tk.Entry (root)
        self.entry.grid(row = 2, column = 0)
        #Search for label
        self.lbl_search_for = tk.Label(text = "Search For", font = BUTTON_FONT)
        self.lbl_search_for.grid(row = 3, column = 0, sticky ="news")
        #Search for entry box
        self.entry = tk.Entry (root)
        self.entry.grid(row = 4, column = 0)               
        #Scrolled Text Box
        self.results = ScrolledText(height = 8, width = 40)
        self.results.grid(row = 5, columnspan = 3)
        #Back Clear and submit buttons
        self.btn_add = tk.Button(text = "Back", font = BUTTON_FONT)
        self.btn_add.grid(row = 6, column = 0)
        self.btn_add = tk.Button(text = "Clear", font = BUTTON_FONT)
        self.btn_add.grid(row = 6, column = 1)         
        self.btn_add = tk.Button(text = "Submit", font = BUTTON_FONT)
        self.btn_add.grid(row = 6, column = 2)'''

'''class Saved(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "File Saved!",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky ="news")  
        self.btn_add = tk.Button(text = "OK", font = BUTTON_FONT)
        self.btn_add.grid(row = 1, column = 0)''' 

'''class Edit(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Which title would you like to edit?",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, columnspan = 5, sticky ="news")  
        self.entry = tk.Entry (root)
        self.entry.grid(row = 1, columnspan =4 )
        self.btn_add = tk.Button(text = "Cancel", font = BUTTON_FONT)
        self.btn_add.grid(row = 2, column = 1)
        self.btn_add = tk.Button(text = "OK", font = BUTTON_FONT)
        self.btn_add.grid(row = 2, column = 2)''' 

'''class Remove(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Which title would you like to remove?",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, columnspan = 5, sticky ="news")  
        self.entry = tk.Entry (root)
        self.entry.grid(row = 1, columnspan =4 )
        self.btn_add = tk.Button(text = "Cancel", font = BUTTON_FONT)
        self.btn_add.grid(row = 2, column = 1)
        self.btn_add = tk.Button(text = "Remove", font = BUTTON_FONT)
        self.btn_add.grid(row = 2, column = 2)'''
        
        
'''class Verify_remove(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "These games are marked for removal",  font = BUTTON_FONT)
        self.lbl_title.grid(row = 0, columnspan = 5, sticky ="news")
        self.results = ScrolledText(height = 8, width = 40)
        self.results.grid(row = 1, columnspan = 3)
        self.btn_add = tk.Button(text = "Cancel", font = BUTTON_FONT)
        self.btn_add.grid(row = 2, column = 1)
        self.btn_add = tk.Button(text = "Remove", font = BUTTON_FONT)
        self.btn_add.grid(row = 2, column = 2)   '''

class Add(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Add Game",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, columnspan = 4, sticky ="news")
        #Genre entrybox
        self.lbl_search_by = tk.Label(text = "Genre: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 0, sticky ="news")        
        self.entry = tk.Entry (root)
        self.entry.grid(row = 2, column = 0)
        #Title entrybox
        self.lbl_search_by = tk.Label(text = "Title: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 1, sticky ="news")        
        self.entry = tk.Entry (root)
        self.entry.grid(row = 2, column = 1)
        #Decoloper entrybox
        self.lbl_search_by = tk.Label(text = "Devoloper: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 3, column = 0, sticky ="news")        
        self.entry = tk.Entry (root)
        self.entry.grid(row = 4, column = 0)  
        #Publisher entrybox
        self.lbl_search_by = tk.Label(text = "Publisher: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 3, column = 1, sticky ="news")        
        self.entry = tk.Entry (root)
        self.entry.grid(row = 4, column = 1)  
        #Year entrybox
        self.lbl_search_by = tk.Label(text = "Year: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 5, column = 0, sticky ="news")        
        self.entry = tk.Entry (root)
        self.entry.grid(row = 6, column = 0)
        #Notes Scrolled text box
        self.lbl_search_by = tk.Label(text = "Notes: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 7, column = 0, sticky ="news")                
        self.results = ScrolledText(height = 8, width = 40)
        self.results.grid(row = 8, columnspan = 3)
        #Cancel Reset Remove Buttons
        self.btn_add = tk.Button(text = "Cancel", font = BUTTON_FONT)
        self.btn_add.grid(row = 9, column = 1)
        self.btn_add = tk.Button(text = "Reset", font = BUTTON_FONT)
        self.btn_add.grid(row = 9, column = 2)
        self.btn_add = tk.Button(text = "Confirm", font = BUTTON_FONT)
        self.btn_add.grid(row = 9, column = 3)         
        
        
    
    
      
         
         
    
        
        
        
        
       

if __name__ == "__main__":
    data_file = open("game_library", "rb")
    games = pickle.load(data_file)
    data_file.close()
    root = tk.Tk()
    root.title("Game Lib")
    root.geometry("500x500")
    add = Add()
    add.grid(row = 0, column = 0)
    

         
    
          
    root.mainloop()
    