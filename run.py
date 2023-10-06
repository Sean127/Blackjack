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


def total(player_hand, dealer_hand):
    ''' Calculate hand total'''
    player_total = 0
    dealer_total = 0

    for card in player_hand:
        if card in ['Jack', 'Queen', 'King']:
            player_total += 10
        elif card == 'Ace':
            player_total += 11
        else:
            player_total += card

    for card in dealer_hand:
        if card in ['Jack', 'Queen', 'King']:
            dealer_total += 10
        elif card == 'Ace':
            dealer_total += 11
        else:
            dealer_total += card

    return player_total, dealer_total


def hit(player_hand):
    ''' Add ability to "hit" the dealer '''
    card = deck.pop()
    player_hand.append(card)
    return player_hand