import emoji
import sys
from time import sleep

def print_lyrics():

    lines = [
        (f"{emoji.emojize(':folded_hands:')} Shri Ram Jai Ram Jai Jai Ram {emoji.emojize(':bow_and_arrow:')}", 0.13, 0.4),
        (f"{emoji.emojize(':om:')}  Shri Ram Jai Ram Jai Jai Ram {emoji.emojize(':sun:')}", 0.12, 0.1),
        (f"{emoji.emojize(':crown:')} Sita Ram Sita Ram {emoji.emojize(':sparkling_heart:')}", 0.09, 0.2),
        (f"{emoji.emojize(':lotus:')}  Sita Ram Sita Ram {emoji.emojize(':sparkles:')}", 0.09, 0.2),
        (f"{emoji.emojize(':musical_notes:')} Sita Ram Sita Ram {emoji.emojize(':star:')}", 0.09, 0.3),
        (f"{emoji.emojize(':folded_hands:')} Sita Ram Sita Ram {emoji.emojize(':hibiscus:')}", 0.09, 0.3),
        (f"{emoji.emojize(':crown:')} Sita Ram Sita Ram {emoji.emojize(':sparkling_heart:')}", 0.09, 0.2),
        (f"{emoji.emojize(':lotus:')}  Sita Ram Sita Ram {emoji.emojize(':sparkles:')}", 0.09, 0.2),
        (f"{emoji.emojize(':musical_notes:')} Sita Ram Sita Ram {emoji.emojize(':star:')}", 0.09, 0.2),
        (f"{emoji.emojize(':folded_hands:')} Sita Ram Sita Ram {emoji.emojize(':hibiscus:')}", 0.09, 0.2),
        (f"{emoji.emojize(':folded_hands:')} Shri Ram Jai Ram Jai Jai Ram {emoji.emojize(':bow_and_arrow:')}", 0.15, 0.5),
        (f"{emoji.emojize(':om:')}  Shri Ram Jai Ram Jai Jai Ram {emoji.emojize(':sun:')}", 0.13, 0.3),
    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()