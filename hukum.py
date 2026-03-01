import emoji
import sys
from time import sleep

def print_lyrics():

    lines = [
        (f"Hukum... Tiger Ka Hukum {emoji.emojize(':tiger:')}{emoji.emojize(':crown:')}", 0.08, 0.0),
        (f"Alappara Kelapparom Dha Paaru Da {emoji.emojize(':fire:')}{emoji.emojize(':clapping_hands:')} Kalavaram Yeranguna Tha Daaru Da {emoji.emojize(':collision:')}", 0.055, 0.5),
        (f"Nelavaram Puriyidha Okkaruda {emoji.emojize(':sparkles:')}{emoji.emojize(':man_raising_hand:')}  Thalaivaru Kalathula Super Star’u Da {emoji.emojize(':star:')}{emoji.emojize(':sunglasses:')}", 0.055, 0.5),
        (f"Varamora Odachida Set Aanavan {emoji.emojize(':crown:')} Thalamora Kadakura Hit Aanavan {emoji.emojize(':fire:')}{emoji.emojize(':trophy:')}", 0.057, 0.5),
        (f"Eliyavan Manasula Fit Aanavan {emoji.emojize(':brain:')}{emoji.emojize(':sparkles:')} Mudivula Jeichida Urithaanavan {emoji.emojize(':crossed_swords:')}{emoji.emojize(':check_mark_button:')}", 0.058, 1.2),
        (f"Nadakkura Nada Puyalam Iche {emoji.emojize(':cyclone:')}{emoji.emojize(':fire:')} Mudi Odhukkura Style’ah Iche {emoji.emojize(':crown:')}{emoji.emojize(':sparkles:')}", 0.07, 0.5),
        (f"Kannavilla Ithu Real’ah Iche {emoji.emojize(':eyes:')}{emoji.emojize(':hundred_points:')}", 0.07, 0.5),
        (f"Thala Mudhal Adi Vara {emoji.emojize(':crown:')}{emoji.emojize(':person_running:')} Thalaivaru Alappara {emoji.emojize(':tiger:')}{emoji.emojize(':fire:')}", 0.05, 0.5),
        (f"Thani Thala Pola Bail’ah Iche {emoji.emojize(':lion:')} Ada Nooru’ku Dail’ah Iche {emoji.emojize(':telephone_receiver:')}", 0.06, 0.5),
        (f"Sethukkura Edam Jail’ah Iche {emoji.emojize(':oncoming_police_car:')}{emoji.emojize(':police_car_light:')}", 0.06, 0.6),
        (f"Sera Mudhal Thera Vara {emoji.emojize(':star:')}{emoji.emojize(':movie_camera:')} Thalaivaru Alappara {emoji.emojize(':tiger:')}{emoji.emojize(':fire:')}", 0.04, 0.5),
        (f"Onn Alumba Paatthavan {emoji.emojize(':eyes:')}{emoji.emojize(':astonished_face:')} Ungoppan Whistle’ah Kaettavan {emoji.emojize(':clapping_hands:')}", 0.06, 0.7),
        (f"Onn Mavanum Peranum Aatam Poda Veppavan {emoji.emojize(':man_dancing:')}", 0.1, 0.5),
        (f"Ivan Paera Thooka Naalu Paeru {emoji.emojize(':speaking_head:')}{emoji.emojize(':loudspeaker:')} Pattatha Parika Nooru Paeru {emoji.emojize(':crossed_swords:')}{emoji.emojize(':busts_in_silhouette:')}", 0.06, 0.5),
        (f"Kutti Chevutha Etti Paatha {emoji.emojize(':ear:')}{emoji.emojize(':eyes:')} Usura Kodukka Kodi Paeru {emoji.emojize(':red_heart:')}{emoji.emojize(':people_holding_hands:')}", 0.07, 0.5),
        (f".....BGM.....", 0.9, 0.5),

    ]

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
            
        print("")
        sleep(line_delay)

# Run the function
print_lyrics()