import pyautogui as pag

path = "ALH_images\\"

""" Cash Shop buttons list """
cs_x, cs_y = (610, 290)  # Cash Shop button (to use Cash)
exit_x, exit_y = (620, 390)  # Exit button

glob_x = 0
glob_y = 0


def getglob_x():
    return glob_x


def getglob_y():
    return glob_y


def usage():
    print("""
Le bot se lance avec Python
La fenêtre de jeu ne doit pas être cachée, déplacée,ou minimisée
Enfin a tout moment appuyer sur q pour arrêter le bot
    """)


def locate_game():
    if pag.locateOnScreen(path + 'CS_UI.png', confidence=0.8) is not None:
        left, top, width, height = pag.locateOnScreen(path + 'CS_UI.png', confidence=0.8)
        return left, top
    elif pag.locateOnScreen(path + 'FM_UI.png', confidence=0.8) is not None:
        left, top, width, height = pag.locateOnScreen(path + 'FM_UI.png', confidence=0.8)
        return left, top
    elif pag.locateOnScreen(path + 'Game_UI.png', confidence=0.8) is not None:
        left, top, width, height = pag.locateOnScreen(path + 'Game_UI.png', confidence=0.8)
        return left, top
    else:
        usage()
        exit(0)


def click(button_x, button_y):
    pag.moveTo(glob_x + button_x, glob_y + button_y)
    pag.leftClick()


def text_to_int(text_price):
    try:
        cleaning = ",!() @.\n"
        for char in cleaning:
            text_price = text_price.replace(char, '')
        price = int(text_price)
    except ValueError:
        price = 0
    return price


class PictureError(Exception):
    def __init__(self):
        super()
