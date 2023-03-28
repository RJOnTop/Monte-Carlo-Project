# Monte Carlo: BlackJack
# CSCI 154


import random
from collections import deque

# Function to draw a card from an infinite deck
def draw_card_infinite():
    card = random.randint(1, 13)
    return min(card, 10)

# Function to check if a hand has an Ace
def soft(hand):
    return 1 in hand and sum(hand) + 10 <= 21

# Function to calculate the value of a hand
def hand_value(hand):
    if soft(hand):
        return sum(hand) + 10
    return sum(hand)

# Policy 1: If your hand ≥ 17, stick. Else hit.
def policy1(hand):
    return hand_value(hand) < 17

# Policy 2: If your hand ≥ 17 and is hard, stick. Else hit unless your hand = 21
def policy2(hand):
    return (hand_value(hand) < 17 and not soft(hand)) or hand_value(hand) == 21

# Policy 3: Always stick
def policy3(hand):
    return False

# Function to create a single deck of cards
def create_single_deck():
    deck = [min(card, 10) for _ in range(4) for card in range(1, 14)]
    random.shuffle(deck)
    return deque(deck)

def draw_card_single(deck):
    return deck.popleft()

# Function to simulate Blackjack of policy and deck type
def play_game(policy, infinite_deck=False, single_deck=False):
    if single_deck:
        deck = create_single_deck()
        draw_card = lambda: draw_card_single(deck)
    else:
        draw_card = draw_card_infinite if infinite_deck else draw_card_infinite


    hand = [draw_card(), draw_card()]
    d_hand = [draw_card(), draw_card()]

    # Player's turn
    while policy(hand):
        hand.append(draw_card())

    # Dealer's turn
    while hand_value(d_hand) < 17:
        d_hand.append(draw_card())


    player_final = hand_value(hand)
    d_final = hand_value(d_hand)


    if player_final > 21:
        return -1
    elif d_final > 21:
        return 1
    elif player_final > d_final:
        return 1
    if player_final > 21:
        return -1
    elif d_final > 21:
        return 1
    elif player_final > d_final:
        return 1
    elif player_final == d_final:
        return 0
    else:
        return -1

def policyinfinite(hand):
    return hand_value(hand) < 17

def policysingle(hand):
    return hand_value(hand) < 17

# Function to run Monte Carlo simulations for the given policy and deck type
def run_monte_carlo(policy, infinite_deck=False, single_deck=False, num_simulations=100000):
    dealer_wins = 0
    player_wins = 0
    draws = 0

    for _ in range(num_simulations):
        result = play_game(policy, infinite_deck, single_deck)
        if result == -1:
            dealer_wins += 1
        elif result == 1:
            player_wins += 1
        else:
            draws += 1

    return dealer_wins, player_wins, draws

# To ouput policy, 1, 2, and 3
if __name__ == "__main__":
    policies = [policy1, policy2, policy3]
    for i, policy in enumerate(policies, 1):
        dealer_wins, player_wins, draws = run_monte_carlo(policy, num_simulations=100000)
        winning_probability = player_wins / (dealer_wins + player_wins + draws) * 100
        print(f"Policy {i}: Player Winning Probability = {winning_probability}%")
        print(f"Dealer wins: {dealer_wins}, Player wins: {player_wins}, Draws: {draws}\n")

    # Infinite deck
    dealer_wins, player_wins, draws = run_monte_carlo(policyinfinite, infinite_deck=True, num_simulations=100000)
    winning_probability = player_wins / (dealer_wins + player_wins + draws) * 100
    print(f"Infinite Deck: Player Winning Probability = {winning_probability}%")
    print(f"Dealer wins: {dealer_wins}, Player wins: {player_wins}, Draws: {draws}\n")

    # Single deck
    dealer_wins, player_wins, draws = run_monte_carlo(policysingle, single_deck=True, num_simulations=100000)
    winning_probability = player_wins / (dealer_wins + player_wins + draws) * 100
    print(f"Single Deck: Player Winning Probability = {winning_probability}%")
    print(f"Dealer wins: {dealer_wins}, Player wins: {player_wins}, Draws: {draws}\n")
