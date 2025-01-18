import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        (f"{emoji.emojize(':cloud_with_lightning:')}  Stranded in the open{emoji.emojize(':man_standing:')}",0.16),
        (f"{emoji.emojize(':fire:')} Dried out tears of sorrow{emoji.emojize(':disappointed_face:')}", 0.16),
        (f"{emoji.emojize(':speaking_head:')}  Lacking all emotion{emoji.emojize(':tired_face:')}", 0.16),
        (f"{emoji.emojize(':eyes:')} Staring down the barrel waiting for the{emoji.emojize(':hourglass_not_done:')}", 0.12),
        (f"{emoji.emojize(':flexed_biceps:')} Final gates to open{emoji.emojize(':shinto_shrine:')}", 0.16),
        (f"{emoji.emojize(':glowing_star:')} To a new tomorrow{emoji.emojize(':sunrise_over_mountains:')}", 0.16),
        (f"{emoji.emojize(':man_running:')} Moving with the motion{emoji.emojize(':cyclone:')}", 0.16 ),
        (f"{emoji.emojize(':high_voltage:')} Following the light that sets me free{emoji.emojize(':dove:')}", 0.13),
        (f"{emoji.emojize(':musical_notes:')} MUSIC {emoji.emojize(':musical_notes:')}", 0.4),     
    ]

    delays = [2,2.25,2,0.2,3,3,2,0.2,3.1,3] 

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()  
            sleep(char_delay)  
        sleep(delays[i])  
        print("")

print_lyrics()
