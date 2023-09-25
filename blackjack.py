import random
import time
import os
import sys

class Card:

    #flavour
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    #values with none so values accurately match up with list placement
    values = [None, None, "2", "3", "4", "5", "6",\
        "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.v = v
        self.value = v
        self.s = s

        #seperate values to calculate 10-king as just 10, and ace to 11
        if(self.value >10 and self.value <= 13):
            self.value = 10
        elif(self.value == 14):
            self.value = 11

    #return string to print card value and suit
    def cardValue(self):
        v = self.values[self.v] + " of " + self.suits[self.s]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        
        #shuffle deck after init loop
        random.shuffle(self.cards)

    #pop card from stack and return to variable
    def removeCard(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
    

# playerclass to track cards, wins and also reset
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.wins = 0
        self.blackjacks = 0
        self.cardTotal = 0

        #card counter at one, equivalent to "2" as counting from zero
        self.cardCounter = 1

    def resetTotal(self):
        self.cardTotal = 0
        self.cards = []
        self.cardCounter = 1
    
    #append to self card list
    def appendCard(self, card):
        self.cards.append(card)

        

class Game:
    def __init__(self, computer, player):
        self.player = player
        self.computer = computer

        self.deck = Deck()

    def gameloop(self):
        while(1):
            playerInput = ""
            playerOptions = ["stand", "hit"]
            playerReplay = ["y", "n"]
            
            # variable for tracking if you've already seen dealer cards this loop, reset every game loop.
            dealercards = 0

            #computer draw
            c1c = self.deck.removeCard()
            self.computer.appendCard(c1c)
            c1c = self.deck.removeCard()
            self.computer.appendCard(c1c)


            #player draw
            p1c = self.deck.removeCard()
            self.player.appendCard(p1c)

            p1c = self.deck.removeCard()
            self.player.appendCard(p1c)

            # take numerical value from player card and add it as to calculate bust/ blackjack
            self.player.cardTotal += self.player.cards[0].value
            self.player.cardTotal += self.player.cards[1].value

            # same process but for computer calculation after players turn is over
            self.computer.cardTotal += self.computer.cards[0].value
            self.computer.cardTotal += self.computer.cards[1].value



            print("Drawing cards...")
            time.sleep(0.4)
            print("Dealers first card : {}".format(self.computer.cards[0].cardValue()))

            #printing players cards
            print("\n\n your cards: {} and {}, a total of {}".format(self.player.cards[0].cardValue(), \
            self.player.cards[1].cardValue(), self.player.cardTotal))

            

            # blackjack scenario
            if(self.player.cardTotal == 21):
                print("Blackjack!")
                print("Dealer's turn...")
                time.sleep(0.4)
                self.player.blackjacks += 1
                #dealers turn

                print("dealer's cards: {} and {}".format(self.computer.cards[0].cardValue(), \
                self.computer.cards[1].cardValue()))


                #if blackjack
                if(self.computer.cardTotal == 21):
                    print("Unlucky! the dealer also rolled blackjack..")
                    self.computer.blackjacks += 1
                    break

                # if not blackjack, loop
                while(1):

                    #dealer draw
                    if(self.computer.cardTotal <= 16):
                        c1c = self.deck.removeCard()
                        self.computer.cards.append(c1c)
                        self.computer.cardCounter += 1
                        self.computer.cardTotal += self.computer.cards[self.computer.cardCounter].value
                        print("The dealer drew another card!")
                        print("He drew {}".format(self.computer.cards[self.computer.cardCounter].cardValue()))
                    
                    # if over draw limit must stand below 21 and over 16
                    elif(self.computer.cardTotal >= 16 and self.computer.cardTotal <=21):
                        if(self.computer.cardTotal == 21):
                            print("Unlucky, the dealer managed to get up to 21!")
                            break
                        
                        else:
                            print("You win this round! the dealer rolled a total of: {}".format(self.computer.cardTotal))
                            self.player.wins += 1
                            break
                    
                    elif(self.computer.cardTotal > 21):
                        print("Dealer went bust with {}! You win!".format(self.computer.cardTotal))
                        self.player.wins += 1
                        break

            else:
                while(1):
                    while(playerInput not in playerOptions):
                        playerInput = str(input("Enter your option (Stand/Hit) : "))
                        playerInput = playerInput.lower()

                    if(playerInput == "stand"):
                        time.sleep(0.4)
                        if(not dealercards):

                            # print full hand so you can see what you're up against
                            print("\n\nDealers full hand: {} and {} ".format(self.computer.cards[0].cardValue(), self.computer.cards[1].cardValue()))
                            print("\nThe Dealer's total is: {}".format(self.computer.cardTotal))
                            dealercards = 1
                            time.sleep(0.4)

                        #dealer draw
                        if(self.computer.cardTotal <= 16):
                            c1c = self.deck.removeCard()
                            self.computer.cards.append(c1c)
                            self.computer.cardCounter += 1
                            self.computer.cardTotal += self.computer.cards[self.computer.cardCounter].value
                            print("The dealer drew another card!")
                            print("He drew {}".format(self.computer.cards[self.computer.cardCounter].cardValue()))
                            print("His total is {}\n".format(self.computer.cardTotal))
                            time.sleep(0.8)
                        
                        # if over draw limit must stand below 21 and over 16
                        elif(self.computer.cardTotal >= 16 and self.computer.cardTotal <=21):

                            # comparing totals
                            if(self.computer.cardTotal > self.player.cardTotal):
                                print("Unlucky, the dealer managed to get higher than you with {}!".format(self.computer.cardTotal))
                                self.computer.wins += 1
                                time.sleep(0.4)
                                break
                            
                            # draw edge case
                            elif(self.computer.cardTotal == self.player.cardTotal):
                                print("A draw! you both had a total card value of {}".format(self.player.cardTotal))
                                time.sleep(0.4)
                                break
                            else:
                                print("You win this round! the dealer rolled a total of: {}, you had {}".format(self.computer.cardTotal,\
                                self.player.cardTotal))
                                self.player.wins += 1
                                time.sleep(0.4)
                                break
                        
                        # bust scenario
                        elif(self.computer.cardTotal > 21):
                            print("Dealer went bust with {}! You win!".format(self.computer.cardTotal))
                            self.player.wins += 1
                            break
                    
                    elif(playerInput == "hit"):
                        p1c = self.deck.removeCard()
                        self.player.appendCard(p1c)
                        self.player.cardCounter +=1
                        self.player.cardTotal += self.player.cards[self.player.cardCounter].value
                        print("You drew : {} with a new total of {}".format(self.player.cards[self.player.cardCounter].cardValue(),\
                        self.player.cardTotal))
                        time.sleep(0.4)

                        # bust scenario
                        if(self.player.cardTotal > 21):
                            print("You bust! unlucky...")
                            self.computer.wins += 1
                            time.sleep(0.4)
                            break
                        
                        # if 21 automatically stand after hitting 21
                        if(self.player.cardTotal == 21):
                            print("You hit a total of 21! Dealers turn...")
                            playerInput = "stand"
                            time.sleep(0.4)
                        
                        else:
                            playerInput = ""
                            



            #input loop for valid input to restart
            while(playerInput not in playerReplay):
                    playerInput = str(input("Play again? (Y/N): "))
                    playerInput = playerInput.lower()
            
            if(playerInput == "y"):

                # reset
                dealercards = 0
                self.deck = Deck()
                self.player.resetTotal()
                self.computer.resetTotal()
                print("...")
                time.sleep(0.4)

            elif(playerInput == "n"):
                print("You won {} time(s) against the computer's {} time(s)".format(self.player.wins, self.computer.wins))
                print("You had blackjack {} time(s)!".format(self.player.blackjacks))
                print("Exiting game... 3...")
                time.sleep(0.4)
                print("2...")
                time.sleep(0.4)
                print("1...")
                time.sleep(0.4)
                sys.exit()


            
            



# gameloop code

# clear screen for better gameplay
if os.name.lower() == "windows":
    os.system("cls")
else:
    os.system("clear")

cp = Player("cp")
playername = str(input("Enter name: "))
p1 = Player(playername)

gameloop = Game(cp, p1)

gameloop.gameloop()