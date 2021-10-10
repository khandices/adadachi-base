from constants import STATUS
import random
from constants import GAMES
from adadachi import Adadachi

class Player:
    def __init__(self):
        self.adadachi = None
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": ["banana cream pie", "carrot sticks", "mashed potatoes", "mac 'n cheese", "tater tots", "chocolate cake", "strawberries", "fried rice"],
        }
    
    def get_status(self):
        print(f"Hunger: {self.adadachi.hunger}\nHappiness: {self.adadachi.happiness}\nPoop Level: {self.adadachi.poop_lvl}")

    def play_with_adadachi(self):
        # play pet fav game happiness increase 2
        # play other game happiness increase 1
        # play pet hated game happiness decrease by 1
        answer = int(input(GAMES))
        games = self.inventory["games"]
        selection = games[answer-1]
        if selection == self.adadachi.personality["fav_game"]:
            self.adadachi.happiness += 2
        elif selection == self.adadachi.personality["hates_game"]:
            self.adadachi.happiness -= 1
        else:
            self.adadachi.happiness += 1

    def clean(self):
        # if poop level over a certian level, happiness decrease by 1 proportionate 
        pass

    def feed(self):
        # pet is fed favorite food, the hunger decrease 2 points until 0
        # poop level increase by 1
        # pet is fed favorite food happiness increase 1
        # pet fed hated food, hunger increase 1
        # if hunger reaches 5, pet dies
        # pet fed hated food, happiness decrease by 1
        # if selection == self.adadachi.personality["fav food"]:
        #     self.adadachi.hunger -= 2
        #     self.adadachi.happniess += 1
        pass
