import sys
from time import sleep

def print_lyrics():
    lines = [
        ("Get readyyy!!!", 0.08, 0.1),
        ("DHU  RAN  DHAR", 0.08, 0.3),
        ("I’m a king, but I’m far from a saint.", 0.03, 0.2),
        ("They call me a bad man, that’s a fucking good thing. ", 0.04, 0.2),
        ("Mama said, swing back when another man swings. ", 0.04, 0.2),
        ("So I make my mama proud and make the hits rain.", 0.04, 0.2),
        ("Father, Forgive me, I can’t forgive them.", 0.05, 0.2),
        ("You know my history, you know what I did then.", 0.04, 0.2),
        ("What I do now, a whole lot worse.", 0.06, 0.3),
        ("Heavy is the head, it’s a blessing and a curse.", 0.03, 0.6),
        ("Na de dil pardesi nu tainu nit da roona pai jau ga", 0.06, 0.4),
        ("Nal ranjhe tay jogi de tainu jogan hauna pai jau ga", 0.08, 0.5),
        ("Mai ishq de allein zakhma de khud has has ke muh seen lan gi", 0.075, 0.4),
        ("Je Yaaar mera mainu", 0.05, 0.1),
        ("Z.. Z.. Zehar", 0.06, 1.55),
        ("DHU  RAN  DHAR", 0.09, 2.8),
        ("DHU  RAN  DHAR", 0.09, 1.0), 
    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()
