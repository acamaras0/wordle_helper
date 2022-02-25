from game_data import GameData
from cli import WordleCli
from gui import WordleGui

game_data = GameData()
interface = WordleGui(game_data)
interface.play() #commented for testing to get GUI faster
#choice_of_interface = ""
# while choice_of_interface != "0":
#     choice_of_interface = ""
#     choice_of_interface = input("Would you like a GUI? (yes/no)")
#     if choice_of_interface == "no":
#         interface = WordleCli(game_data)
#         interface.play()
#     elif choice_of_interface == "yes":
#         interface = WordleGui(game_data)
#         interface.play()
#         exit()
#     elif choice_of_interface != "0":
#         print("Answer yes or no. (0 to quit)")

"""
 _________________________________________
/ It's wonderful that you have decided to \ 
\ code a beautiful program.               /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
"""""""""""""""""""""""""""""""""""""""""""""
