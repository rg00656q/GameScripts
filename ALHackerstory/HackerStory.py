# In case the link was not opening :
# supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250

import alhsmodule as alhs
import keyboard

ox, oy = alhs.locate_game()
gm_nb = 0
hrp_nb = 0
alhs.start_bot(game_window_left_coord_x=ox, game_window_top_coord_y=oy)
while not keyboard.is_pressed('q'):
    if alhs.omni_detect(ox, oy):
        alhs.dodge(ox, oy)
    elif alhs.detect_full_inventory(ox, oy):
        alhs.efficient_sell(ox, oy)
alhs.stop_bot(ox, oy)
