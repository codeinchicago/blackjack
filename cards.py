"""
Your task, should you choose to accept, will be to create a blackjack program using Jupyter Notebook and Object Oriented Principles. I have provided a starter notebook for you that describes the rules of the game. 


This project will be completed individually, but feel free to share ideas with your fellow students.

Once completed, commit the project to github and submit the link to this assignment.
"""


#To do list
# X Make Cards
#Implement drawing cards, adding up their value. Be careful of Ace, can be 1 or 11.
#   Need to work on order: deck must be first shuffled, then card drawn, then card evaluated.
#Implement busting, winning, adding player totals
#Add player and humans

#Thanks to Brian Stanton for code on the deck.
#Thanks to Stack Overflow for how to take a variable from one class into another.

import random

class Card:
    def __init__(self):
        self.card = "Ace of Spades"
        self.deck = []
    def shuffle_deck(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [(value, suit) for value in values for suit in suits]
        random.shuffle(self.deck)
        #print(self.deck)
        return self.deck
    def draw_card(self):
        self.draw = self.deck.pop()
        print(f'Your card is the {self.draw[0]} of {self.draw[1]}.')
        #print(type(draw))
        return self.draw
    def card_value(self):
        evaluated = self.draw_card()
        if evaluated[0] in {'Jack', 'Queen', 'King'}:
            value = 10
        elif evaluated[0] == "Ace":
            value = 11
        else:
            value = int(evaluated[0])
        print(value)
        return value


class Human(Card):


    def grab_card(self):
        #print(self.card)
        self.shuffle_deck()
        print(self.deck)
        self.draw_card()
    
my_card = Card()
#print(my_card)
my_human = Human()
my_human.grab_card()