import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
    'Ace'
)
values = {
    'Two': 2, 
    'Three': 3, 
    'Four': 4, 
    'Five': 5, 
    'Six': 6, 
    'Seven':7, 
    'Eight': 8, 
    'Nine': 9, 
    'Ten': 10, 
    'Jack': 10, 
    'Queen': 10, 
    'King': 10, 
    'Ace': 10
    }
Ace_of_1 = {'Ace': 1}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}. {self.value}'

class Deck:

    def __init__(self):
        self.all_cards = []
        
        for i in suits:
            for j in ranks:
                card = Card(i, j)
                self.all_cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.value = 0
        self.aces = 0
    
    def add_cards(self, card):
        self.all_cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def total_of_cards(self):
        sum = 0
        for i in self.all_cards:
            sum += i.value
        return sum 
    
    def __str__(self): 
        cards_to_string = '' 
        for i in self.all_cards:
            cards_to_string += ' ' + i
        return f'Player {self.name} has {self.all_cards}.'

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_cards(single_card)
    hand.adjust_for_ace()

def hit_or_stay(deck, hand):
    global playing

    while True:
        answer = input('Do you want to Hit or Stay ? (h / s)')

        if answer not in ['h', 's']:
            print('Invalid input.')
        
        if answer == 'h':
            hit(deck, hand)
        elif answer == 's':
            print('Player Stands Dealer"s Turn')
        break

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except:
            print('Sorry, provide an integer.')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have: {chips.total}')
            else:
                break

def wanna_play_again():
    answer = 'Wrong'

    while answer not in ['y', 'n']:
        answer = input('Do you want to play again ? (y / n)')

        if answer not in ['y', 'n']:
            print('Invalid input.')

    
    if answer == 'y':
        return True
    else:
        return False

def print_some_cards(player, dealer):
    print('\n Dealer"s hand:')
    print('First card hidden!')
    print(dealer.all_cards[0])

    print('\n Player"s hand:')
    for i in player.all_cards:
        print(i)

def show_all_cards(player, dealer):
    # Loop through the player's hand
    print('\n Dealer"s hand:',*dealer.all_cards, sep='\n')

    print(f'Value of Dealer"s hand is:{dealer.value}')

    # Loop through the player's hand
    print('\n Player"s hand:',*player.all_cards, sep='\n') 

    print(f'Value of Player"s hand is:{player.value}')

def player_busts(player, dealer, chips):
    print('Player cards are more than 21. It is a bust!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player WINS!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer WINS!')
    chips.lose_bet()

def dealer_busts(player, dealer, chips):
    print('Player WINS!')
    chips.win_bet()


class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

game_on = True
# c = Card('Hearts', 'Ace')
# b = Card('Ace', 'Ace')
# arr = [c, b]
# deal = arr.pop()
# if deal.rank == 'Ace':
#     print('Ace')
while True:

    player = Player('Daulet')
    computer = Player('Dealer')

    deck = Deck()

    deck.shuffle()        

    for i in range(2):
        computer.add_cards(deck.deal())
        player.add_cards(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    print('\n'*20)
    
    print_some_cards(player, computer)

    while game_on:

        hit_or_stay(deck, player)

        print_some_cards(player, computer)

        if player.value > 21:
            player_busts(player, computer, player_chips)
            break
        
    if player.value <= 21:
        print("It is Dealer's turn now.")

        while computer.value < 17:

            hit(deck, computer)

        show_all_cards(player, computer)

        if computer.value > 21:
            dealer_busts(player, computer, player_chips)
        
        if player.value > computer.value:
            player_wins(player, computer, player_chips)
        elif player.value < computer.value:
            dealer_busts(player, computer, player_chips)
        else:
            print('Draw')
            game_on = False
        
    print(f'\n Player total chips are at: {player_chips.total}')

        


    if wanna_play_again():
        game_on = True
    else:
        break

            






    

    

    



