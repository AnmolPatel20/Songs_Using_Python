import emoji
import sys
from time import sleep
 
def print_lyrics():
    lines = [
        (f"{emoji.emojize(':milky_way:')} Ooo..oo {emoji.emojize(':sparkles:')}", 0.18, 0.6),
        (f"{emoji.emojize(':snowflake:')} Sapno ke bin aankhon ki jaise keemat koi na {emoji.emojize(':gem_stone:')}", 0.12, 0.4),
        (f"{emoji.emojize(':sparkling_heart:')} Waise hoon main tere bin, meri chahat koi na {emoji.emojize(':folded_hands:')}", 0.13, 0.1),
        (f"{emoji.emojize(':volcano:')} Dardon ke ek kehna hai {emoji.emojize(':fire:')}", 0.11, 0.1),
        (f"{emoji.emojize(':sparkling_heart:')} Saansein jisko kehta hoon {emoji.emojize(':sparkles:')}", 0.10, 0.2),
        (f"{emoji.emojize(':sun_with_face:')} Teri soorat marham hai {emoji.emojize(':folded_hands:')}{emoji.emojize(':sparkles:')}", 0.10, 0.2),
        (f"{emoji.emojize(':crescent_moon:')} Dooji raahat koi na {emoji.emojize(':violin:')}", 0.12, 0.2),
        (f"{emoji.emojize(':crescent_moon:')} Chanda kaise haasil hoga ye bataa {emoji.emojize(':violin:')}", 0.13, 0.2),
        (f"{emoji.emojize(':blossom:')} Phoolon ka qisa se kya hai waasta {emoji.emojize(':violin:')}", 0.14, 10),
    ]
       
    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()
