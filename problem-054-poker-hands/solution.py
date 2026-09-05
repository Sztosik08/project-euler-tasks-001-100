f = open("0054_poker.txt")
content = f.read()
raw_content = content.split()
print(raw_content)
player1_hands = []
player2_hands = []
for i in range(0, len(raw_content), 10):
    player1_hands.append(raw_content[i:i+5])
    player2_hands.append(raw_content[i+5:i+10])
    


from collections import Counter
  
def parse_hand(hand):
    face_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    values = []
    suits = []
    for el in hand:
        suits.append(el[-1])
        if el[0] in face_cards:
            values.append(face_cards[el[0]])
        else:
            values.append(int(el[0]))
    return sorted(values), suits

def are_consecutive(a):
    return sorted(a) == list(range(min(a), max(a) + 1))


print(parse_hand(player1_hands[0]))


def evaluate_hand(hand):
    values, suits = parse_hand(hand)
    counts = Counter(values)
    count_values = sorted(counts.values(), reverse=True)
    is_flush = len(set(suits)) == 1
    is_straight = are_consecutive(values)
    is_straight_flush = False
    if is_flush and is_straight:
        is_straight_flush = True
    is_four = count_values == [4,1]
    full_house = count_values == [3,2]
    is_three = count_values == [3,1,1]
    is_2pair = count_values == [2, 2, 1]
    is_pair = count_values == [2, 1, 1, 1]
    

    tiebreakers = tiebreakers = sorted(counts.keys(), key=lambda x: (counts[x], x), reverse=True)
    if is_flush and is_straight:
        return(8, tiebreakers)
    elif is_four:
        return(7, tiebreakers)
    elif full_house:
        return(6, tiebreakers)
    elif is_flush:
        return(5, tiebreakers)
    elif is_straight:
        return(4, tiebreakers)
    elif is_three:
        return(3, tiebreakers)
    elif is_2pair:
        return(2, tiebreakers)
    elif is_pair:
        return(1, tiebreakers)
    else:
        return(0, tiebreakers)
    


p1_wins = 0
for h1, h2 in zip(player1_hands, player2_hands):
    if evaluate_hand(h1) > evaluate_hand(h2):
        p1_wins += 1
print(p1_wins)
