import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        (f"Yeah, you can be the greatest{emoji.emojize(':person_with_crown:')}, you can be the best{emoji.emojize(':man_technologist:')}", 0.05),
        (f"You can be the King Kong {emoji.emojize(':gorilla:')} bangin' on your chest{emoji.emojize(':oncoming_fist:')}", 0.05),
        (f"You can beat the world{emoji.emojize(':globe_showing_Asia-Australia:')}, you can win the war{emoji.emojize(':crossed_swords:')}", 0.06),
        (f"You can talk to God{emoji.emojize(':folded_hands:')}, go banging on his door{emoji.emojize(':door:')}", 0.06),
        (f"You can throw your hands up{emoji.emojize(':raising_hands:')}, you can beat the clock{emoji.emojize(':eight-thirty:')}", 0.06),
        (f"You can move a mountain{emoji.emojize(':mountain:')}, you can break rocks{emoji.emojize(':rock:')}", 0.06),
        (f"You can be a Master{emoji.emojize(':ninja:')}, Don't wait for luck{emoji.emojize(':four_leaf_clover:')}", 0.06),
        (f"Dedicate Yourself and {emoji.emojize(':man:')}You can find Yourself{emoji.emojize(':shooting_star:')}", 0.05),
        (f"Standing{emoji.emojize(':man_standing:')} in the Hall of Fame{emoji.emojize(':trophy:')}", 0.06),
        (f"And the world's{emoji.emojize(':globe_showing_Asia-Australia:')} gonna know your name {emoji.emojize(':flexed_biceps:')}", 0.06),
        (".", 0.06),  
    ]

    delays = [0.2,0.1,0.1,0.2,0.1,0.2,0.2,0.2,3.1,3] 

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()  
            sleep(char_delay)  
        sleep(delays[i])  
        print("")

print_lyrics()
