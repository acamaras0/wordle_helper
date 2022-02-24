from game_data import GameData
from cli import WordleCli

game_data = GameData()
interface = WordleCli(game_data)
count = 6
mode = None

while mode not in ["AI", "me"]:
    mode = input("Would you like to play the game yourself or let AI decide?(me/AI)")
if mode == "AI":
    print("Well too bad, because that isn't implemented yet")
print("\n")

victory = False
while count > 0 and not victory:
    victory = interface.ask_for_guess()
    if victory:
        break
    interface.get_wordle_result()
    print("\n")
    

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

"""
MANUALLY TESTED:

1. Green ones work
2. Yellow ones work
3. 

"""