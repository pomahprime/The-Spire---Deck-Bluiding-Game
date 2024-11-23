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
############################################################
#                     INITIALISATION DU JEU                #
############################################################

# Initialisation des personnages
liste_joueurs = []
liste_NMIs = []
liste_joueurs.append(Personnage("Img_PJ.png", True ,hp=1, mana=3))
Joueur = liste_joueurs[0]
liste_NMIs.append(Personnage("Img_Npc-Type-01.png", hp=1))



# Création des decks et des autres piles de cartes
# Création Deck Joueur
# Img_Card_00 = pygame.image.load("Card_PJ_Mandale.png").convert_alpha()
# Img_Card_01 = pygame.image.load("Card_PJ_Demacia.png").convert_alpha()

Nb_Espaces = 15
Deck_Joueur = [Carte('Mandale'+" "*(Nb_Espaces-len('Mandale')), "Mandale.png", 1, 5)] * 4 + [Carte('Démontage !!'+" "*(Nb_Espaces-len('Démontage !!')), "demontage.png", 2, 10)] * 2 + [Carte('HIIKKK !'+" "*(Nb_Espaces-len('HIIKKK !')), "HIC.png",1,0,5)] * 3 + [Carte('Armure de feu !'+" "*(Nb_Espaces-len('Armure de feu !')), "Fire_Armor.png",2,5,10)] * 1

# Création Deck Nmi puis attribution et mélange de ce deck à chaque NMI present dans la liste NMI
Deck_NMI = [Carte('Jet d\'acide', "Attack.png", 0, 7)] * 2 + [Carte('Morsure sanglante', "Attack.png", 0, 13)] * 1

for ennemies in liste_NMIs:
    ennemies.Pioche = Deck_NMI[:]
    # Melange Pioche_NMI
    ennemies.melanger_cartes(ennemies.Pioche)
    # Prépare les cartes en main du joueur eyt initialisation de la défausse
    ennemies.pick_card(Nb_cards = 1)
    
# Création Joueur.Pioche
Joueur.Pioche = Deck_Joueur[:]

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
NMIs_alive = False # ---> False pour pas rentrer dans la boucle de jeu 
Players_alive  = True
while NMIs_alive and Players_alive:
    print("\n"*20 + "*" * 110)
    print(f"TOUR : {tour}    |    VOUS AVEZ : {Joueur.hp} PV| {Joueur.armor} DEF | LA CRÉATURE A : {liste_NMIs[0].hp} PV et attaquera à la fin du tour !")
    print(f"{' '*12}|    VOUS AVEZ : {Joueur.mana} MANA{' '*7}|{' '*1}Elle utilisera la carte : {liste_NMIs[0].Main[0].title} infligeant {liste_NMIs[0].Main[0].dmg} PV !")
    print("*" * 110 + "\n"*3)
    print("cartes en MAIN :\n"*1)
    
    # Affiche les cartes en main
    for i, carte in enumerate(Joueur.Main):
        print(f"{i + 1} - {carte}")
    print()
    print("0 - FINIR LE TOUR !\n"*1)
    
    # Demande au joueur de choisir une carte
    choix_carte = None
    
    while choix_carte is None:
        try:
            choix = int(input("\n"*3+"Saisissez le numéro de votre choix , puis appuyez sur la touche **Entrée**"+"\n"*5+"VOTRE CHOIX : ")) - 1
            if choix == -1:  # Fin du tour
                choix_carte = None
                input ("\n"*20+"                    ***** FIN DE VOTRE TOUR *****\n\n                   ***** L'ENNEMI VA JOUER SON TOUR******"+"\n"*10+"(Appuyez sur **Entrée** pour continuer)\n\n")
                break
            elif 0 <= choix < len(Joueur.Main) and Joueur.Main[choix].cost <= Joueur.mana:
                choix_carte = Joueur.Main[choix]
            else:
                input("\n"*20+"Choix invalide ou mana insuffisante."+"\n"*10+"Appuyez sur la touche **Entrée** pour continuer")
        except ValueError:
            input("\n"*20+"Veuillez entrer un nombre valide."+"\n"*10+"Appuyez sur la touche **Entrée** pour continuer")
#             print("Veuillez entrer un nombre valide.")

    if choix_carte:
        # Utilise la carte choisie
        Joueur.mana -= choix_carte.cost
        Joueur.play_card(choix_carte,liste_NMIs[0])
        

        # Si l'ennemi est mort
        if liste_NMIs[0].hp <= 0:
            print(f"Bravo ! Vous avez tué l'ennemi en {tour} tours !")
            break
    else:
        # Fin du tour, l'ennemi attaque *************************************************************************************************
        #print(f"Le tour se termine, l'ennemi attaque  et inflige {NMI.Main[0].dmg} PV !")
        #Joueur.hp = max(0, Joueur.hp - NMI.Main[0].dmg)
        liste_NMIs[0].play_card(liste_NMIs[0].Main[0],Joueur)
        liste_NMIs[0].pick_card(1)
        Joueur.mana = 3  # Recharge le mana DU JOUEUR pour le prochain tour
        tour += 1
        input("\n"*20 +"                                *******************\n"+f"                                ***** TOUR {tour} *****\n"+"                                *******************\n"+"\n"*15+"(Appuyez sur la touche **Entrée** pour conitnuer)\n\n\n")

        # Déplace toutes les cartes de la main à la défausse
        Joueur.Defausse.extend(Joueur.Main)
        Joueur.Main.clear()
        Joueur.pick_card()

# Fin de partie si le joueur perd tous ses points de vie
if Joueur.hp <= 0:
    print(f"Vous avez perdu ! L'ennemi vous a vaincu en seulement {tour} tours !.")
    
    
clock = pygame.time.Clock()

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    screen.blit(resized(image_bg), (0, 0))
    #screen.blit(image_TEST, (0, 0))
    screen.blit(resized(image_Pioche), ((235-pioche_width)*ratio_width,770*ratio_height))
    screen.blit(resized(image_Defausse), ((1920-245)*ratio_width,770*ratio_height))
    screen.blit(resized(image_Mana), ((235-pioche_width)*ratio_width,650*ratio_height))
    screen.blit(resized(image_FDT), ((1920-245)*ratio_width,650*ratio_height))
    screen.blit(resized(liste_NMIs[0].char_visual), (pos_x_npc*ratio_width, pos_y_npc*ratio_height))
    screen.blit(resized(liste_joueurs[0].char_visual), (pos_x_pj*ratio_width, pos_y_pj*ratio_height))
    screen.blit(resized(image_Param), ((1820-param_width-20)*ratio_width,(100+20)*ratio_height))
    screen.blit(resized(image_Life_Bar), (370*ratio_width, 180*ratio_height))  # Position de la barre de vie PJ
    screen.blit(resized(image_Life_Bar), (1000*ratio_width, 180*ratio_height))  # Position de la barre de vie NPC

    # Affichage des cartes avec décalage en x
    screen.blit(resized(Deck_Joueur[1].card_visual), (245*ratio_width, 650*ratio_height))
    for i in range(1, 8):  # 7 fois
        x_position = 245 + i * (card_width + 10)  # Décalage de 10 pixels + largeur de la carte pour chaque carte
        screen.blit(resized(Deck_Joueur[0].card_visual), (x_position*ratio_width, 650*ratio_height))  # Position de départ y=650
        
    #screen.blit(image_Text_Box, (245,580-card_height)) #affiche la boite de texte avec les spécificitées de la carte
    
    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
