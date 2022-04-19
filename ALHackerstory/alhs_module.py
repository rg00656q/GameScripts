import pyautogui as pag
import alhs_commands as al


# Game screens
wx, wy = (700, 425)  # Taille de la fenêtre de jeu
pix_detect_x, pix_detect_y = (470, 246)  # Coordonnées du point d'apparition des ennemis
""" Game icons """
accuracy_ico_x, accuracy_ico_y = (40, 130)
str_ico_x, str_ico_y = (80, 130)
twinc_ico_x, twinc_ico_y = (460, 60)


def start_bot():
    al.init_glob()
    al.glob_x, al.glob_y = al.locate_game()
    al.click(al.exit_x, al.exit_y)


def omni_detect():
    if pag.pixel(int(al.getglob_x() + pix_detect_x), int(al.getglob_y() + pix_detect_y))[0] != 255:
        return True
    else:
        return False


def dodge(encounters):
    pag.moveTo(al.getglob_x() + al.cs_x, al.getglob_y() + al.cs_y)
    pag.leftClick()
    encounters += 1
    al.click(al.exit_x, al.exit_y)
    return encounters


def detect_full_inventory():
    if pag.locateOnScreen(al.path + 'slot9.png', region=(al.getglob_x() + 420, al.getglob_y() + 370, 68, 68)) is None:
        return True
    else:
        return False


def detect_no_twc():
    if pag.locateOnScreen(
            al.path + 'twincoupon.png', region=(al.getglob_x() + twinc_ico_x, al.getglob_y() + twinc_ico_y, 60, 60)
    ) is None:
        return True
    else:
        return False


def detect_no_acc():
    if pag.pixel(int(al.getglob_x() + accuracy_ico_x), int(al.getglob_y() + accuracy_ico_y))[0] == 255:
        return True
    else:
        return False


def stop_bot():
    pag.moveTo(al.getglob_x() + al.cs_x, al.getglob_y() + al.cs_y)
    pag.leftClick()
