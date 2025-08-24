def strength(ch):
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a') + 1
    elif 'A' <= ch <= 'Z':
        return ord(ch) - ord('A') + 27
    elif '0' <= ch <= '9':
        return int(ch)
    else:
        return 0

def battle(my_army, opposing_army):
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(opposing_army) > len(my_army):
        return "We retreated"

    my_wins = 0
    opp_wins = 0

    for m, o in zip(my_army, opposing_army):
        my_strength = strength(m)
        opp_strength = strength(o)

        if my_strength > opp_strength:
            my_wins += 1
        elif opp_strength > my_strength:
            opp_wins += 1
        # If equal, no one wins

    if my_wins > opp_wins:
        return "We won"
    elif opp_wins > my_wins:
        return "We lost"
    else:
        return "It was a tie"