import sys
import os
import random
import time

random.seed()

class Game:
    def __init__(self, p1, cp):
        self.p1 = p1
        self.cp = cp
        
        


    def rps(self):
        print("Ready? Rock...")
        time.sleep(0.4)
        print("Paper...")
        time.sleep(0.4)
        print("Scissors!")
        time.sleep(0.4)

        #change it to length of choice and minus them, as they're all unique you'll always get the
        #results below
        length = len(self.p1.choice) - len(self.cp.choice)    

        match length:
            case -4:
                print("{} Wins with {} against {}".format(self.p1.name, self.p1.choice, \
                    
                self.cp.choice))
                self.p1.wins += 1
            case 1:
                print("{} Wins with {} against {}".format(self.p1.name, self.p1.choice, \
                    
                self.cp.choice))
                self.p1.wins += 1
            case 3:
                print("{} Wins with {} against {}".format(self.p1.name, self.p1.choice, \
                    
                self.cp.choice))
                self.p1.wins += 1
            case -1:
                print("{} Wins with {} against {}".format(self.cp.name, self.cp.choice, \
                    
                self.p1.choice))
                self.cp.wins += 1

            case -3:
                print("{} Wins with {} against {}".format(self.cp.name, self.cp.choice, \
                    
                self.p1.choice))
                self.cp.wins += 1
            case 4:
                print("{} Wins with {} against {}".format(self.cp.name, self.cp.choice, \
                    
                self.p1.choice))
                self.cp.wins += 1

            case 0:
                print("Draw! you both used {}!".format(self.p1.choice))
                self.p1.draws +=1
                self.cp.draws +=1

    def endgame(self):
        if self.p1.wins > self.cp.wins:
            print("{} Wins with {} rounds!".format(self.p1.name, self.p1.wins))
        elif self.p1.wins < self.cp.wins:
            print("{} Wins with {} rounds!".format(self.cp.name, self.cp.wins))
        else:
            print("It's a tie! you both had {} wins!".format(self.p1.wins))

        print("Exiting game...")
        time.sleep(0.4)
        print("3...")
        time.sleep(0.4)
        print("2...")
        time.sleep(0.4)
        print("1...")
        time.sleep(0.4)

        sys.exit()


    def playagain(self):
        play = ""
        while(1):

            play = str(input("Play again? (Y/N): "))

            match play.lower():
                case "y":
                    print("Loading...")
                    time.sleep(0.4)
                    break
                case "n":
                    print("Thanks for playing! \n")
                    self.endgame()
                case _:
                    print("Invalid input, please input Y or N")

    
    
class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.draws = 0
        self.choice = ""
        self.options = ["rock", "paper", "scissors"]

    def choose(self):
        while(self.choice.lower() not in self.options):
            self.choice = str(input("Enter choice: "))
            if self.choice.lower() not in self.options:
                print("Invalid input, Please input rock,  paper or scissors")
            
        self.choice = self.choice.lower()
    
    def computerchoose(self):
        i = random.randint(0, 2)
        self.choice = self.options[i]


# runtime code starts here
if os.name.lower() == "windows":
    os.system("cls")
else:
    os.system("clear")

computer = Player("computer")
playername = str(input("Enter name: "))
p1 = Player(playername)

activegame = Game(p1, computer)

while(1):
    activegame.p1.choose()
    activegame.cp.computerchoose()

    activegame.rps()


    if activegame.p1.wins >= 3:
        activegame.endgame()
    elif activegame.cp.wins >= 3:
        activegame.endgame()

    
    activegame.playagain()
    activegame.p1.choice = ""


