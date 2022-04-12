# supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250
"""
Code ecrit par Guillaume Romero
Le 11/04/2022
Mis a jour le 12/04/2022

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
    Coder evasion GM efficace
        - obtenir images GM
            -> 1/4
    Coder vente efficace
    compteurs dans le module?
    changer d'equipement par palier?
"""

import alhsmodule as alhs
import keyboard

i = 0
ox, oy = alhs.locate_game()
alhs.start_bot(window_left_coord_x=ox, window_top_coord_y=oy)
while not keyboard.is_pressed('q'):
    if alhs.detect_gm(ox, oy):
        i = alhs.gm_photoshoot(ox, oy, i)
        alhs.dodge_gm(ox, oy)
        print("Woop woop!")
        print("Po-po eluded")
    elif alhs.detect_player(ox, oy):
        alhs.dodge_player(ox, oy)
        print("dodged a player")
    elif alhs.detect_full_inventory(ox, oy):
        alhs.fast_sell(ox, oy)
        print("Done!")
alhs.stop_bot(ox, oy)
