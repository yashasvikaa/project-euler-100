from collections import Counter

value_map = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
             '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def reader():
    hands = []
    with open("problem_54(ques).txt") as f:
        for line in f:
            cards = line.strip().split()
            player1 = cards[:5]
            player2 = cards[5:]
            hands.append((player1, player2))
    return hands

def one_pair(hand):
    for i in range(0, 5):
        for j in range(i+1, 5):
            if hand[i][0] == hand[j][0]:
                return True
    return False

def two_pair(hand):
    values = [value_map[card[0]] for card in hand]
    counts = Counter(values)
    pairs = [val for val, count in counts.items() if count == 2]
    if len(pairs) == 2:
        return True
    return False
    

def three_kind(hand):
    values = [value_map[card[0]] for card in hand]
    counts = Counter(values)
    pairs = [val for val, count in counts.items() if count == 3]
    if pairs != []:
        return True
    return False

def straight(hand):
    values = [value_map[card[0]] for card in hand]
    is_straight = sorted(values) == list(range(min(values), max(values)+1))
    return is_straight 

def flush(hand):
    house = hand[0][1]
    for i in range(1, 5):
        if not hand[i][1] == house:
            return False
    return True 

def full_house(hand):
    values = [value_map[card[0]] for card in hand]
    counts = Counter(values)
    return sorted(counts.values()) == [2, 3]

def four_kind(hand):
    values = [value_map[card[0]] for card in hand]
    counts = Counter(values)
    pairs = [val for val, count in counts.items() if count == 4]
    if pairs != []:
        return True
    return False

def straight_flush(hand):
    if straight(hand) and flush(hand):
        return True
    return False

def royal_flush(hand):
    return flush(hand) and sorted([value_map[c[0]] for c in hand]) == [10, 11, 12, 13, 14]

def ranked(hand):
    values = sorted([value_map[card[0]] for card in hand], reverse = True)
    counts = Counter(values)
    most_common = counts.most_common()

    if royal_flush(hand):
        return (10, [14])
    if straight_flush(hand):
        return (9, values)
    if four_kind(hand):
        four_val = [val for val, count in counts.items() if count == 4][0]
        kicker = [val for val in values if val != four_val]
        return (8, [four_val] +  kicker)
    if full_house(hand):
        three_val = [val for val, count in counts.items() if count == 3]
        two_val = [val for val, count in counts.items() if count == 2]
        return (7, three_val + two_val)
    if flush(hand):
        return (6, values)
    if straight(hand):
        return (5, values)
    if three_kind(hand):
        three_val = [val for val, count in counts.items() if count == 3][0]
        kickers = sorted([val for val in values if val != three_val], reverse=True)
        return (4, [three_val] + kickers)
    if two_pair(hand):
        pairs = sorted([val for val, count in counts.items() if count == 2], reverse=True)
        kicker = [val for val in values if val not in pairs]
        return (3, pairs + kicker)
    if one_pair(hand):
        pair_val = [val for val, count in counts.items() if count == 2][0]
        kickers = sorted([val for val in values if val != pair_val], reverse=True)
        return (2, [pair_val] + kickers)
    return (1, values)


def compare(hand1, hand2):
    rank1, tiebreaker1 = ranked(hand1)
    rank2, tiebreaker2 = ranked(hand2)

    if rank1 != rank2:
        return rank1 > rank2
    else:
        return tiebreaker1 > tiebreaker2


def main():
    hands = reader()
    player1_wins = 0
    for hand in hands:
        hand1, hand2 = hand[0], hand[1]
        if compare(hand1, hand2):
            player1_wins += 1
    print(player1_wins)


if __name__ == "__main__":
    main()