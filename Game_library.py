#!/usr/bin/python3
#Kendal Goevert
#1-27-2020


import pickle

'''This is a game library to hold all the Data to your games'''

#data_file = open("game_library", "rb")
#games = pickle.load(data_file)
#data_file.close()

         



def add_game():
    #print("running add_game()")
    new_key = len(games)+1
    new_entry = []
    valid = False
    while not valid:
        title = input("What is the Title of the game to add? ")
        
        genre = input("   What is the genre? ")
        new_entry.append(genre)
        title = input("   What is the title? ")
        new_entry.append(title)
        developer = input("   Who is the developer? ")
        new_entry.append(developer)
        publisher = input("   Who is the publisher? ")
        new_entry.append(publisher)
        platform = input("   What is the platform? ")
        new_entry.append(platform)
        year_released = input("   What is the release year? ")
        new_entry.append(year_released)
        rating = input("   What is the rating? ")
        new_entry.append(rating)
        solo_or_multiplayer = input("   Is it single or multiplayer? ")
        new_entry.append(solo_or_multiplayer)
        price = input("   What is the price? ")
        new_entry.append(price)
        have_you_played = input("   Have you played the game? ")
        new_entry.append(have_you_played)
        purchase_date = input("   What is the purchase date? ")
        new_entry.append(purchase_date)
        notes = input("   Any notes? ")
        new_entry.append(notes)
        answer = input(" Is this correct?: ")
        if answer.lower() in ("yes", "y"):
            valid = True
    games[new_key] = new_entry
    #games[title] = [genre, title, developer, publisher, platform, year_released, rating,
                       #solo_or_multiplayer, price, have_you_played, purchase_date, notes]  

def edit_game():
    #print("running edit_game()")
    print("Here is the Library: ")
    for key in games.keys():
        print(key, "-", games[key][1])
    edit_key = input("Which game do you want to change?: ")
    edit_key = len(games)+1
    edit_entry = []
    valid = False
   
    while not valid:    
        title = input("What is the Title of the game to edit? ")
        if title in games[1]:
            print("*** THAT TITLE DOES NOT EXISTS! ***\n")
        else:
            genre = input("   What is the genre? ")
            edit_entry.append(genre)
            title = input("   What is the title? ")
            edit_entry.append(title)
            developer = input("   Who is the developer? ")
            edit_entry.append(developer)
            publisher = input("   Who is the publisher? ")
            edit_entry.append(publisher)
            platform = input("   What is the platform? ")
            edit_entry.append(platform)
            year_released = input("   What is the release year? ")
            edit_entry.append(year_released)
            rating = input("   What is the rating? ")
            edit_entry.append(rating)
            solo_or_multiplayer = input("   Is it single or multiplayer? ")
            edit_entry.append(solo_or_multiplayer)
            price = input("   What is the price? ")
            edit_entry.append(price)
            have_you_played = input("   Have you played the game? ")
            edit_entry.append(have_you_played)
            purchase_date = input("   What is the purchase date? ")
            edit_entry.append(purchase_date)
            notes = input("   Any notes ")
            edit_entry.append(notes)
            answer = input(" Is this correct?: ")
            if answer.lower() in ("yes", "y"):
                valid = True
        games[new_key] = edit_entry            
            #games[title] = [genre, title, developer, publisher, platform, year_released, rating,
            #               solo_or_multiplayer, price, have_you_played, purchase_date, notes]    
def print_all():
    #print("running print_all()")
    key_list = games.keys()
       
    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Titlte: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher : ", games[key][3])
        print("Platform: ", games[key][4])
        print("Year Released: ", games[key][5])
        print("Your Rating: ", games[key][6])
        print("Solo or Multiplayer?: ", games[key][7])
        print("Price: ", games[key][8])
        print("Have You Played? : ", games[key][9])
        print("Date Baught: ", games[key][10])
        print("Notes: ", games[key][11])
        print("----------------------")
       
def search_genre():
    #print("running search_title")
    found_one = False
    name = input("  What is the genre of the Game? ")
    for key in games.keys():
        if name == games[key][0]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")    
   
def search_title():
    #print("running search_title")
    found_one = False
    name = input("  What is the title of the Game? ")
    for key in games.keys():
        if name == games[key][1]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
       
def search_developer():
    #print("running search_title")
    found_one = False
    name = input("  Who is the developer of the Game? ")
    for key in games.keys():
        if name == games[key][2]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")  

