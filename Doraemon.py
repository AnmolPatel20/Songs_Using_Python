import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        # (Lyrics, char_delay, line_delay) --> delays tuned to match song pace
        (f"Zindagi sawar doon Ik nayi bahaar doon {emoji.emojize(':evergreen_tree:')}", 0.09, 0.8),
        (f"Duniya hi badal doon Main to pyara sa chamatkaar hoon {emoji.emojize(':globe_showing_Asia-Australia:')}", 0.08, 1.0),
        (f"Main kisi ka sapna hoon Jo aaj ban chuka hoon sach {emoji.emojize(':thought_balloon:')}", 0.06, 0.8),
        (f"Ab ye mera sapna hai ki Sabke sapne sach main karoon {emoji.emojize(':glowing_star:')}", 0.07, 1.3),
        (f"Aasmaan ko chhoo loon Titli ban udoon {emoji.emojize(':butterfly:')}", 0.08, 0.7),
        (f"Yeah.. Helicopter {emoji.emojize(':helicopter:')}", 0.15, 2.0),
        (f"Ah-ha-ha Main hoon ek udta robo {emoji.emojize(':cloud:')}", 0.09, 1.0),
        (f"Doraemon {emoji.emojize(':robot:')}", 0.25, 0.9),
        (f"Mano ya na mano {emoji.emojize(':grinning_cat:')}", 0.09, 1.2),
        (f"Main hoon ek udta robo {emoji.emojize(':light_blue_heart:')}", 0.07, 1.0),
        (f"Doraemon {emoji.emojize(':robot:')}", 0.25, 10.0),

    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()
