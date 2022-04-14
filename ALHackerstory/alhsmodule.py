from PIL import Image, ImageOps
import pyautogui as pag
import pytesseract as tess
from time import sleep

tess.pytesseract.tesseract_cmd = r'C:\Users\guill\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

path = "ALH_images\\"

# Game screens
wx, wy = (700, 425)  # fenêtre de jeu
pix_detect_x, pix_detect_y = (470, 246)  # Coordonnées du point d'apparition des ennemis

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

""" Coordonnées des boutons de vente """
ok_x, ok_y = (675, 200)
yes_x, yes_y = (585, 330)
no_x, no_y = (645, 330)


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


""" Boucle de ventes multiples (pour vendre les 9 slots) """


def gather_price(ox, oy, price_type):
    if price_type == 'average':
        sc = pag.screenshot(region=(ox + 540, oy + 225, 140, 40))
        sc.save(path + 'price.png')
        img_price = Image.open(path + 'price.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_price))  # inverting colors + grayscale for precision
        text_price = tess.image_to_string(gray)[14:-1]
    else:
        sc = pag.screenshot(region=(ox + 540, oy + 265, 140, 40))
        sc.save(path + 'price.png')
        img_price = Image.open(path + 'price.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_price))
        text_price = tess.image_to_string(gray)[21:-1]

    array_price = text_price.split(',')
    price_str = '0.'  # conversion to float first to evade a TypeError
    for element in array_price:
        price_str += element.strip('\n')
    price = float(price_str)
    price *= pow(1000, text_price.count(','))
    price *= pow(10, len(array_price[0].strip('\n')))
    price = int(round(price))
    img_price.close()
    return price


def efficient_sell(ox, oy):
    print("going to Free Market, to sell items")
    pag.moveTo(ox + fm_x, oy + fm_y)
    pag.leftClick()
    pag.moveTo(ox + selld_x, oy + selld_y)
    pag.leftClick()
    for i in range(9):
        pag.moveTo(ox + ok_x, oy + ok_y)
        pag.leftClick()
        avg_price = gather_price(ox, oy, 'average')
        current_price = gather_price(ox, oy, 'current')

        # Comparaison des prix, et maj du prix propose
        while current_price <= avg_price:
            pag.moveTo(ox + no_x, oy + no_y)
            pag.leftClick()
            current_price = gather_price(ox, oy, 'current')
            sleep(0.1)

        pag.moveTo(ox + yes_x, oy + yes_y)
        pag.leftClick()
        print(f'Item price {avg_price} sold for {current_price}')
        print(f'We saved {current_price - avg_price} mesos')
    pag.moveTo(ox + exit_x, oy + exit_y)
    pag.leftClick()


def omni_detect(ox, oy):
    if pag.pixel(int(ox + pix_detect_x), int(oy + pix_detect_y))[0] != 255:
        return True
    else:
        return False


def dodge(ox, oy):
    pag.moveTo(ox + cs_x, oy + cs_y)
    pag.leftClick()
    pag.moveTo(ox + exit_x, oy + exit_y)
    pag.leftClick()


def detect_full_inventory(ox, oy):
    if pag.locateOnScreen(path + 'slot9.png', region=(ox + 420, oy + 370, 68, 68)) is None:
        return True
    else:
        return False


def start_bot(game_window_left_coord_x, game_window_top_coord_y):
    pag.moveTo(game_window_left_coord_x + exit_x, game_window_top_coord_y + exit_y)
    pag.leftClick()


def stop_bot(ox, oy):
    pag.moveTo(ox + cs_x, oy + cs_y)
    pag.leftClick()
