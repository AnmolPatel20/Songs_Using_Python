import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        (f"{emoji.emojize(':om:')}  Ommm.....{emoji.emojize(':person_in_lotus_position:')}", 0.5, 2.0),
        (f"{emoji.emojize(':musical_notes:')} MUSIC {emoji.emojize(':sparkles:')}", 1.0, 6.5),
        (f"{emoji.emojize(':om:')} Om Gan Ganapataye Namo Namah {emoji.emojize(':folded_hands:')}", 0.12, 0.2),
        (f"{emoji.emojize(':classical_building:')} Shri Siddhivinayak Namo Namah {emoji.emojize(':diya_lamp:')}", 0.10, 0.2),
        (f"{emoji.emojize(':elephant:')} Astavinayak Namo Namah {emoji.emojize(':sparkles:')}", 0.12, 0.2),
        (f"{emoji.emojize(':elephant:')} Ganapati Bappa Moraya.. {emoji.emojize(':folded_hands:')}", 0.12, 0.2),
        (f"{emoji.emojize(':crescent_moon:')} Mangal Moorti Moraya.. {emoji.emojize(':diya_lamp:')}", 0.10, 0.3),
        (f"{emoji.emojize(':om:')} Om Gan Ganapataye Namo Namah {emoji.emojize(':folded_hands:')}", 0.11, 0.2),
        (f"{emoji.emojize(':classical_building:')} Shri Siddhivinayak Namo Namah {emoji.emojize(':diya_lamp:')}", 0.09, 0.2),
        (f"{emoji.emojize(':elephant:')} Astavinayak Namo Namah {emoji.emojize(':sparkles:')}", 0.12, 0.2),
        (f"{emoji.emojize(':elephant:')} Ganapati Bappa Moraya.. {emoji.emojize(':folded_hands:')}", 0.12, 0.2),
        (f"{emoji.emojize(':crescent_moon:')} Mangal Moorti Moaraya.. {emoji.emojize(':diya_lamp:')}", 0.07, 8.0),
    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()
