from config import PLAYERS_CARDS_DIR, NMIS_CARDS_DIR, SOUNDS_DIR, BACKGROUND_ROOMS_DIR, UI_DIR
from utils import load_image
from Data.class_Carte import Carte
from Data.class_Personnage import Personnage
import pygame 
import os


###########################################################
#                       PYGAME INIT                       #
###########################################################



pygame.init()
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
ratio_width, ratio_height = screen_width/1920, screen_height/1080
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
###########################################################
#                 Chargement des images                   #
###########################################################
#interface
image_bg = load_image("Img_Background-plus-safe-frame-areas.png", BACKGROUND_ROOMS_DIR)
# image_TEST = pygame.image.load("decor-fake-test.png")
#####card_visual_player = load_image("Attack.png", PLAYERS_CARDS_DIR)
image_Life_Bar = load_image("Img_Life-Bar-Background.png", UI_DIR)
image_Pioche = load_image("Img_Pioche.png", UI_DIR).convert_alpha()
image_Defausse = load_image("Img_Defausse.png", UI_DIR).convert_alpha()
image_FDT = load_image("Img_Fin_tour.png", UI_DIR).convert_alpha()
image_Mana = load_image("Img_Player_Stamina.png", UI_DIR).convert_alpha()
image_Param = load_image("Img_Btn_Parameter.png", UI_DIR).convert_alpha()
image_Text_Box = load_image("Img_Bulle_Texte_Carte.png", UI_DIR).convert_alpha()
#cartes joueur

# Img_Card_00 = pygame.image.load("Card_PJ_Mandale.png").convert_alpha()
# Img_Card_01 = pygame.image.load("Card_PJ_Demacia.png").convert_alpha()


#################################################
######       MODIFICATION TAILLE IMG       ######
#################################################
def resized(image):
    """
    prend une image en parametre qui doit etre load avant,
    permet de modifier la taille de l'image selon le ratio de la définition de l'écran actuel.
    """
    return pygame.transform.scale(image, (image.get_width()*ratio_width, image.get_height()*ratio_height))

# Calcul de la largeur de l'image de la carte
card_width = 169 #Img_Card_00.get_width()
card_height = 271 #Img_Card_00.get_height()
pioche_width = image_Pioche.get_width()
param_width = image_Param.get_width()
param_height = image_Param.get_height()

print("TAILLE ECRAN : ", screen_width, screen_height)
print("RATIOS : ",ratio_width, ratio_height)
# Message d'introduction
#input("\n\n\n\n\n\n                                          Tuez la créature ennemie avant qu'elle ne vous tue !\n\n\n\n Durant votre tour : \n - Jouez autant de vos cartes en MAIN que votre MANA le permet, (Chaque carte ayant son propre coût de MANA)\n - A tout moment, finissez votre tour de jeu en appuyant sur le chiffre 0,\n\n\n [ATTENTION] \n - L'Ennemi joue son attaque quand vous finissez votre tour ! \n\n\n\n\n(...appuyez sur la touche **Entrée** pour continuer)\n\n\n ")
#MESSAGE D'INTRO ^^^
def all_dead(liste_pers):
    for perso in liste_pers:
        if perso.hp > 0: 
            return False
    return True

def display(name_image,x,y):
    """affiche une image à une position x et y d'une taille ecran standrad de 1920x1080, puis l'adapte à l'écran courant grace au ratio,
    prend en parametre le nom de la varible qui stock l'image load, x et qui et y qui sont des positions 
    """
    screen.blit((resized(name_image)),(x*ratio_width,y*ratio_height))
    
    #cards_anchor = (screen_width / 2) - (len(player.Main)*(card_width/2)) 
def display_player_hand(player_hand):
    cards_anchor = (screen_width / 2) - len(player_hand)*(card_width*ratio_width)/2 + (10 * len(player_hand))
    for i in range(len(player_hand)):
        #x_position = cards_anchor + i * (card_width + 10)  # Décalage de 10 pixels + largeur de la carte pour chaque carte
        x_position = cards_anchor + i * (card_width + 10)  # Décalage de 10 pixels + largeur de la carte pour chaque carte
        display(player_hand[i].card_visual, x_position, 650)  # Position de départ y=650
    
############################################################
#                     INITIALISATION DU JEU                #
############################################################

# Initialisation des personnages
# liste_joueurs = []
liste_NMIs = []
# liste_joueurs.append(
Joueur = Personnage("Img_PJ.png", True ,hp=1, mana=3)
# Joueur = liste_joueurs[0]
liste_NMIs.append(Personnage("Img_Npc-Type-01.png", hp=1))
NMI_0 = liste_NMIs[0]



# Création des decks et des autres piles de cartes
# Création Deck Joueur
Deck_joueur_01 = [Carte('Mandale', "Mandale.png", 1, 5)] * 1 + [Carte('Démontage !!', "demontage.png", 2, 10)] * 2 + [Carte('HIIKKK !', "HIC.png",1,0,5)] * 3 + [Carte('Armure de feu !', "Fire_Armor.png",2,5,10)] * 1
Joueur.Pioche.extend(Deck_joueur_01)
# Création Deck Nmi puis attribution et mélange de ce deck à chaque NMI present dans la liste NMI
NMI_0.Pioche = [Carte('Jet d\'acide', "Attack.png", 0, 7, human_card = False)] * 2 + [Carte('Morsure sanglante', "Attack.png", 0, 13, human_card = False)] * 1

# Melange Joueur.Pioche
Joueur.melanger_cartes(Joueur.Pioche)

# Prépare les cartes en main du joueur eyt initialisation de la défausse
Joueur.pick_card()



###################################################################
#                      BOUCLE PRINCIPALE                          #
###################################################################

tour = 1

###################################################################
#                           INTERFACE                             #
###################################################################
#boucle pour une salle_combat : tant que le joueur ou l'ennemi (gestion enemi unique pour le moment) sont en vie le combaty perdure.
NMIs_alive = True # ---> False pour pas rentrer dans la boucle de jeu 
Players_alive  = True

clock = pygame.time.Clock() # gere les FPS     
while running: 
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    #while NMIs_alive and Players_alive :
# Positions des personnages
    pos_x_pj = 400
    pos_y_pj = 350
    pos_x_npc = 1000
    pos_y_npc = 350
    
    # Gestion des touches pour déplacer les personnages
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        pos_x_pj += 15
    if pressed[pygame.K_q]:
        pos_y_pj += 10
    if pressed[pygame.K_p]:
        pos_x_npc -= 15
    if pressed[pygame.K_m]:
        pos_y_npc += 10
    
    # Affichage des images de fond et des personnages
    display(image_bg, 0, 0)
    #screen.blit(image_TEST, (0, 0))
    display(image_Pioche, (235-pioche_width),770)
    display(image_Defausse, (1920-245),770)
    display(image_Mana, (235-pioche_width),650)
    display(image_FDT, (1920-245),650)
    display(liste_NMIs[0].char_visual, pos_x_npc, pos_y_npc)
    display(Joueur.char_visual, pos_x_pj, pos_y_pj)
    display(image_Param, (1820-param_width-20),(120))
    display(image_Life_Bar, 370, 180)  # Position de la barre de vie PJ
    display(image_Life_Bar, 1000, 180)  # Position de la barre de vie NPC
    display_player_hand(Joueur.Main)

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
"""PROCHAINE SESION : mettre le ratio au moment du loading de l'image"""