import re

with open('input') as f:
    input = f.readlines()
    
# array of [winning numbers, numbers you have, copies of this card (including original)]
cards = []
for card in input:
    content = card.split(':')[1].split('|')
    winning = re.findall(r'\d+', content[0])
    have = re.findall(r'\d+', content[1])
    cards.append([winning, have, 1])
    
processed = 0
for i in range(0,len(cards)):
    card = cards[i]
    winning = card[0]
    have = card[1]
    amount = card[2]
    
    # computes points
    points = 0
    for n in have:
        if n in winning:
            points += 1
    
    # resolves all copies
    for j in range(i+1, i+1+points):
        cards[j][2] += amount
    processed += amount
    
print(processed)
