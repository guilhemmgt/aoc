import re
from collections import Counter
import functools

LABELS = { 'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2 }

with open('input') as f:
    input = f.readlines()

# get a hand's type
def getType (hand):
    freq = Counter(hand)
    freq = [freq[k] for k in freq]
    if max(freq) == 5: return 6 # five of a kind
    elif max(freq) == 4: return 5 # four of a kind
    elif freq == [3,2] or freq == [2,3]: return 4 # full house
    elif max(freq) == 3: return 3 # three of a kind
    elif freq == [2,2,1] or freq == [2,1,2] or freq == [1,2,2]: return 2 # two pairs
    elif max(freq) == 2: return 1 # one pair
    else: return 0 # high card

# compare 2 CARDS LABELS
def cardBetterThan (label1, label2):
    value1, value2 = LABELS[label1], LABELS[label2]
    if value1 > value2: return 1
    elif value1 < value2: return -1
    else: return 0
    
# compare 2 HANDS TYPES
def handTypeBetterThan (hand1, hand2):
    type1, type2 = getType(hand1), getType(hand2)
    if type1 > type2: return 1
    elif type1 < type2: return -1
    else: return 0
    
# compare 2 HANDS LABELS
def handLabelsBetterThan (hand1, hand2):
    for i in range(0,5):
        comparison = cardBetterThan(hand1[i], hand2[i])
        if comparison == 0: continue
        else: return comparison
    return 0

# compare 2 HANDS (types, then labels)
def handBetterThan (hand1, hand2):
    typeCompare = handTypeBetterThan(hand1, hand2)
    if typeCompare == 0: return handLabelsBetterThan(hand1, hand2)
    else: return typeCompare

# parse
hands_bids = []
for line in input:
    d = line.split('\n')[0].split(' ')
    hands_bids.append([d[0], int(d[1])])

hands_bids = sorted(hands_bids, key=functools.cmp_to_key(lambda a,b: handBetterThan(a[0], b[0])))
hands_bids_ranks = [[hands_bids[i][0], hands_bids[i][1], i+1] for i in range(0, len(hands_bids))]

winnings = sum([x[1] * x[2] for x in hands_bids_ranks])

print(winnings)