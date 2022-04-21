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


def getprice(price_type):
    if price_type == 'average':
        sc = pag.screenshot(region=(al.getglob_x() + 540, al.getglob_y() + 225, 140, 40))
        sc.save(al.path + 'screenshot.png')
        img_price = Image.open(al.path + 'screenshot.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_price))  # inverting colors + grayscale for precision
        text_price = tess.image_to_string(gray)[14:]
    else:
        sc = pag.screenshot(region=(al.getglob_x() + 540, al.getglob_y() + 265, 140, 40))
        sc.save(al.path + 'screenshot.png')
        img_price = Image.open(al.path + 'screenshot.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_price))
        text_price = tess.image_to_string(gray)[20:]
    price = al.text_to_int(text_price)
    img_price.close()
    return price


def getmoney(money_type):
    if money_type == 'meso':
        sc = pag.screenshot(region=(al.getglob_x() + 535, al.getglob_y() + 30, 140, 25))
        sc.save(al.path + 'screenshot.png')
        img_money = Image.open(al.path+'screenshot.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_money))
        text_money = tess.image_to_string(gray)[7:]
    else:
        sc = pag.screenshot(region=(al.getglob_x() + 535, al.getglob_y() + 45, 140, 25))
        sc.save(al.path + 'screenshot.png')
        img_money = Image.open(al.path+'screenshot.png')
        gray = ImageOps.grayscale(ImageOps.invert(img_money))
        text_money = tess.image_to_string(gray)[7:]
    money = al.text_to_int(text_money)
    img_money.close()
    return money


def efficient_sell(savings):
    print("going to Free Market, to sell items")
    al.click(fm_x, fm_y)
    al.click(selld_x, selld_y)
    try:
        for i in range(9):
            al.click(ok_x, ok_y)
            avg_price = getprice('average')
            current_price = getprice('current')

            # Comparaison des prix, et maj du prix propose
            while current_price <= avg_price:
                al.click(no_x, no_y)
                current_price = getprice('current')
                if current_price == 0 and avg_price == 0:
                    raise al.PictureError()
                sleep(0.1)

            al.click(yes_x, yes_y)
            savings += current_price - avg_price
    except al.PictureError as pe:
        print('Error : no numbers on the game trading screen')
    finally:
        al.click(al.exit_x, al.exit_y)
    return savings


def buy_cash(savings):
    print("going to Free Market, to buy coins")
    al.click(fm_x, fm_y)
    al.click(cash_x, cash_y)
    al.click(item_selector_x, item_selector_y)
    al.click(amorian_basket_x, amorian_basket_y)
    al.click(ok_x, ok_y)

    money = getmoney('meso')

    avg_price = getprice('average')

    while money >= avg_price:
        current_price = getprice('current')
        while current_price >= avg_price:
            al.click(no_x, no_y)
            current_price = getprice('current')
            sleep(0.2)
        al.click(yes_x, yes_y)
        savings += (avg_price - current_price)

        al.click(ok_x, ok_y)

        money = getmoney('meso')

        avg_price = getprice('average')
        sleep(0.2)

    al.click(al.exit_x, al.exit_y)


def buy_buffs():
    al.click(al.cs_x, al.cs_y)
    al.click(etc_x, etc_y)
    al.click(ok_x, ok_y)
    al.click(cs_yes_x, cs_yes_y)
    al.click(npc_x, npc_y)
    al.click(item_selector_x, item_selector_y)
    al.click(onyx_apple_x, onyx_apple_y)
    sleep(.1)
    al.click(ok_x, ok_y)
    al.click(cs_yes_x, cs_yes_y)
    al.click(item_selector_x, item_selector_y)
    al.click(amorian_basket_x, amorian_basket_y)
    sleep(.1)
    al.click(ok_x, ok_y)
    al.click(cs_yes_x, cs_yes_y)
    al.click(al.exit_x, al.exit_y)
