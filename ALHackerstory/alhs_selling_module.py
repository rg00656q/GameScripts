from PIL import Image, ImageOps
import pyautogui as pag
import pytesseract as tess
from time import sleep
import alhs_commands as al
tess.pytesseract.tesseract_cmd = r'C:\Users\guill\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

""" cash shop buttons list """
pet_x, pet_y = (60, 358)  # Pet and Hack buttons
etc_x, etc_y = (140, 358)  # ETC and Scroll buttons
npc_x, npc_y = (218, 358)  # NPC and Buy Equip buttons
item_selector_x, item_selector_y = (580, 194)  # Menu defilant
onyx_apple_x, onyx_apple_y = (580, 260)  # Option 3 du menu
amorian_basket_x, amorian_basket_y = (580, 330)  # Option 6 du menu
cs_yes_x, cs_yes_y = (610, 305)
""" free market buttons list """
fm_x, fm_y = (610, 250)  # Free Market button
selld_x, selld_y = (300, 358)  # Sell Drops button
fame_x, fame_y = (385, 358)  # Fame button
cash_x, cash_y = (470, 358)  # Cash button (to buy Cash)
""" Coordonnées des boutons de vente """
ok_x, ok_y = (675, 200)
yes_x, yes_y = (585, 330)
no_x, no_y = (645, 330)



def gather_price(price_type):
    if price_type == 'average':
        sc = pag.screenshot(region=(al.getglob_x() + 540, al.getglob_y() + 225, 140, 40))
        sc.save(al.path + 'price.png')
        img_price = Image.open(al.path + 'price.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_price))  # inverting colors + grayscale for precision
        text_price = tess.image_to_string(gray)[14:]
    else:
        sc = pag.screenshot(region=(al.getglob_x() + 540, al.getglob_y() + 265, 140, 40))
        sc.save(al.path + 'price.png')
        img_price = Image.open(al.path + 'price.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_price))
        text_price = tess.image_to_string(gray)[20:]
    price = al.text_to_int(text_price)
    img_price.close()
    return price


def efficient_sell(savings):
    print("going to Free Market, to sell items")
    al.click(fm_x, fm_y)   # ?
    al.click(selld_x, selld_y)
    for i in range(9):
        al.click(ok_x, ok_y)
        avg_price = gather_price('average')
        current_price = gather_price('current')

        # Comparaison des prix, et maj du prix propose
        while current_price <= avg_price:
            al.click(no_x, no_y)
            current_price = gather_price('current')
            sleep(0.1)

        al.click(yes_x, yes_y)
        savings += current_price - avg_price
    al.click(al.exit_x, al.exit_y)
    return savings


def buy_cash(savings):
    print("going to Free Market, to buy coins")
    al.click(fm_x, fm_y)
    al.click(cash_x, cash_y)
    al.click(item_selector_x, item_selector_y)
    al.click(amorian_basket_x, amorian_basket_y)
    al.click(ok_x, ok_y)

    img = pag.screenshot(region=(al.getglob_x() + 535, al.getglob_y() + 30, 140, 25))
    img.save(al.path+'price.png')
    img = Image.open(al.path+'price.png')
    img = ImageOps.grayscale(ImageOps.invert(img))
    text_money = tess.image_to_string(img)[7:]
    money = al.text_to_int(text_money)

    avg_price = gather_price('average')

    while money >= avg_price:
        current_price = gather_price('current')
        while current_price >= avg_price:
            al.click(no_x, no_y)
            current_price = gather_price('current')
            sleep(0.2)
        al.click(yes_x, yes_y)
        savings += (avg_price - current_price)

        al.click(ok_x, ok_y)

        img = pag.screenshot(region=(al.getglob_x() + 535, al.getglob_y() + 30, 140, 25))
        img.save(al.path+'price.png')
        img = Image.open(al.path+'price.png')
        img = ImageOps.grayscale(ImageOps.invert(img))
        text_money = tess.image_to_string(img)[7:]
        money = al.text_to_int(text_money)

        avg_price = gather_price('average')
        sleep(0.2)

    al.click(al.exit_x, al.exit_y)


def buy_twc():
    al.click(al.cs_x, al.cs_y)
    al.click(etc_x, etc_y)
    al.click(ok_x, ok_y)
    al.click(cs_yes_x, cs_yes_y)
    al.click(al.exit_x, al.exit_y)
