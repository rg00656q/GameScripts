# AyumiLove's Hackerstory V1 Bot
## Code ecrit par Guillaume Romero
### Mis a jour le 14/04/2022

### Installation
Comme il s'agit d'un jeu flash, il faut installer au préalable <mark style="background-color: #FFFF00">supernova</mark>.

Passez le lien suivant dans votre navigateur pour lancer le jeu flash :

<mark style="background-color: #FFFF00">url</mark> : 
<mark style="background-color: red">supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250)</mark>

### Le jeu
Le but du jeu est de monter en niveau, tout en évitant les autres joueurs et surtout les Game Masters

Pour ce faire on doit échanger des objets dans le free market

Le trade exp, visible uniquement en passant notre curseur sur le niveau du personnage, permet d'échanger plus rapidement nos objets avec les autres, au meilleur prix

Le mini-jeu du trade exp est important si on utilise une fonction qui vérifie les prix avant de vendre.

### Le bot
Il s'agit d'un bot qui jouera a la place du joueur et ce tant qu'on ne le désactive pas.

Il fonctionne pour la detection du defamer et celle du GM (une défaite est cependant possible).

Il fonctionne aussi pour la vente des objets, mais une erreur est encore envisageable.

<mark style="background-color: #FF0000">Appuyez sur 'q' a tout moment pour arrêter le programme</mark>

##To Do:

    Programming the late game
        - Buff enabler
            - buy cash (redigee mais sors parfois de boucle)
                - Twin coupon (1 000 coin) + teddy cvs (5 000 coin)
                    - Check expiration
                - potions  (coordinates are done, just to code it)
                    - Accuracy -> Amorian Basket (180 000 coin)
                    - Damage -> Onyx Apple (30 000 000 coin ... very late game lol)
        
    Detection based on pixel color change
        + twin coupon on a grid makes it annoying, we have to check multiple colors
        + same for slot9, we have to check an other pixel depending of the item in it
        - faster than checking 10 pictures (3 for each person/group to verify)
        - can be done for everything so overall better

    automated equipment progression

## Credits
Le jeu AyumiLove's HackerStory V1 est un jeu de AyumiLove.

Il est hébergé sur la plateforme www.kongregate.com.

Les images du jeu viennent de MapleStory, un jeu de NEXON.