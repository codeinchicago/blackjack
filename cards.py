"""
Your task, should you choose to accept, will be to create a blackjack program using Jupyter Notebook and Object Oriented Principles. I have provided a starter notebook for you that describes the rules of the game. 


This project will be completed individually, but feel free to share ideas with your fellow students.

Once completed, commit the project to github and submit the link to this assignment.
"""

#To do list

#Thanks to Brian Stanton for code on the deck.
#Thanks to Stack Overflow for how to take a variable from one class into another.

import random

class Card:

    def __init__(self):
        # self.card = "Ace of Spades"
        self.hand = []
        self.shuffled = False
        self.bust = False
        self.deck = []
        self.dscore = 0
        self.pscore = 0
        self.dhand =[]
        self.money = 1000
        self.bet = 0
        
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
    def get_deck(self):
        print(self.deck)
        return self.deck

    def dealer_card(self):
        self.shuffle_deck()
        dcard = self.deck.pop()
        print(dcard)
        self.dhand.append(dcard)
        self.card_value(self.dhand)
        self.dscore = self.value
        print("Dealer score is:", self.dscore)


    def grab_card(self):
        newcard = self.draw_card()
        self.hand.append(newcard)

    def show_hand(self):
        print(self.hand)
        
    
    def card_value(self, hand):
        self.value = 0
        for i in range(len(hand)):
            if hand[i][0] in {'Jack', 'Queen', 'King'}:
                self.value += 10
            elif hand[i][0] == "Ace":
                self.value += 11
            else:
                self.value += int(hand[i][0])
        print(self.value)
        #Busting
        return self.value

    def show_value(self):
        print(f"Hand value is {self.value}.")



    def initial_draw(self):
        self.bet = int(input('Howdy, how much would you like to bet? '))     
        self.dealer_card()
        self.grab_card()
        self.grab_card()
        print("This is your hand.")
        print(self.hand)
        self.card_value(self.hand)
        self.show_value()
        self.pscore = self.value

        #Blackjack
        if self.pscore == 21:
            print("Blackjack!")
            self.money += self.bet

        morecard = True
        while morecard == True:
            cardcheck = input("Would you like another card? ")
            if cardcheck == 'y':
                self.grab_card()
                print(self.hand)
                self.card_value(self.hand)
                #print('This is cardcheck - y.')
                self.show_value()
                self.pscore = self.value
                if self.pscore > 21:
                    print('You bust.')
                    self.money -= self.bet
                    print(f'You now have ${self.money}.')

            elif cardcheck == 'n':                
                print(self.value)
                morecard == False
                #print('This is cardcheck - n')
                break
        print("Dealer score is: ", self.dscore)
        while self.dscore < 17:
            dcard = self.deck.pop()
            print(f'The {dcard}')
            self.dhand.append(dcard)
            self.card_value(self.dhand)
            print(f'Total dealer card value is: {self.value}')
            
            self.dscore = self.value

            if self.dscore > 21:
                print("Dealer busts.")
                
                
                #Give player money
                break
        if self.pscore > self.dscore:
            print("Player wins.")
            self.money += self.bet
            print('You have ', self.money)
        elif self.pscore == self.dscore:
            print("Draw.")
        else:
            print("Dealer wins.")
            self.money -= self.bet
            print('You have ', self.money)
        
def gamble():
    playing = True
    while playing == True:
        Human().initial_draw()
        playagain = input("Would you like to play again? ")
        if playagain == 'n':
            playing = False

gamble()
