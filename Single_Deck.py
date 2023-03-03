import random

suit_template = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
deck = [suit_template.copy(), suit_template.copy(), suit_template.copy(), suit_template.copy()]

class normal_deck:
    def __init__(self):
        self.amount = 52
        self.tempDeck = deck
    
    def drawCard(self):
        if self.amount <= 0:
            return -1
        else:
            self.amount = self.amount - 1
        
        while True:
            suit = random.randint(0, len(self.tempDeck) - 1)
            if len(self.tempDeck[suit]) > 0:
                break

        length_of_suit = len(self.tempDeck[suit]) - 1
        card = self.tempDeck[suit].pop(random.randint(0, length_of_suit))
        
        return card