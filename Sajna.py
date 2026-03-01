import emoji
import sys
from time import sleep
 
def print_lyrics():
    lines = [
        (f"{emoji.emojize(':sparkles:')} O Sajnaa..{emoji.emojize(':sparkling_heart:')}", 0.22, 0.2),
        (f"{emoji.emojize(':two_hearts:')} Main tera, Tu mere ho gayi aa..{emoji.emojize(':infinity:')}", 0.12, 0.1),
        (f"{emoji.emojize(':red_heart:')} ho gayi aa, ho gayi aa, ho gayi aa{emoji.emojize(':folded_hands:')}", 0.07, 0.1),
        (f"{emoji.emojize(':dove:')}  Maari koyal bethi Todle {emoji.emojize(':musical_note:')}", 0.11, 0.1),
        (f"{emoji.emojize(':rose:')} Mehendi na rang lai pardesh udi jaay re..{emoji.emojize(':sparkles:')}", 0.14, 0.2),
        (f"{emoji.emojize(':sun_with_face:')} Jone, koyal bethi Todle.. {emoji.emojize(':dove:')}{emoji.emojize(':musical_note:')}", 0.12, 0.2),
        (f"{emoji.emojize(':crescent_moon:')} Mahendi na rang lai pardesh udi jaaye re {emoji.emojize(':violin:')}", 0.12, 0.2),
        (f"{emoji.emojize(':musical_score:')} MUSIC {emoji.emojize(':musical_score:')}", 0.7, 15),
    ]
       
    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)


print_lyrics()
