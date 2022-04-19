# In case the link was not opening :
# supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250
import alhs_selling_module as se
import alhs_module as alhs
import keyboard

encounters = 0
savings = 0
alhs.start_bot()
while not keyboard.is_pressed('q'):
    if keyboard.is_pressed('space'):
        se.buy_cash(savings)
    if alhs.omni_detect():
        encounters = alhs.dodge(encounters)
    elif alhs.detect_full_inventory():
        savings = se.efficient_sell(savings)
    #elif alhs.detect_no_twc():
    #    se.buy_twc()
alhs.stop_bot()
saving_text = "{:,}".format(savings)
print(f'I have dodged {encounters} encounters, and saved {saving_text} mesos this session')
