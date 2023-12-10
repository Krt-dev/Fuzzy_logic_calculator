
def membership_function(value, low, mid, high):
    if low <= value <= mid:
        return (value - low) / (mid - low)
    elif mid <= value <= high:
        return (high - value) / (high - mid)
    else:
        return 0.0


def fuzzy_rules(player_hand, dealer_card):
    low_player_hand = membership_function(player_hand, 4, 10, 16)
    mid_player_hand = membership_function(player_hand, 10, 16, 21)
    high_player_hand = membership_function(player_hand, 16, 21, 26)

    low_dealer_card = membership_function(dealer_card, 2, 6, 10)
    mid_dealer_card = membership_function(dealer_card, 6, 10, 14)
    high_dealer_card = membership_function(dealer_card, 10, 14, 18)  

    #RULES
    #if player hand is LOW and dealer hand is HIGH then HIT
    hit = min(low_player_hand, high_dealer_card)

    #if player hand is mid and dealer hand is mid then STAND
    stand = min(mid_player_hand, mid_dealer_card)

    #if player hand is MID and dealer hand is LOW then DOUBLE DOWN
    double_down = min(mid_player_hand, low_dealer_card)

    #if player hand is HIGH and dealer hand is LOW then SPLIT
    split = min(high_player_hand, low_dealer_card)

    return hit, stand, double_down, split


def fuzzy_decision(player_hand, dealer_card):

    hit, stand, double_down, split = fuzzy_rules(player_hand, dealer_card)

 
    decision = max(hit, stand, double_down, split)

    return decision


while True:
    try:
        print("\n---WELCOME TO BLACKJACK DECISION CALCULATOR---\n")
        print("\nInput the total sum of the 2 starting cards")
        player_hand_value = int(input("Player's hand (between 4 and 26): "))
        print("\nInput the total sum of the dealers card")
        dealer_card_value = int(input("Dealer's card (between 2 and 18): "))
        if 4 <= player_hand_value <= 26 and 2 <= dealer_card_value <= 18:
            break
        else:
            print("Invalid input. Please enter valid values.")
    except ValueError:
        print("Invalid input.")

# Perform fuzzy decision
decision = fuzzy_decision(player_hand_value, dealer_card_value)

# Print the output
print("\nFuzzy Decision:")
print("Hit:", fuzzy_rules(player_hand_value, dealer_card_value)[0])
print("Stand:", fuzzy_rules(player_hand_value, dealer_card_value)[1])
print("Double Down:", fuzzy_rules(player_hand_value, dealer_card_value)[2])
print("Split:", fuzzy_rules(player_hand_value, dealer_card_value)[3])
print("\nOverall Decision (Defuzzified):", decision)
