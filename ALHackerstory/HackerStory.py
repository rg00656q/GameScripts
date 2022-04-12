# In case the link was not opening :
# supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250

import alhsmodule as alhs
import keyboard

ox, oy = alhs.locate_game()
alhs.start_bot(window_left_coord_x=ox, window_top_coord_y=oy)
while not keyboard.is_pressed('q'):
    if alhs.detect_gm(ox, oy):
        alhs.dodge_gm(ox, oy)
        print("Woop woop!")
        print("Po-po eluded")
    elif alhs.detect_player(ox, oy):
        alhs.dodge_player(ox, oy)
        print("dodged a player")
    elif alhs.detect_full_inventory(ox, oy):
        alhs.fast_sell(ox, oy)
        print("Done!")
alhs.stop_bot(ox, oy)
