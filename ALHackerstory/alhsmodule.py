import pyautogui as pag
import pytesseract as tess
from time import sleep

tess.pytesseract.tesseract_cmd = r'C:\Users\guill\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

path = "AHL_images\\"

# Game screens
wx, wy = (700, 425)  # fenetre de jeu

""" Cash Shop buttons list """
cs_x, cs_y = (610, 290)  # Cash Shop button (to use Cash)
pet_x, pet_y = (60, 358)  # Pet and Hack buttons
etc_x, etc_y = (140, 358)  # ETC and Scroll buttons
npc_x, npc_y = (218, 358)  # NPC and Buy Equip buttons
exit_x, exit_y = (620, 390)  # Exit button

""" free market buttons list """
fm_x, fm_y = (610, 250)  # Free Market button
selld_x, selld_y = (300, 358)  # Sell Drops button
fame_x, fame_y = (385, 358)  # Fame button
cash_x, cash_y = (470, 358)  # Cash button (to buy Cash)

""" Coordonnees des bouttons de vente """
ok_x, ok_y = (675, 200)
yes_x, yes_y = (585, 330)
no_x, no_y = (645, 330)


def usage():
    print("""
Le bot se lance avec Python
La fenetre de jeu ne doit pas etre cachee, deplacee,ou minimisee
Enfin a tout moment appuier sur q pour arreter le bot
    """)


def locate_game():
    if pag.locateOnScreen(path+'CS_UI.png', confidence=0.8) is not None:
        left, top, width, height = pag.locateOnScreen(path+'CS_UI.png', confidence=0.8)
        return left, top
    elif pag.locateOnScreen(path+'FM_UI.png', confidence=0.8) is not None:
        left, top, width, height = pag.locateOnScreen(path+'FM_UI.png', confidence=0.8)
        return left, top
    elif pag.locateOnScreen(path+'Game_UI.png', confidence=0.8) is not None:
        left, top, width, height = pag.locateOnScreen(path+'Game_UI.png', confidence=0.8)
        return left, top
    else:
        usage()
        exit(0)


""" Boucle de ventes multiples (pour vendre les 9 slots) """
""" Vente rapide """


def fast_sell(ox, oy):
    print("going to Free Market, to sell items")
    pag.moveTo(ox + fm_x, oy + fm_y)
    pag.leftClick()
    pag.moveTo(ox + selld_x, oy + selld_y)
    pag.leftClick()
    for i in range(9):
        pag.moveTo(ox + ok_x, oy + ok_y)
        pag.leftClick()
        sleep(0.2)
        pag.moveTo(ox + yes_x, oy + yes_y)
        pag.leftClick()
        sleep(0.2)
    pag.moveTo(ox + exit_x, oy + exit_y)
    pag.leftClick()


""" Vente Efficace (non fini)"""


# for i in range(9):
#     pag.moveTo(ok_x, ok_y)
#     pag.leftClick()
#     time.sleep(1)
#     img_avg_price = pag.screenshot(region =(580, 247, 60, 20))
#     img_current_price = pag.screenshot(region =(580, 286, 60, 20))
#     avg_price = int(tess.image_to_string(img_avg_price.resize((240, 80))))
#     current_price = int(tess.image_to_string(img_current_price.resize((240, 80))))
#     while current_price <= avg_price :
#         pag.moveTo(no_x, no_y)
#         pag.leftClick()
#         img_avg_price = pag.screenshot(region =(580, 247, 60, 20))
#         img_current_price = pag.screenshot(region =(580, 286, 60, 20))
#         avg_price = int(tess.image_to_string(img_avg_price.resize((240, 80))))
#         current_price = int(tess.image_to_string(img_current_price.resize((240, 80))))
#     pag.moveTo(yes_x, yes_y)
#     pag.leftClick()


def detect_gm(ox, oy):
    if pag.locateOnScreen(path+'GM.png', region=(ox + 255, oy + 180, 240, 120), confidence=0.7) is not None \
            or pag.locateOnScreen(path+'GM1.png', region=(ox + 255, oy + 180, 240, 120), confidence=0.7) is not None:
        return True
    else:
        return False


def detect_player(ox, oy):
    if pag.locateOnScreen(path+'defame.png', region=(ox + 255, oy + 180, 240, 120), confidence=0.7) is not None \
            or pag.locateOnScreen(path+'defame1.png', region=(ox + 255, oy + 180, 240, 120),
                                  confidence=0.7) is not None \
            or pag.locateOnScreen(path+'defame2.png', region=(ox + 255, oy + 180, 240, 120),
                                  confidence=0.7) is not None:
        return True
    else:
        return False


def detect_full_inventory(ox, oy):
    if pag.locateOnScreen(path+'slot9.png', region=(ox + 420, oy + 370, 68, 63)) is None:
        return True
    else:
        return False


def dodge_gm(ox, oy):
    pag.moveTo(ox + cs_x, oy + cs_y)
    pag.leftClick()
    pag.moveTo(ox + exit_x, oy + exit_y)
    pag.leftClick()


def dodge_player(ox, oy):
    pag.moveTo(ox + cs_x, oy + cs_y)
    pag.leftClick()
    pag.moveTo(ox + exit_x, oy + exit_y)
    pag.leftClick()


def start_bot(window_left_coord_x, window_top_coord_y):
    pag.moveTo(window_left_coord_x + exit_x, window_top_coord_y + exit_y)
    pag.leftClick()


def stop_bot(ox, oy):
    imgend = pag.screenshot(region=(ox, oy, 700, 425))
    imgend.save(path+'screenshot.png')
    pag.moveTo(ox + cs_x, oy + cs_y)
    pag.leftClick()


# Fonction de recuperation de photos (peux mieux faire)
def gm_photoshoot(ox, oy, i):
    sleep(.1)
    img = pag.screenshot(region=(ox + 255, oy + 180, 240, 120))
    img.save(path+'screen{}.png'.format(i))
    i += 1
    return i
