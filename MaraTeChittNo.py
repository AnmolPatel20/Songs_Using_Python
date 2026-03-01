import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        (f"Mara Te Chitt No Chor Re.. Maro Sawariyo..{emoji.emojize(':folded_hands:')}{emoji.emojize(':red_heart:')}", 0.15, 0.5),
        (f"Mara Te Chitt No Chor Re.. Maro Sawariyo..{emoji.emojize(':peacock:')}{emoji.emojize(':blue_heart:')}", 0.13, 0.3),
        (f"Hee.. Jevo Radha Ne Nand No Kishor{emoji.emojize(':boy:')}{emoji.emojize(':girl:')}{emoji.emojize(':sparkles:')}", 0.12, 0.5),
        (f"Evo Maro Sawariyo.. Ho Maro Sanwariyo{emoji.emojize(':crown:')}{emoji.emojize(':star:')}", 0.13, 0.8),
        (f"Mara Te Chitt No Chor Re.. Maro Sawariyo....{emoji.emojize(':musical_notes:')}{emoji.emojize(':sparkling_heart:')}", 0.13, 0.5),      
        (f"Mara Te Chitt No Chor Re.. Maro Sawariyo..{emoji.emojize(':folded_hands:')}{emoji.emojize(':hibiscus:')}", 0.16, 0.8),
    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()