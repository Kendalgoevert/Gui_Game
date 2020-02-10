#usr/bin/python3
#KEndal Goevert
#1-28-2020

import pickle
games = {1:['FPS', 'Halo3', 'Bungee','microsoft','xbox360','2007','10','either','30.00','yes','1/15/2008','This game blows chunks']}

data_file = open("game_library", "wb")
pickle.dump(games, data_file)
data_file.close()