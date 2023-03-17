import random

#        2, 3, 4, 5, 6, 7, 8, 9, 10, J,  Q,  K,  A
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

class Infinite_Deck:
    def __init__(self):
        self.deck = cards.copy()

    def draw_card(self):
        
        if len(self.deck) == 0:     # Once the deck is empty this re-shuffles a brand new one
            self.deck = cards.copy()

        
        card = random.choice(self.deck)     # Random card is taken

        
        self.deck.remove(card)    # Proceeds to remove that card

        return card


deck = Infinite_Deck()    # Assigns class to a variable

# Takes a range of cards and prints
for i in range(20):
    card = deck.draw_card()
    print("Card Taken:", card)

# This is an infinite version that continuously prints just put the range above in comments 
'''
while True:
    card = deck.draw_card()
    print("Card taken:", card)
'''
