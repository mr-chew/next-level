CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"

card_values = list(range(2,15))
suits = [CLUB, HEART, DIAMOND, SPADE]

face_cards = {
    10: 'T',
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
def generate_cards():
    cards = []
    for suit in suits:
        for value in card_values:
            if value in face_cards:
                _card = Card(face_cards[value], suit)
            else:
                _card = Card(value, suit)
            cards.append(_card)
    return cards
    
# cards = generate_cards()
# for card in cards:
#     print(card.value, card.suit)