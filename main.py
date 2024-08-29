from random import shuffle

class Card:
    def __init__(self, symbol, val, suit) -> None:
        self.suit = suit
        self.symbol = symbol
        self.val = val

class Deck:
    symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Club", "Diamond", "Heart", "Spade"]

    def __init__(self) -> None:
        self.cards = [Card(symbol, idx, suit) for idx, symbol in enumerate(Deck.symbols) for suit in Deck.suits]
    
    def shuffle(self):
        shuffle(self.cards)

    def distribute(self):
        player_cards = []
        for i in range(26):
            player_cards.append(self.cards.pop(0))
        return player_cards

class Player:
    def __init__(self, name, cards) -> None:
        self.name = name
        self.cards = cards
    
    def play_card(self):
        return self.cards.pop(0) if self.cards else None
    
    def add_card(self, cards):
        shuffle(self.cards)
        print(f'{self.name} got {len(cards)} cards!')
        self.cards.extend(cards)


def start_game():
    deck = Deck()
    deck.shuffle()
    p1 = input("Enter player 1 name: ")
    p2 = input("Enter player 2 name: ")
    player1 = Player(p1, deck.distribute())
    player2 = Player(p2, deck.distribute())
    print(':::::: GAME STARTS NOW ::::::')
    war_cards = []
    
    while True:
        if not player1.cards:
            print(f'::::::  {player2.name} WON THE GAME!! ::::::')
            break
        elif not player2.cards:
            print(f'::::::  {player1.name} WON THE GAME!! ::::::')
            break
        
        card1 = player1.play_card()
        card2 = player2.play_card()
        print(f'{player1.name} played {card1.symbol} of {card1.suit}')
        print(f'{player2.name} played {card2.symbol} of {card2.suit}')
        
        if card1.val == card2.val:
            print("::::::  !!IT'S A DRAW!!  ::::::")
            if len(player1.cards) < 2:
                print(f':::::: BUT {player1.name} HAS NO CARDS! {player2.name} WON THE GAME!! ::::::')
                break
            elif len(player2.cards) < 2:
                print(f':::::: BUT {player2.name} HAS NO CARDS! {player1.name} WON THE GAME!! ::::::')
                break
            print(":::::: WAR TIME! ::::::")
            p1_war = player1.play_card()
            p2_war = player2.play_card()
            print(f"::::::  {player1.name}'s {p1_war.symbol} of {p1_war.suit} AND {player2.name}'s {p2_war.symbol} of {p1_war.suit} ARE IN THE WARZONE!! ::::::")
            war_cards.extend([card1, card2, p1_war, p2_war])
            continue
        elif card1.val > card2.val:
            print(f":::::: {player1.name} GETS THE CARD!! ::::::")
            player1.add_card([card1, card2] + war_cards)
        else:
            print(f":::::: {player2.name} GETS THE CARD!! ::::::")
            player2.add_card([card1, card2] + war_cards)
        war_cards.clear()

start_game()
