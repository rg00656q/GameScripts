# AyumiLove's Hackerstory V1 Bot
## Code écrit par Guillaume Romero
### Ceci est mon premier projet de bot pour maitriser Python
### Mis a jour le 21/04/2022

### Version 3
q to quit

w to convert all mesos into cash

e to buy buffs

Enemy checking is done

automatic selling is done (though it still bugs sometimes)

Buying important items is done

###Improvements:

    Too much informations to check will lead to not enough time to check everything
        -> you may get banned because of the code causing slowness
            + Coding only pixel checks
            + Reducing images to check
        
    Detection based on pixel color change
        + twin coupon on a grid makes it annoying, we have to check multiple colors
        + same for slot9, we have to check an other pixel depending of the item in it
        - faster than checking 10 pictures (3 for each person/group to verify)
        - can be done for everything so overall better

    automated equipment progression
        + faster game plan
        - checks images again, so might get banned

## FRANCAIS
### Installation
Comme il s'agit d'un jeu flash, il faut installer au préalable <mark style="background-color: #FFFF00">supernova</mark>.

Passez le lien suivant dans votre navigateur pour lancer le jeu flash :

<mark style="background-color: #FFFF00">url</mark> : 
<mark style="background-color: red">supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250)</mark>

### Le jeu
Le but du jeu est de monter en niveau, tout en évitant les autres joueurs et surtout les Game Masters.

Pour ce faire on doit échanger des objets dans le free market.

Le trade exp, visible uniquement en passant notre curseur sur le niveau du personnage, permet d'échanger plus rapidement nos objets avec les autres, au meilleur prix.

Le mini-jeu du trade exp est important si on utilise une fonction qui vérifie les prix avant de vendre.

### Le bot
Il s'agit d'un bot qui jouera a la place du joueur et ce tant qu'on ne le désactive pas.

Il fonctionne pour la detection du defamer et celle du GM (une défaite est cependant possible).

Il fonctionne aussi pour la vente des objets.

Le bot peut se permettre de verifier 1 image, avec plus sa réactivité en est affaiblie.

<mark style="background-color: #FF0000">Appuyez sur 'q' a tout moment pour arrêter le programme</mark>

### Credits
Le jeu AyumiLove's HackerStory V1 est un jeu de AyumiLove.

Il est hébergé sur la plateforme www.kongregate.com.

Les images du jeu viennent de MapleStory, un jeu de NEXON.

## English
### Installation
As this game is a flash game, we have to install <mark style="background-color: #FFFF00">supernova</mark> beforehand.

Then just copy-paste the following link in your browser to start the game :

<mark style="background-color: #FFFF00">url</mark> : 
<mark style="background-color: red">supernova://play/?swfurl=http://chat.kongregate.com/gamez/0003/2079/live/ayumilove_hackerstory2_secure.swf?kongregate_game_version=1230090250)</mark>

### The game
The goal of the game is to level up, while dodging other players and the Game Masters.

To aid us we have the Free Market to exchange items.

Trade exp, only visible when we hover our mouse over the level of our character, allows us to exchange faster our items, and at better prices.

The mini-game of trade exp is important as it starts slow but gives more results on our money over time.

### The bot
It is simply a bot that plays instead of the player, and until we tell him to stop.

It detects the players and Game Masters (but a defeat might still be possible).

It works for items selling.

The bot can check 1 picture, but with more pictures its efficiency drops.

### Credits
The game AyumiLove's HackerStory V1 is a game of Ayumilove.

It is hosted on www.kongregate.com

The pictures of the game are from Maplestory, a NEXON game.

### Last words
It was a lot of fun coding this bot, even though all my ideas could not come to life.

In the next bot I'll try to use pillow more for the image capture, instead of pyautogui.

For all codes, we have to change a few details for it to run perfectly