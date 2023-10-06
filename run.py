import random

deck = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']*4


def deal_player_hands(deck):
    ''' Creates Players hand '''
    player_hand = []

    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        player_hand.append(card)
    return player_hand


def deal_dealer_hand(deck):
    ''' Creates Dealers hand '''
    dealer_hand = []

    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        dealer_hand.append(card)
    return dealer_hand


