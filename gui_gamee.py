#!/usr/bin/python3
#Kendal Goevert
#2-10-2020
'''GUI verson of the gamelibary'''

import pickle

import tkinter as tk

from tkinter.scrolledtext import ScrolledText

TITLE_FONT = ("Times New Roman", "24")
BUTTON_FONT = ("Arial", "15")

class Screen(tk.Frame):
   
    current = 0
   
    def __init__(self):
        tk.Frame.__init__(self)
       
    def switch_frame():
        screens[Screen.current].tkraise()

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Game Library",
                             font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Add", font = BUTTON_FONT,
                                 command = self.go_add)
        self.btn_add.grid(row = 1, column = 0, sticky = "news")
       
        self.btn_edit = tk.Button(self, text = "Edit", font = BUTTON_FONT,
                                 command = self.go_edit)
        self.btn_edit.grid(row = 2, column = 0, sticky = "news")
       
        self.btn_search = tk.Button(self, text = "Search", font = BUTTON_FONT,
                                 command = self.go_search)
        self.btn_search.grid(row = 3, column = 0, sticky = "news")
       
        self.btn_remove = tk.Button(self, text = "Remove", font = BUTTON_FONT,
                                 command = self.go_remove)
        self.btn_remove.grid(row = 4, column = 0, sticky = "news")
       
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT,
                                 command = self.go_save)
        self.btn_save.grid(row = 5, column = 0, sticky = "news")
       
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
   
    def go_add(self):
        Screen.current = 1
        Screen.switch_frame()
       
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        frm_edit_list = EditGame1(pop_up)
        frm_edit_list.grid(row = 0, column = 0)
   
    def go_search(self):
        Screen.current = 4
        Screen.switch_frame()
       
    def go_remove(self):
        pop_up = tk.Tk()
        pop_up.title("Remove")
        frm_edit_list = Remove(pop_up)
        frm_edit_list.grid(row = 0, column = 0)
   
    def go_save(self):
        pop_up = tk.Tk()
        pop_up.title("Save")
        frm_edit_list = Save(pop_up)
        frm_edit_list.grid(row = 0, column = 0)    

