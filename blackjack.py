"""
Your task, should you choose to accept, will be to create a blackjack program using Jupyter Notebook and Object Oriented Principles. I have provided a starter notebook for you that describes the rules of the game. 


This project will be completed individually, but feel free to share ideas with your fellow students.

Once completed, commit the project to github and submit the link to this assignment.
"""


import random

#Make Cards
#Implement drawing cards, adding up their value. Be careful of Ace, can be 1 or 11.
#Implement busting, winning, adding player totals
#Add player and humans

#Thanks to Brian Stanton for this code.
class Card:
    def shuffle_deck():
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        deck = [(value, suit) for value in values for suit in suits]

        random.shuffle(deck)
        print(deck)
        return deck


Card.shuffle_deck()