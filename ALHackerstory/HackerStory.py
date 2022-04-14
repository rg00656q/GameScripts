# In case the link was not opening :
# supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250

import alhsmodule as alhs
import keyboard

encounters = 0
savings = 0
ox, oy = alhs.locate_game()
alhs.start_bot(game_window_left_coord_x=ox, game_window_top_coord_y=oy)
while not keyboard.is_pressed('q'):
    if keyboard.is_pressed('space'):
        alhs.buy_cash(ox, oy, savings)
    if alhs.omni_detect(ox, oy):
        encounters = alhs.dodge(ox, oy, encounters)
    elif alhs.detect_full_inventory(ox, oy):
        savings = alhs.efficient_sell(ox, oy, savings)
alhs.stop_bot(ox, oy)
print(f'I have dodged {encounters} encounters, and saved {savings} mesos this session')
