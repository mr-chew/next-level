import random
import importlib.util

def module_from_file (module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

cm = module_from_file("cards_module", "../20.generate-deck-cards/generate-deck-cards.py")

cards = cm.generate_cards()
face_cards = cm.face_cards

def split_deck (deck = cards):
    mine = random.sample(deck, 26)
    opponent = [i for i in deck if i not in mine]
    random.shuffle(opponent)
    return mine, opponent

my_cards, opp_cards = split_deck()

def draw_cards (cards):
    return cards.pop(0)

def play_now (mine=my_cards, opp=opp_cards):
        my_play = draw_cards(mine)
        opp_play = draw_cards(opp)
        my_val = my_play.value if my_play.value not in face_cards else face_cards[my_play.value]
        opp_val = opp_play.value if opp_play.value not in face_cards else face_cards[opp_play.value]
        print(f"I draw: {my_play.value} {my_play.suit}")
        print(f"Opponent draw: {opp_play.value} {opp_play.suit}")
        if my_val > opp_val:
            mine.append(my_play)
            mine.append(opp_play)
        elif opp_val > my_val:
            opp.append(my_play)
            opp.append(opp_play)
        else:
            mine.append(my_play)
            opp.append(opp_play)
        return mine, opp
    
mine, opp = play_now()
counter = 0
while mine and opp:
    counter = counter + 1
    mine, opp = play_now(mine, opp)
    print(f"Round: {counter}")
    print(f"My deck: {len(mine)} cards, Opponent deck: {len(opp)} cards.")
    if len(mine) == 0:
        print("Opponent win")
    if len(opp) == 0:
        print(("I win"))
