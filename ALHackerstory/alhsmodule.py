from PIL import Image, ImageOps
import pyautogui as pag
import pytesseract as tess
from time import sleep

tess.pytesseract.tesseract_cmd = r'C:\Users\guill\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

path = "ALH_images\\"

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


def efficient_sell(ox, oy):
    print("going to Free Market, to sell items")
    pag.moveTo(ox + fm_x, oy + fm_y)
    pag.leftClick()
    pag.moveTo(ox + selld_x, oy + selld_y)
    pag.leftClick()
    for i in range(9):
        pag.moveTo(ox + ok_x, oy + ok_y)
        pag.leftClick()

        # Recuperation et conversion de text en int du prix moyen
        sc = pag.screenshot(region=(ox + 540, oy + 225, 140, 40))
        sc.save(path+'avgp.png')
        img_avg_price = Image.open(path+'avgp.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_avg_price))  # inverting colors + grayscale for precision
        text_avg_price = tess.image_to_string(gray)[14:-1]
        array_avg_price = text_avg_price.split(',')
        avg_price_str = '0.'  # conversion to float first to evade a TypeError
        for element in array_avg_price:
            avg_price_str += element
        avg_price = float(avg_price_str)
        avg_price *= pow(1000, text_avg_price.count(','))
        avg_price *= pow(10, len(array_avg_price[0]))
        avg_price = int(round(avg_price))

        # Recuperation et conversion de text en int du prix propose
        sc = pag.screenshot(region=(ox + 540, oy + 265, 140, 40))
        sc.save(path+'currp.png')
        img_current_price = Image.open(path+'currp.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_current_price))
        text_current_price = tess.image_to_string(gray)[21:-1]
        array_current_price = text_current_price.split(',')
        current_price_str = '0.'
        for element in array_current_price:
            current_price_str += element
        current_price = float(current_price_str)
        current_price *= pow(1000, text_current_price.count(','))
        current_price *= pow(10, len(array_current_price[0]))
        current_price = int(round(current_price))

        sleep(0.1)

        # Comparaison des prix, et maj du prix propose
        while current_price <= avg_price:
            pag.moveTo(ox + no_x, oy + no_y)
            pag.leftClick()
            sc = pag.screenshot(region=(ox + 540, oy + 265, 140, 40))
            sc.save(path+'currp.png')
            img_current_price = Image.open(path+'currp.png')
            gray = ImageOps.grayscale(ImageOps.invert(img_current_price))
            text_current_price = tess.image_to_string(gray)[21:-1]
            array_current_price = text_current_price.split(',')
            current_price_str = '0.'
            for element in array_current_price:
                current_price_str += element
            current_price = float(current_price_str)
            current_price *= pow(1000, text_current_price.count(','))
            current_price *= pow(10, len(array_current_price[0]))
            current_price = int(round(current_price))
            sleep(0.1)
        pag.moveTo(ox + yes_x, oy + yes_y)
        pag.leftClick()
        print(f'Item price {avg_price} sold for {current_price}')
        print(f'We saved {current_price-avg_price}')
        img_avg_price.close()
        img_current_price.close()
    pag.moveTo(ox + exit_x, oy + exit_y)
    pag.leftClick()


def detect_gm(ox, oy):
    if pag.locateOnScreen(path+'GM.png', region=(ox + 255, oy + 180, 240, 120), confidence=0.7) is not None \
            or pag.locateOnScreen(path+'GM1.png', region=(ox + 255, oy + 180, 240, 120), confidence=0.7) is not None\
            or pag.locateOnScreen(path+'GM2.png', region=(ox + 255, oy + 180, 240, 120), confidence=0.7) is not None:
        return True
    else:
        return False


def detect_player(ox, oy):
    if pag.locateOnScreen(path+'defame.png',
                          region=(ox + 255, oy + 180, 240, 120),
                          confidence=0.7) is not None \
            or pag.locateOnScreen(path+'defame1.png',
                                  region=(ox + 255, oy + 180, 240, 120),
                                  confidence=0.7) is not None \
            or pag.locateOnScreen(path+'defame2.png',
                                  region=(ox + 255, oy + 180, 240, 120),
                                  confidence=0.7) is not None:
        return True
    else:
        return False


def detect_full_inventory(ox, oy):
    if pag.locateOnScreen(path+'slot9.png', region=(ox + 420, oy + 370, 68, 68)) is None:
        return True
    else:
        return False


def dodge_gm(ox, oy, gm_encounter_number):
    pag.moveTo(ox + cs_x, oy + cs_y)
    pag.leftClick()
    gm_encounter_number += 1
    pag.moveTo(ox + exit_x, oy + exit_y)
    pag.leftClick()
    return gm_encounter_number


def dodge_player(ox, oy, highrank_player_encounter_number):
    pag.moveTo(ox + cs_x, oy + cs_y)
    pag.leftClick()
    highrank_player_encounter_number += 1
    pag.moveTo(ox + exit_x, oy + exit_y)
    pag.leftClick()
    return highrank_player_encounter_number


def start_bot(game_window_left_coord_x, game_window_top_coord_y):
    pag.moveTo(game_window_left_coord_x + exit_x, game_window_top_coord_y + exit_y)
    pag.leftClick()


def stop_bot(ox, oy):
    pag.moveTo(ox + cs_x, oy + cs_y)
    pag.leftClick()
