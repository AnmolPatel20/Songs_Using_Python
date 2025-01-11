import sys
from time import sleep

def print_lyrics():
    lines = [
        ("You're a good soldier ,Choosing your battles", 0.08),
        ("Pick yourself up ,And dust yourself off", 0.04),
        ("Get back in the saddle", 0.06),
        ("You're on the front line ,Everyone's watching", 0.08),
        ("You know it's serious", 0.08),
        ("We're getting closer ,This isn't over", 0.08),
        ("The pressure's on ,You feel it", 0.10),
        ("But you got it all ,Believe it", 0.10),
        ("When you fall get up, oh oh", 0.08),
        ("If you fall get up, eh eh", 0.08),
        
    ]

    delays = [0.2,0.1,0.1,0.2,0.1,0.2,0.2,0.2,0.3] 

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()  
            sleep(char_delay)  
        sleep(delays[i])  
        print("")

print_lyrics()
