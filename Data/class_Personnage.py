import pygame
import os
import sys
from random import shuffle

# Ajoute le dossier racine du projet au chemin d'import
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

# Importe les modules
from config import *
from utils import load_image
# Classe de base pour les personnages du jeu
class Personnage:
    def __init__(self, char_visual, human = False, archetype = 0, hp = 0, mana=0, armor=0):
        self.human = human
        self.archetype = archetype
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.Pioche = []
        self.Defausse = []
        self.Main = []
        if human:
            self.nom = "Human"
            self.char_visual = load_image(f"{char_visual}", CHAR_PLAYERS)
        else:
            self.nom = "Alien"
            self.char_visual = load_image(f"{char_visual}", CHAR_NMIS)

            
        self.pos_x = 400
        self.pos_y = 350
        
        self.interact_area = pygame.Rect(self.pos_x-100, 0, self.pos_x+100, self.pos_y)
        
    def play_card(self,carte_i,cible): #,liste_joueurs,liste_Nmis,liste_elements_jeu
        """obj_carte , cible = obj perso.cible"""
        damage_to_hp = max(0, carte_i.dmg - cible.armor)
        cible.armor = max(0, cible.armor - carte_i.dmg)
        cible.hp -= damage_to_hp
        
            
        self.armor += carte_i.arm
        self.Defausse.append(carte_i)
        self.Main.remove(carte_i)
        input("\n"*20+ " "*19+f"{self.nom} utilise la carte :\n"+ " "*19+F"[{carte_i.title}] : coût MANA : {carte_i.cost} | Dégâts : +{carte_i.dmg} | Défense : +{carte_i.arm} \n\n"+" "*19+f"{self.nom} possède maintenant : {self.mana} MANA \n\n\n                   {cible.nom} reçoit {damage_to_hp} dégâts, et il lui reste {cible.hp} pv"+"\n"*8+" (Appuyez sur la touche **Entrée ** pour continuer)"+"\n"*6)
#         print(f"Défenseur reçoit {damage} dégâts, et il lui reste {cible.hp} pv ")
        
    def pick_card(self,Nb_cards = 4):
        
        if len(self.Pioche) < Nb_cards:
            self.melanger_cartes(self.Defausse)
            self.Pioche.extend(self.Defausse)
            self.Defausse.clear()
        # Pioche les nouvelles cartes
        self.Main = [self.Pioche.pop(0) for _ in range(min(Nb_cards, len(self.Pioche)))]
       
    
    # Fonction pour mélanger les cartes d'une liste
    def melanger_cartes(self,liste_cartes_melange):
        shuffle(liste_cartes_melange)
