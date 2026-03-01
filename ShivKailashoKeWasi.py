import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        # Shiv Kailasho ke Vasi (Lord of Kailash)
        (f"{emoji.emojize(':mountain:')} Shiv Kailasho ke Vasi{emoji.emojize(':trident_emblem:')}", 0.18, 0.6),
        (f"{emoji.emojize(':snowflake:')} Dhaulidharon ke raja{emoji.emojize(':crown:')}", 0.20, 0.6),
        (f"{emoji.emojize(':sparkles:')} Shankar Sankat Harna{emoji.emojize(':folded_hands:')}{emoji.emojize(':om:')}", 0.25, 1.8),
        (f"{emoji.emojize(':mountain:')} Shiv Kailasho ke Vasi{emoji.emojize(':trident_emblem:')}", 0.18, 0.6),
        (f"{emoji.emojize(':snowflake:')} Dhaulidharon ke raja{emoji.emojize(':crown:')}", 0.20, 0.6),
        (f"{emoji.emojize(':sparkles:')} Shankar Sankat Harna{emoji.emojize(':folded_hands:')}{emoji.emojize(':om:')}", 0.20, 1.0),
        (f"{emoji.emojize(':crescent_moon:')}.......{emoji.emojize(':banjo:')}", 0.8, 12),

    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()
