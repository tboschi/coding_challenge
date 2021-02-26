#! /bin/python3

import sys

from collections import Counter

# convert card face value to int value
rank = { '2' : 0, '3' : 1, '4' : 2, '5' : 3,
         '6' : 4, '7' : 5, '8' : 6, '9' : 7,
         'T' : 8, 'J' : 9, 'Q' : 10, 'K' : 11,
         'A' : 12 }

def is_flush(suits):
    """ Check if the suits (str) are of the same type """
    return suits == 5 * suits[0]

def is_straight(ranks):
    """ Check if cards are in a straight order
        assuming ranks is an already sorted list
    """
    return all(p == n + 1 for p, n in zip(ranks[:-1], (ranks[1:])))

def score(hand):
    """ Give a score to hand of 5 cards for poker
        It produces a list where the first element
        is the score from hand combination
            0 - no combo
            1 - one pair
            2 - two pairs
            3 - three of a kind
            4 - straight
            5 - flush
            6 - full
            7 - four of a kind
            8 - straight flush
        and the rest of the list is the hand of cards
        sorted by frequency and reversed value to be
        used in list to list comparison for ranking.
        As such, there is no need to assign
        a score to royal flush

    aguments:
        hand - str with 5 cards space-separated
               e.g.  "8C TS KC 9H 4S"

    return:
        list - structure explained above
    """

    # value of cards
    ranks = sorted([rank[card[0]] for card in hand], reverse=True)
    # suits of cards
    suits = ''.join(card[1] for card in hand)

    # count of unique cards
    count = Counter(ranks)
    # frequency-sorted
    ranks = sorted(ranks, key=count.get, reverse=True)
    # list of counts sorted by frequency
    count = [c[1] for c in count.most_common()]

    # order is such that more common hands are checked first
    if count[0] == 2:
        if count[1] == 2:
            value = 2   # two pairs
        else:
            value = 1   # one pair
    elif count[0] == 3:
        if count[1] == 2:
            value = 6   # full house
        else:
            value = 3   # three of a kind
    elif is_straight(ranks): 
        if is_flush(suits):
            value = 8
        else:
            value = 4
    elif is_flush(suits):
        value = 5 
    elif count[0] == 4: # four of a kind
        value = 7
    else:
        value = 0

    return [value] + ranks


if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)

def game():
    p1wins = 0
    with open(sys.argv[1]) as data:
        for hand in data.read().splitlines():
            alls = hand.split()
            p1, p2 = alls[:5], alls[5:]

            r1 = score(p1)
            r2 = score(p2)

            if r1 > r2:
                p1wins += 1

    print(f"Player 1 won {p1wins} rounds")

import timeit
times = timeit.repeat('game()', globals=globals(), number=1, repeat=5)
print(f">> best of 5 = {1000*min(times):.6f} ms")
