import pyautogui as pag
import alhs_commands as al
import alhs_trade_module as tm
import keyboard


# Game screens
wx, wy = (700, 425)  # Taille de la fenêtre de jeu
pix_detect_x, pix_detect_y = (470, 246)  # Coordonnées du point d'apparition des ennemis
""" Game icons """
accuracy_ico_x, accuracy_ico_y = (40, 130)


def start_bot():
    al.glob_x, al.glob_y = al.locate_game()
    al.click(al.exit_x, al.exit_y)


def omni_detect():
    if pag.pixel(int(al.getglob_x() + pix_detect_x), int(al.getglob_y() + pix_detect_y))[0] != 255:
        return True
    else:
        return False


def detect_full_inventory():
    if pag.locateOnScreen(al.path + 'slot9.png', region=(al.getglob_x() + 420, al.getglob_y() + 370, 68, 68)) is None:
        return True
    else:
        return False


def dodge(encounters):
    pag.moveTo(al.getglob_x() + al.cs_x, al.getglob_y() + al.cs_y)
    pag.leftClick()
    encounters += 1
    al.click(al.exit_x, al.exit_y)
    return encounters


def stop_bot():
    pag.moveTo(al.getglob_x() + al.cs_x, al.getglob_y() + al.cs_y)
    pag.leftClick()


def bot():
    encounters = 0
    savings = 0
    start_bot()
    while not keyboard.is_pressed('q'):
        if keyboard.is_pressed('w'):
            tm.buy_cash(savings)
        if keyboard.is_pressed('e'):
            tm.buy_buffs()
        if omni_detect():
            encounters = dodge(encounters)
        if detect_full_inventory():
            savings = tm.efficient_sell(savings)
    stop_bot()
    saving_text = "{:,}".format(savings)
    print(f'I have dodged {encounters} encounters, and saved {saving_text} mesos this session')
