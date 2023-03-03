import Single_Deck
import time

deck = Single_Deck.normal_deck()

outer_test = 100000
inner_test = 60

# Method 1
print("Method 1")
start_time = time.time()

for j in range(outer_test):
    deck.shuffle_cards()
    for i in range(inner_test):
        deck.draw_card_single()

print(time.time() - start_time)


# Method 2
print("Method 2")
start_time = time.time()

for j in range(outer_test):
    deck.shuffle_cards()
    for i in range(inner_test):
        deck.draw_card_single2()

print(time.time() - start_time)

# Method 3
print("Method 3")
start_time = time.time()

for j in range(outer_test):
    deck.shuffle2()
    for i in range(inner_test):
        deck.draw_card_single3()

print(time.time() - start_time)
