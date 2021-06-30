import random

# Global variables to create cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    """
    Creates a default class for all cards
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """
    Creates a default class for deck
    """

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                add_cards = Card(suit, rank)
                self.deck.append(add_cards)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        print("This shows the list of cards in the deck")
        list_cards = ''
        i = 0
        for card in self.deck:
            i += 1
            if i > 10:
                list_cards += f"{i}: {card}\n"
        return list_cards


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If total values is more than 21 and there is an ace in hand
        # change value of ace to be 1 instead of 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Please enter a correct value!")
        else:
            if chips.total < chips.bet:
                print("Sorry your current balance is ${} unable to bet ${}".format(chips.total, chips.bet))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:

        answer = input("Press H for Hit or S for stand ").upper()

        if answer == "H":
            hit(deck, hand)
        elif answer == "S":
            print("Player stands. Dealer is playing. ")
            playing = False
        else:
            print("Sorry wrong input please try again")
            continue
        break


def show_some(player, dealer):
    # shows the dealer's second card
    print("\n Dealer's Hand: ")
    print("First card hidden! ")
    print(dealer.cards[1])

    # Shows all the cards in player's hand
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    # shows all the dealer's card
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    # Calculate and display value for dealer
    print(f"Value of Dealer's hand is:{dealer.value} ")

    # Shows all player's card
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    # Calculate and display value for player
    print(f"Value of Player's hand is:{player.value} ")


def player_busts(chips):
    print("Player Busts!")
    chips.lose_bet()


def player_wins(chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer Busts!")
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer Wins!")
    chips.lose_bet()


def player_low(chips):
    print("Player score below 17! Player loses!")
    chips.lose_bet()


def push():
    print("Dealer and Player tie! It's a push. ")


def main():
    global playing
    # Set up the Player's chips
    player_chips = Chips()

    while True:
        # Print an opening statement
        print("Welcome to the game of BlackJack! Score as close to 21 to win! \n")
        print("Each play has to have 17 or more to win!\nAce counts as 11 or 1. ")

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Shows the starting chips and prompt the Player for their bet
        print(f"\nPlayer has {player_chips.total} chips")
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        print(f"Player Value:{player_hand.value}")

        while playing:  # recall this variable from our hit_or_stand function
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)
            print(f"Player Value:{player_hand.value}")

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if player_hand.value < 17:
                player_low(player_chips)
            elif dealer_hand.value > 21:
                dealer_busts(player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
            else:
                push()

        # Inform Player of their remaining chips
        print(f"\nPlayer has {player_chips.total} chips remaining")
        # Checks to see if the player has chips left
        if player_chips.total <= 0:
            print("Player has run out of chips! \nPlayer lost!")
            no_chips = input("Do you want to play again? Key in Y to play, any other key to stop").upper()
            # If there are no chips, ask the player if they want to play again, else exit the game
            if no_chips == "Y":
                player_chips = Chips()
                playing = True
                continue
            else:
                print("Thank you for playing!")
                break

        # Ask to play again
        new_hand = input("Enter Y to play another hand. Any other key to stop playing ").upper()

        if new_hand == "Y":
            playing = True
            continue
        else:
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
