import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter.
    '''
    input("\nPress enter to continue. ")
    print()

def make_deck():
    '''()->list of str
    Returns a deck of cards with one queen removed.
    '''
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']  # Unicode suits: spade, heart, diamond, club
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    deck.remove('Q\u2663')  # Remove one queen as required
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
    Shuffles the deck.
    '''
    random.shuffle(deck)

def deal_cards(deck):
    '''(list of str) -> tuple of (list of str, list of str)
    Deals cards alternately to two players.
    '''
    return deck[::2], deck[1::2]

def remove_pairs(l):
    '''(list of str) -> list of str
    Removes pairs and shuffles remaining cards.
    '''
    no_pairs = []
    sorted_l = sorted(l, key=lambda x: x[:-1])
    i = 0
    while i < len(sorted_l) - 1:
        if sorted_l[i][:-1] == sorted_l[i + 1][:-1]:
            i += 2  # Skip both cards if they form a pair
        else:
            no_pairs.append(sorted_l[i])
            i += 1
    if i == len(sorted_l) - 1:
        no_pairs.append(sorted_l[i])
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''(list of str) -> None
    Prints the deck.
    '''
    print(" ".join(deck))

def get_valid_input(n):
    '''(int) -> int
    Ensures valid integer input within range.
    '''
    while True:
        try:
            choice = int(input(f"Give me an integer between 1 and {n}: "))
            if 1 <= choice <= n:
                return choice
            print(f"Invalid number. Please enter integer between 1 and {n}.", end=" ")
        except ValueError:
            print(f"Invalid input. Please enter integer between 1 and {n}.", end=" ")

def play_game():
    '''()->None
    Main game function.
    '''
    deck = make_deck()
    shuffle_deck(deck)
    dealer, human = deal_cards(deck)

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
    
    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    while dealer and human:
        # Human's turn
        print("*********************************************************** Your turn.")
        print("Your current deck of cards is:")
        print_deck(human)
        print(f"I have {len(dealer)} cards. If 1 stands for my first card and {len(dealer)} for my last card, which of my cards would you like?")
        
        choice = get_valid_input(len(dealer))
        selected_card = dealer.pop(choice - 1)
        print(f"You asked for my {choice}th card. Here it is. It is {selected_card}")
        
        human.append(selected_card)
        human = remove_pairs(human)
        print("With the card added, your current deck of cards is:")
        print_deck(human)
        wait_for_player()

        # Robot's turn
        if not human:
            print("Congratulations! You, Human, win")
            break

        print("*********************************************************** My turn.")
        robot_choice = random.randint(0, len(human) - 1)
        print(f"I took your {robot_choice + 1}th card.")
        dealer.append(human.pop(robot_choice))
        dealer = remove_pairs(dealer)
        wait_for_player()

        if not dealer:
            print("You lost! I, Robot, win")
            break

# Main
if __name__ == "__main__":
    play_game()
