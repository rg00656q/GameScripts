# In case the link was not opening :
# supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250
import alhs_trade_module as tm
import alhs_module as alhs
import keyboard

encounters = 0
savings = 0
alhs.start_bot()
while not keyboard.is_pressed('q'):
    if keyboard.is_pressed('space'):
        tm.buy_cash(savings)
    if keyboard.is_pressed('w'):
        tm.buy_twc()
    if keyboard.is_pressed('l'):
        if alhs.al.getInterruptor():
            alhs.al.toggle_late_g = False
        else:
            alhs.al.toggle_late_g = True
    if alhs.omni_detect():
        encounters = alhs.dodge(encounters)
    elif alhs.detect_full_inventory():
        savings = tm.efficient_sell(savings)
    if alhs.al.getInterruptor() and alhs.detect_no_acc():
        tm.buy_buffs()

alhs.stop_bot()
saving_text = "{:,}".format(savings)
print(f'I have dodged {encounters} encounters, and saved {saving_text} mesos this session')
