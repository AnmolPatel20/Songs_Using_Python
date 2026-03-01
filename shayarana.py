import emoji
import sys
from time import sleep
 
def print_lyrics():
    lines = [
        (f"{emoji.emojize(':milky_way:')} Tu hasrat puraani..{emoji.emojize(':sparkles:')}", 0.09, 0.3),
        (f"{emoji.emojize(':snowflake:')}  Tu aadat nayi hai..{emoji.emojize(':gem_stone:')}", 0.09, 1.5),
    ]
       
    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()
