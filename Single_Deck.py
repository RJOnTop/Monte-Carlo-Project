import random

suit_template = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
deck = [suit_template.copy(), suit_template.copy(), suit_template.copy(), suit_template.copy()]

class normal_deck:
    def __init__(self):
        self.amount = 52
        self.tempDeck = deck.copy()
    
    def draw_card_single(self):
        # If there are no more cards in the deck, this function will return -1 for the main driver to handle with the shuffle_cards function
        if self.amount <= 0:
            return -1
        else:
            self.amount = self.amount - 1
        # Keep choosing a random suit until one with cards is found
        while True:
            suit = random.randint(0, len(self.tempDeck) - 1)
            if len(self.tempDeck[suit]) > 0:
                break
        # length_of_suit is just the side of the chosen suit which should have 1 or more cards. I'm using this variable for readability where the card is defined
        length_of_suit = len(self.tempDeck[suit]) - 1
        card = self.tempDeck[suit].pop(random.randint(0, length_of_suit))
        
        return card
    
    # This function is used to refill the deck with the deck defined above the class
    def shuffle_cards(self):
        self.tempDeck = deck.copy()
        