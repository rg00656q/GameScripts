# In case the link was not opening :
# supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250

import alhsmodule as alhs
import keyboard

ox, oy = alhs.locate_game()
gm_nb = 0
hrp_nb = 0
alhs.start_bot(game_window_left_coord_x=ox, game_window_top_coord_y=oy)
while not keyboard.is_pressed('q'):
    if alhs.detect_gm(ox, oy):
        gm_nb = alhs.dodge_gm(ox, oy, gm_encounter_number=gm_nb)
        print(f'I dodged {gm_nb} GMs')
    elif alhs.detect_player(ox, oy):
        hrp_nb = alhs.dodge_player(ox, oy, highrank_player_encounter_number=hrp_nb)
        print(f'I dodged {hrp_nb} players')
    elif alhs.detect_full_inventory(ox, oy):
        alhs.efficient_sell(ox, oy)
alhs.stop_bot(ox, oy)
