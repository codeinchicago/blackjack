"""
Your task, should you choose to accept, will be to create a blackjack program using Jupyter Notebook and Object Oriented Principles. I have provided a starter notebook for you that describes the rules of the game. 


This project will be completed individually, but feel free to share ideas with your fellow students.

Once completed, commit the project to github and submit the link to this assignment.
"""


import random

# X Make Cards
#Implement drawing cards, adding up their value. Be careful of Ace, can be 1 or 11.
#   Need to work on order: deck must be first shuffled, then card drawn, then card evaluated.
#Implement busting, winning, adding player totals
#Add player and humans

#Thanks to Brian Stanton for this code.
class Card:
    def __init__(self):
        self.deck = []

    def shuffle_deck(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [(value, suit) for value in values for suit in suits]

        random.shuffle(self.deck)
        print(self.deck)
        return self.deck
    def draw_card(self):
        draw = self.deck.pop()
        print(draw)
        #print(type(draw))
        return draw
    def card_value(self):
        evaluated = self.draw_card()
        if evaluated[0] in {'Jack', 'Queen', 'King', 'Ace'}:
            print('Not a number, need to edit.')
        else:
            print(evaluated[0])
        return evaluated

def get_card():
    my_card = Card()
    my_card.shuffle_deck()
    my_card.draw_card()
    my_card.card_value()


get_card()