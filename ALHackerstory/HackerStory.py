# supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250
"""
Code ecrit par Guillaume Romero
Le 11/04/2022
Mis a jour le 11/04/2022

Le jeu AyumiLove's HackerStory V1 est un jeu de AyumiLove, tous les droits lui sont reserves.
Il se joue sur la plateforme www.kongregate.com/, mais comme il s'agit d'un jeu flash
    Il faut installer au prealable supernova
    Et utiliser le lien au tout debut du fichier
Les images du jeu viennent de MapleStory, un jeu de NEXON

Il s'agit d'un bot qui jouera a la place du joueur et ce tant qu'on ne le desactive pas.
    Il fonctionne pour la detection du defamer, pas encore celle du GM (une defaite est encore possible)
    La fonctionnalite pour la vente efficace est encore en cours de codage
Appuyez sur 'q' a tout moment pour arreter le programme

To Do:
    Coder evasion GM
        - obtenir images GM
            -> 1/2
    Coder vente efficace
    Coder appui clavier en fonction de la place de l'ecran de jeu
        - locateonscreen avec une image du jeu
    faire un module avec le code dedans
        - fonction de detection
        - fonction d'esquive
            compteurs?
    changer d'equipement par palier?
"""

from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\guill\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import pyautogui as pag
import time
import keyboard

""" On va attendre le changement de couleur du pixel de la zone a regarder """
# Game screens
ox, oy = (0, 0)  # Point de depart, jeu au coin superieur gauche
wx, wy = (699, 420)  # fenetre de jeu

# print(pag.position())

""" Cash Shop buttons list """
cs_x, cs_y = (608, 281)  # Cash Shop button (to use Cash)
pet_x, pet_y = (60, 358)  # Pet and Hack buttons
etc_x, etc_y = (140, 358)  # ETC and Scroll buttons
npc_x, npc_y = (218, 358)  # NPC and Buy Equip buttons
exit_x, exit_y = (620, 381)  # Exit button

""" free market buttons list """
fm_x, fm_y = (610, 237)  # Free Market button
selld_x, selld_y = (300, 358)  # Sell Drops button
fame_x, fame_y = (380, 358)  # Fame button
cash_x, cash_y = (460, 358)  # Cash button (to buy Cash)

""" Coordonnees des bouttons de vente """
ok_x, ok_y = (675, 195)
yes_x, yes_y = (580, 330)
no_x, no_y = (645, 330)


""" Boucle de ventes multiples (pour vendre les 9 slots) """
""" Vente rapide """
def fast_sell():
    for i in range(9):
        pag.moveTo(ok_x, ok_y)
        pag.leftClick()
        time.sleep(0.2)
        pag.moveTo(yes_x, yes_y)
        pag.leftClick()
        time.sleep(0.2)

""" Vente pre Efficace """
def efficient_sell():
    for i in range(9):
        pag.moveTo(ok_x, ok_y)
        pag.leftClick()
        time.sleep(0.2)
        img_avg_price = pag.screenshot(region=(580, 247, 60, 20))
        img_current_price = pag.screenshot(region=(580, 286, 60, 20))
        while tess.image_to_string(img_current_price) != tess.image_to_string(img_avg_price):
            pag.moveTo(no_x, no_y)
            pag.leftClick()
            img_avg_price = pag.screenshot(region=(580, 247, 60, 20))
            img_current_price = pag.screenshot(region=(580, 286, 60, 20))
            time.sleep(0.2)
        pag.moveTo(yes_x, yes_y)
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



# A utiliser de preference dans le cash shop ou FM

pag.moveTo(exit_x, exit_y)
pag.leftClick()     # Sortie du CS
while keyboard.is_pressed('q') == False:
    if pag.locateOnScreen('ALH_images\defame.png',region=(255, 180, 240, 120), confidence=0.7) != None \
            or pag.locateOnScreen('ALH_images\defame1.png',region=(255, 180, 240, 120), confidence=0.7) != None\
            or pag.locateOnScreen('ALH_images\defame2.png', region=(255, 180, 240, 120), confidence=0.7) != None:
        print("I saw a Defamer")
        pag.moveTo(cs_x, cs_y)
        pag.leftClick()
        pag.moveTo(exit_x, exit_y)
        pag.leftClick()
    elif pag.locateOnScreen('ALH_images\slot9.png', region=(420, 365, 68, 63)) == None:
        print("going to Free Market")
        pag.moveTo(fm_x, fm_y)
        pag.leftClick()
        print("Time to sell!")
        pag.moveTo(selld_x, selld_y)
        pag.leftClick()
        fast_sell()
        print("Done!")
        pag.moveTo(exit_x, exit_y)
        pag.leftClick()
imgend = pag.screenshot(region=(255, 180, 260, 120))
imgend.save('ALH_images\screenshot.png')
pag.moveTo(cs_x, cs_y)
pag.leftClick()

""" Code pour la detection du Game Master """
# while keyboard.is_pressed('q') == False:
#     if pag.locateOnScreen('ALH_images\GM.png', confidence=0.7) != None:
#         print("I see Him!")
#         time.sleep(0.5)
#     else:
#         print("I do not see him")
#         time.sleep(0.5)