class SearchParamiters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
       
        self.chk_genre = tk.Checkbutton(self, text = "Genre")
        self.chk_genre.grid(row = 0, column = 0, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Title")
        self.chk_genre.grid(row = 1, column = 0, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Developer")
        self.chk_genre.grid(row = 2, column = 0, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Publisher")
        self.chk_genre.grid(row = 3, column = 0, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Platform")
        self.chk_genre.grid(row = 4, column = 0, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Release Year")
        self.chk_genre.grid(row = 0, column = 1, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Rating")
        self.chk_genre.grid(row = 1, column = 1, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Single/Multi")
        self.chk_genre.grid(row = 2, column = 1, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Price")
        self.chk_genre.grid(row = 3, column = 1, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Played?")
        self.chk_genre.grid(row = 4, column = 1, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Purchase Date")
        self.chk_genre.grid(row = 0, column = 2, sticky = "nws")
       
        self.chk_genre = tk.Checkbutton(self, text = "Notes")
        self.chk_genre.grid(row = 1, column = 2, sticky = "nws")
       
               
       

class SearchGame(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "SEARCH",
                             font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0,
                            sticky = "news")
        self.lbl_search_by = tk.Label(self, text = "Search By",
                             font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 0,
                            sticky = "news")        
       
        options = ["Genre", "Title", "Publisher", "Developer", "Platform", "Release Year",
                   "Rating", "Single/Multiplayer", "Price", "Played?", "Purchase Date"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self, self.tkvar, *options)
        self.menu.grid(row = 2, column = 3)                
       
        self.lbl_search_for = tk.Label(self, text = "Search For",
                             font = BUTTON_FONT)
        self.lbl_search_for.grid(row = 3, column = 0,
                            sticky = "news")        
        self.entry = tk.Entry(self)
        self.entry.grid(row = 4, column = 0,
                        sticky = "news")        
       
        self.results = ScrolledText(self, height = '8', width = '40')
        self.results.grid(row = 5, columnspan = 3,
                          sticky = "news")
       
        self.frm_search_paramiters = SearchParamiters(self)
        self.frm_search_paramiters.grid(row = 1, column = 3, columnspan = 3, rowspan = 4,
                                        sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Back", font = BUTTON_FONT,
                                 command = self.go_main)
        self.btn_add.grid(row = 6, column = 0,
                          sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Clear", font = BUTTON_FONT)
        self.btn_add.grid(row = 6, column = 1,
                          sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Submit", font = BUTTON_FONT)
        self.btn_add.grid(row = 6, column = 2,
                          sticky = "news")
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()    
       
       


class Add(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Add Game",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, columnspan = 4, sticky ="news")
        #Genre entrybox
        self.lbl_search_by = tk.Label(self, text = "Genre: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 1, column = 1)
        #Title entrybox
        self.lbl_search_by = tk.Label(self, text = "Title: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 2, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 2, column = 1)
        #Decoloper entrybox
        self.lbl_search_by = tk.Label(self, text = "Devoloper: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 3, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 3, column = 1)  
        #Publisher entrybox
        self.lbl_search_by = tk.Label(self, text = "Publisher: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 4, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 4, column = 1)  
        #Year entrybox
        self.lbl_search_by = tk.Label(self, text = "Year: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 5, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 5, column = 1)
        #Notes Scrolled text box
        self.lbl_search_by = tk.Label(self, text = "Notes: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 6, column = 0, sticky ="news")                
        self.results = ScrolledText(self, height = 8, width = 40)
        self.results.grid(row = 7, columnspan = 3)
        #Cancel Reset Remove Buttons
        self.btn_add = tk.Button(self, text = "Cancel", font = BUTTON_FONT,
                                 command = self.go_main)
        self.btn_add.grid(row = 9, column = 0, sticky ="news")
        self.btn_add = tk.Button(self, text = "Reset", font = BUTTON_FONT)
        self.btn_add.grid(row = 9, column = 1, sticky ="news")
        self.btn_add = tk.Button(self, text = "Confirm", font = BUTTON_FONT)
        self.btn_add.grid(row = 9, column = 2, sticky ="news")        
       
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
        self.grid_columnconfigure(5, weight = 1)
        self.grid_columnconfigure(6, weight = 1)
        self.grid_columnconfigure(7, weight = 1)
        self.grid_columnconfigure(8, weight = 1)
        self.grid_columnconfigure(9, weight = 1)
        self.grid_columnconfigure(10, weight = 1)
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()    
       
       
       
'''class Save(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)    
        self.lbl_file_saved = tk.Label(self, text = "File Saved",
                                 font = BUTTON_FONT)
        self.lbl_file_saved.grid(row = 0, column = 0,
                                sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Ok", font = BUTTON_FONT,
                                command = self.go_main)
        self.btn_ok.grid(row = 1, column = 0,
                          sticky = "news")
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()    '''

class Remove(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        self.lbl_remove = tk.Label(self, text = "Which Game do You Want to Remove",
                                 font = BUTTON_FONT)
        self.lbl_remove.grid(row = 0, columnspan = 2,
                                sticky = "news")
       
        options = ["Halo3", "Halo2", "GTA 5"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self, self.tkvar, *options)
        self.menu.grid(row = 1, columnspan = 2,
                       sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Cancel", font = BUTTON_FONT,
                                command = self.go_main)
        self.btn_ok.grid(row = 2, column = 0,
                          sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Remove", font = BUTTON_FONT,
                                command = self.go_remove_two)
        self.btn_ok.grid(row = 2, column = 1,
                          sticky = "news")
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        self.parent.destroy()
       
    def go_remove_two(self):
        Screen.current = 3
        Screen.switch_frame()    
        self.parent.destroy()
       
       

class RemoveTwo(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_remove = tk.Label(self, text = "These Games are Marked for Removal",
                                 font = BUTTON_FONT)
        self.lbl_remove.grid(row = 0, columnspan = 3,
                                sticky = "news")
       
        self.results = ScrolledText(self, height = '8', width = '40')
        self.results.grid(row = 6, columnspan = 3,
                          sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Main Menu", font = BUTTON_FONT,
                                command = self.go_main)
        self.btn_ok.grid(row = 7, column = 0,
                          sticky = "news")
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()    

       
'''class OptFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        options = ["One", "Two", "Three", "Four", "Five", "Six"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self, self.tkvar, *options)
        self.menu.grid(row = 0, column = 0)'''

class EditGame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
       
        self.lbl_remove = tk.Label(self, text = "Which Game do You Want to Edit",
                                 font = BUTTON_FONT)
        self.lbl_remove.grid(row = 0, columnspan = 2,
                                sticky = "news")
       
        options = ["Halo3", "Halo2", "GTA 5"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self, self.tkvar, *options)
        self.menu.grid(row = 1, columnspan = 2,
                       sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Cancel", font = BUTTON_FONT,
                                command = self.go_main)
        self.btn_ok.grid(row = 2, column = 0,
                          sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Ok", font = BUTTON_FONT,
                                command = self.go_edit_two)
        self.btn_ok.grid(row = 2, column = 1,
                          sticky = "news")
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        self.parent.destroy()
       
    def go_edit_two(self):
        Screen.current = 3
        Screen.switch_frame()
        self.parent.destroy()
   
class EditTwo(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Edit Game",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, columnspan = 4, sticky ="news")
        #Genre entrybox
        self.lbl_search_by = tk.Label(self, text = "Genre: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 1, column = 1)
        #Title entrybox
        self.lbl_search_by = tk.Label(self, text = "Title: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 2, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 2, column = 1)
        #Decoloper entrybox
        self.lbl_search_by = tk.Label(self, text = "Devoloper: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 3, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 3, column = 1)  
        #Publisher entrybox
        self.lbl_search_by = tk.Label(self, text = "Publisher: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 4, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 4, column = 1)  
        #Year entrybox
        self.lbl_search_by = tk.Label(self, text = "Year: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 5, column = 0, sticky ="news")        
        self.entry = tk.Entry (self)
        self.entry.grid(row = 5, column = 1)
        #Notes Scrolled text box
        self.lbl_search_by = tk.Label(self, text = "Notes: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 6, column = 0, sticky ="news")                
        self.results = ScrolledText(self, height = 8, width = 40)
        self.results.grid(row = 7, columnspan = 3)
        #Cancel Reset Remove Buttons
        self.btn_add = tk.Button(self, text = "Cancel", font = BUTTON_FONT,
                                 command = self.go_edit)
        self.btn_add.grid(row = 9, column = 0, sticky ="news")
        self.btn_add = tk.Button(self, text = "Reset", font = BUTTON_FONT)
        self.btn_add.grid(row = 9, column = 1, sticky ="news")
        self.btn_add = tk.Button(self, text = "Confirm", font = BUTTON_FONT)
        self.btn_add.grid(row = 9, column = 2, sticky ="news")        
       
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
        self.grid_columnconfigure(5, weight = 1)
        self.grid_columnconfigure(6, weight = 1)
        self.grid_columnconfigure(7, weight = 1)
        self.grid_columnconfigure(8, weight = 1)
        self.grid_columnconfigure(9, weight = 1)
        self.grid_columnconfigure(10, weight = 1)

    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        frm_edit_list = EditGame1(pop_up)
        frm_edit_list.grid(row = 0, column = 0)    

##MAIN
if __name__ == "__main__":
    data_file = open("game_lib.pickle", "rb")
    games = pickle.load(data_file)
   
    data_file.close()
    root = tk.Tk()
    root.title("Game_Lib")
    root.geometry("700x500")
    screens = [MainMenu(), Add(), EditTwo(), RemoveTwo(),
                SearchGame()]
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
   
    screens[0].tkraise()
    '''main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0,
                   sticky = "news")
   
    add_game = Add()
    add_game.grid(row = 0, column = 0,
                   sticky = "news")
       
    edit_game_1 = EditGame1()
    edit_game_1.grid(row = 0, column = 0,
                   sticky = "news")
       
    edit_two = EditTwo()
    edit_two.grid(row = 0, column = 0,
                   sticky = "news")
   
    remove_game = Remove()
    remove_game.grid(row = 0, column = 0,
                   sticky = "news")
   
    remove_two = RemoveTwo()
    remove_two.grid(row = 0, column = 0,
                   sticky = "news")
   
    save = Save()
    save.grid(row = 0, column = 0,
                   sticky = "news")
   
    search_game = SearchGame()
    search_game.grid(row = 0, column = 0,
                   sticky = "news")
   
    screen = Screen()
    screen.grid(row = 0, column = 0,
                   sticky = "news")
   
    add_game.tkraise()'''
    root.grid_columnconfigure(0, weight = 1)
       

    root.mainloop()