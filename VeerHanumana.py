import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        (f"{emoji.emojize(':folded_hands:')} Ram Ram... Ram Ram.... Ram Ram.... Ram Ram....{emoji.emojize(':om:')}", 0.2, 1.0),
        (f"{emoji.emojize(':musical_notes:')} TUNE {emoji.emojize(':musical_notes:')}", 0.5, 0.8),
        (f"{emoji.emojize(':monkey_face:')} Ramji Ka Pyara.. Siya Ka Dulara..{emoji.emojize(':folded_hands:')}", 0.14, 0.5),
        (f"{emoji.emojize(':shield:')}  Sankat Hariyo Re{emoji.emojize(':folded_hands:')}{emoji.emojize(':om:')}", 0.14, 0.5),
        (f"{emoji.emojize(':red_heart:')}  Prabhu Man Basiyo Re {emoji.emojize(':folded_hands:')}", 0.14, 0.5),
        (f"{emoji.emojize(':shield:')}  Sankat Hariyo Re {emoji.emojize(':folded_hands:')}", 0.14, 0.5),
        (f"{emoji.emojize(':red_heart:')}  Prabhu Man Basiyo Re{emoji.emojize(':folded_hands:')}{emoji.emojize(':om:')}", 0.14, 0.5),
        (f"{emoji.emojize(':om:')}  Veer Hanumana Ati Balwana {emoji.emojize(':monkey:')}", 0.18, 0.5),
        (f"{emoji.emojize(':folded_hands:')} Ram Naam Rasiyo Re {emoji.emojize(':om:')}", 0.14, 0.5),
        (f"{emoji.emojize(':red_heart:')}  Prabhu Man Basiyo Re  {emoji.emojize(':folded_hands:')}", 0.14, 0.5),
        (f"{emoji.emojize(':folded_hands:')} Ram Naam Rasiyo Re {emoji.emojize(':om:')}", 0.15, 0.5),
        (f"{emoji.emojize(':red_heart:')}  Prabhu Man Basiyo Re{emoji.emojize(':folded_hands:')}", 0.14, 0.5),
    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()