import Single_Deck
import time

deck = Single_Deck.normal_deck()

start_time = time.time()

for i in range(53):
    print(deck.drawCard())

print(time.time() - start_time)