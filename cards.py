"""
Your task, should you choose to accept, will be to create a blackjack program using Jupyter Notebook and Object Oriented Principles. I have provided a starter notebook for you that describes the rules of the game. 


This project will be completed individually, but feel free to share ideas with your fellow students.

Once completed, commit the project to github and submit the link to this assignment.
"""

#To do list
# X Make Cards
# X Implement drawing cards, adding up their value. 
#Be careful of Ace, can be 1 or 11.
#   Need to work on order: deck must be first shuffled, then card drawn, then card evaluated.
#Implement busting, winning, adding player totals
#Track amount of money.
#Add player and humans
#For implementation, shuffle deck before anything else.

#Thanks to Brian Stanton for code on the deck.
#Thanks to Stack Overflow for how to take a variable from one class into another.

import random

class Card:

    def __init__(self):
        # self.card = "Ace of Spades"
        self.deck = []
    def shuffle_deck(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [(value, suit) for value in values for suit in suits]
        random.shuffle(self.deck)
        # print(self.deck)
        return self.deck
    
    def draw_card(self):
        self.draw = self.deck.pop()
        #print(f'Your card is the {self.draw[0]} of {self.draw[1]}.')
        #print(type(draw))
        return self.draw



class Human(Card):
    def __init__(self):
        self.hand = []
        self.shuffled = False
    def get_deck(self):
        print(self.deck)
        return self.deck

    def grab_card(self):
        #print('At start: ', self.shuffled)
        if self.shuffled == False:
            self.shuffle_deck()
            self.shuffled = True
        #print(self.deck)
        newcard = self.draw_card()
        self.hand.append(newcard)
        #print(self.hand)
        #print(self.hand[0][0])
        #print('At end: ', self.shuffled)

    def show_hand(self):
        print(self.hand)
    
    #Need to loop through the first item of every item in the list, adding up their totals.
    def card_value(self):
        self.value = 0
        for i in range(len(self.hand)):
            if self.hand[i][0] in {'Jack', 'Queen', 'King'}:
                self.value += 10
            elif self.hand[i][0] == "Ace":
                self.value += 11
            else:
                self.value += int(self.hand[i][0])
        print(self.value)
        #Busting
        if self.value > 21:
            print("You bust.")
            bust = True
        return self.value

    def initial_draw(self):
        self.grab_card()
        self.grab_card()
        print(self.hand)
        self.card_value()

#Make two players, compare their values.

class Player(Human):
    def __init__(self):
        self.cash = 1000
        self.hand = []
        self.shuffled = False

    def gamble(self):
        hand1 = self.grab_card()
        print(hand1)
#Initialize players

#Get them cards

#Compare a winner

class Dealer(Human):
    def __init__(self):
        self.hand = []
        self.shuffled = False
    
    def reveal_card(self):
        self.grab_card()

    

        

my_card = Card()

my_human = Human()

my_player = Player()
my_player.initial_draw()
my_dealer = Dealer()
my_dealer.initial_draw()
#Winning check.
if my_player.value > my_dealer.value:
    print("You win.")