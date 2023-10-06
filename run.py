import random

deck = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']*4


def deal_hands(deck):
    ''' Creates hands for player and dealer '''
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand


def total(hand):
    ''' Calculate hand total'''
    total = 0

    for card in hand:
        if card in ['Jack', 'Queen', 'King']:
            total += 10
        elif card == 'Ace':
            total += 11
        else:
            total += card

    return hand


def hit(hand):
    ''' Add ability to "hit" the dealer '''
    card = deck.pop()
    hand.append(card)
    return hand


def game():
    hand = deal_hands(deck)
    play = False
    
    print("Welcome to Blackjack!")
    print("To win get closer to 21 than the dealer")
    print("Go over however, and you lose!")

    while play is False:
       
        start = input('Type "enter" to begin or "quit" to quit').lower()
        if start == "enter":
            print(hand)
            

def main():
    game()


main()