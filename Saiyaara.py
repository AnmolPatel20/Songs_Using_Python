import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        (f"Tujhko hee gaaun main {emoji.emojize(':microphone:')}{emoji.emojize(':sparkling_heart:')}", 0.11, 1.0),
        (f"Tujhko pukaaarrruuuuunnnn...unnn..unnn..unnn..unnn..unnn..ounnnn...oouunounn... {emoji.emojize(':clapping_hands:')}{emoji.emojize(':red_heart:')}", 0.15, 1.5),
        (f"Saiyaara tu to badla nahi hai {emoji.emojize(':smiling_face_with_sunglasses:')}{emoji.emojize(':fire:')}{emoji.emojize(':milky_way:')}", 0.15, 1.1),
        (f"Mausam zara sa rootha hua hai {emoji.emojize(':sparkles:')}{emoji.emojize(':cloud_with_rain:')}", 0.15, 1.5),
        (f"Saiyaara tu to badla nahi hai {emoji.emojize(':high_voltage:')}{emoji.emojize(':star:')}", 0.13, 1),       
        (f"Mausam zara sa rootha hua hai {emoji.emojize(':fire:')}{emoji.emojize(':red_heart:')}", 0.16, 0.8),
    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()