def search_publisher():
    #print("running search_title")
    found_one = False
    name = input("  Who is the publisher of the Game? ")
    for key in games.keys():
        if name == games[key][3]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
   
def search_platform():
    #print("running search_title")
    found_one = False
    name = input("  What is the platform of the Game? ")
    for key in games.keys():
        if name == games[key][4]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")  
   
def search_release_year():
    #print("running search_title")
    found_one = False
    name = input("  What is the release year of the Game? ")
    for key in games.keys():
        if name == games[key][5]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")  

def search_rating():
    #print("running search_title")
    found_one = False
    name = input("  What is the rating of the Game? ")
    for key in games.keys():
        if name == games[key][6]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")    

def search_single_multiplayer():
    #print("running search_title")
    found_one = False
    name = input("Is the game single or multiplayer? ")
    for key in games.keys():
        if name == games[key][7]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")  

def search_price():
    #print("running search_title")
    found_one = False
    name = input("  What is the price of the game? ")
    for key in games.keys():
        if name == games[key][8]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")    

def search_played():
    #print("running search_title")
    found_one = False
    name = input("  Have you played the game? :")
    for key in games.keys():
        if name == games[key][9]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")    

def search_purchase_date():
    #print("running search_by_title")
    found_one = False
    name = input("  What is the purchase date of the game? :")
    for key in games.keys():
        if name == games[key][10]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Titlte: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher : ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Your Rating: ", games[key][6])
            print("Solo or Multiplayer?: ", games[key][7])
            print("Price: ", games[key][8])
            print("Have You Played? : ", games[key][9])
            print("Date Baught: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")            
           
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")    


def remove_game():
    #print("running remove_game()")
    remove_key = None
    for key in games.keys():
        print(key, "-", games[key][1])
        print("----------------------")
  
    try:  
        remove_key = int(input("What game would you like to remove?: "))
        remove_key = int(remove_key)
        for key in range(1, len(games)+1):
            if key >= remove_key and key != len(games):
                games[key] = games[key + 1]
            if key == len(games):
                games.pop(key)
    except:
        print("INVALID")
    #if remove_key not in games:
        
        #print("*** THAT GAME DOES NOT EXIST! ***\n")
    #else:
        #entry = games.pop(remove_key)
        #print(remove_key, ":", entry[1]+", removed.")  
   
   
def save():
    #print("running save()")
    data_file = open("game_lib.pickle", "wb")
    pickle.dump(games, data_file)
    data_file.close()
    print("Game Saved")
def quit():
    #print("running quit()")
    choice = input("Would you like to save?: ")
    if choice == "yes":
        save()
    elif choice == "no":
        pickle_file = open("datafile.pickle", "wb")
        pickle.dump(games, pickle_file)
        pickle_file.close()
    else:
        print("*** NOT A VALID CHOICE ***\n")
   

   
keep_going = True


def search():
   
    print('''
       1)Genre:
       2)Title:
       3)Developer:
       4)Publisher:
       5)Platform:
       6)Year Released:
       7)Rating:
       8)Sinle/Multi player
       9)Price:
       10)Purchase Date:
       ''')
   
   
    choice = input("What would you like to search for? ")
    if choice == "Genre":
        search_genre()
    elif choice == "Title":
        search_title()
    elif choice == "Developer":
        search_developer()
    elif choice == "Publisher":
        search_publisher()
    elif choice == "Platform":
        search_platform()
    elif choice == "Year Released":
        search_release_year()
    elif choice == "Rating":
        search_rating()
    elif choice == "Single or Multiplayer":
        search_single_multiplayer()
    elif choice == "Price":
        search_price()
    elif choice == "Played":
        search_played()
    elif choice == "Purchase Date":
        search_purchase_date()
    else:
        print("*** NOT A VALID CHOICE ***\n")    


while keep_going:
    print("""
    Welcome to your game library
    ---------------------------
       
    MAIN MENU
    1) Add Game
    2) Edit Game
    3) Print All
    4) Search By Title
    5) Remove a Game
    6) Save Database
       
    Q) Quit
   
    """)

    choice = input("What would you like to do? ")
    if choice == "1":
        add_game()
    elif choice == "2":
        edit_game()
    elif choice == "3":
        print_all()
    elif choice == "4":
        search()
    elif choice == "5":
        remove_game()
    elif choice == "6":
        save()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** NOT A VALID CHOICE ***\n")
       
print("Goodbye.")

