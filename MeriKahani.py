import emoji
import sys
from time import sleep

def print_lyrics():
    lines = [
        (f"{emoji.emojize(':child:')} Jhula Jhulaiye {emoji.emojize(':leaf_fluttering_in_wind:')}", 0.1, 0.3),
        (f"{emoji.emojize(':water_wave:')} Ye panghat nadiya kinare {emoji.emojize(':seedling:')}", 0.1, 0.3),
        (f"{emoji.emojize(':house:')} Ye angan nindiya tu aana {emoji.emojize(':sleeping_face:')}", 0.1, 0.2),
        (f"{emoji.emojize(':wind_face:')}  Hawa ke sang mujhko bhi tu dikhana {emoji.emojize(':eyes:')}", 0.08, 0.2),
        (f"{emoji.emojize(':rainbow:')} Apne rang Tera Mera galiyon main ye phirna {emoji.emojize(':person_walking:')}", 0.08, 0.1),
        (f"{emoji.emojize(':crescent_moon:')} Phirtay Phirtay raton ko ye thakna {emoji.emojize(':tired_face:')}", 0.08, 0.1),
        (f"{emoji.emojize(':old_woman:')} Thak ke nani ki godi main sona {emoji.emojize(':sleeping_face:')}", 0.12, 0.2),
        (f"{emoji.emojize(':fairy:')} Pariyon ke desh ja ke na ana {emoji.emojize(':sparkles:')}", 0.08, 0.2),
        (f"{emoji.emojize(':open_book:')} Ye meri hai Kahani.. {emoji.emojize(':person_raising_hand:')}", 0.3, 1),
        (f"{emoji.emojize(':open_book:')} Ye meri Kahani.. {emoji.emojize(':person_raising_hand:')}", 0.3, 10),
    ]
        
    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        sleep(line_delay)

print_lyrics()