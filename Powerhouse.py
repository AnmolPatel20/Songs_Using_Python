import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        (f"Arangam adhirattumae , Whistle-u parakattumae… now {emoji.emojize(':microphone:')}{emoji.emojize(':fire:')}", 0.08, 1.0),
        (f"Karangal osarattumae , Take over ottumothamae… now {emoji.emojize(':clapping_hands:')}{emoji.emojize(':collision:')}", 0.09, 1.0),
        (f"Kolantha siripula face than Imaya mala pola mass than {emoji.emojize(':smiling_face_with_sunglasses:')}{emoji.emojize(':fire:')}", 0.09, 0.8),
        (f"Manasa parikira craze than Genz unna pathi pesutham {emoji.emojize(':sparkles:')}{emoji.emojize(':thought_balloon:')}", 0.08, 1.0),
        (f"Coo Coo Coolie Power House-eh {emoji.emojize(':high_voltage:')}{emoji.emojize(':fire:')}", 0.08, 0.8),
        (f"Ennaikum koraiyatha movusu-eh {emoji.emojize(':fire:')}{emoji.emojize(':helicopter:')}", 0.07, 0.6),
        (f"Un mela elasungalukkum Perusugalukkum podusungalukkum Paamaranukkum kumarigalukkum Loves-eh {emoji.emojize(':sparkling_heart:')}", 0.044, 1.1),
        (f"Coo Coo Coolie Power House-eh {emoji.emojize(':high_voltage:')}{emoji.emojize(':fire:')}", 0.08, 0.7),
        (f"Ennaikum koraiyatha movusu-eh {emoji.emojize(':fire:')}{emoji.emojize(':rocket:')}", 0.06, 0.6),
        (f"Un mela elasungalukkum Perusugalukkum podusungalukkum Paamaranukkum kumarigalukkum Loves-eh {emoji.emojize(':heart_with_arrow:')}{emoji.emojize(':two_hearts:')}", 0.044, 1.0),
        (f"Love you love you love you love{emoji.emojize(':heart_hands:')}", 0.06, 0.4),
        (f"Love love love {emoji.emojize(':red_heart:')} {emoji.emojize(':infinity:')}", 0.08, 1.0),
    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()
