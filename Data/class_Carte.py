import pygame
import os
import sys

# Ajoute le dossier racine du projet au chemin d'import
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

# Importe les modules
from config import PLAYERS_CARDS_DIR, NMIS_CARDS_DIR, SOUNDS_DIR, BACKGROUND_ROOMS_DIR, UI_DIR
from utils import load_image
# Classe Carte
class Carte:
    def __init__(self, title, card_visual, cost, dmg=0, arm=0, one_shot=False, unlock=True, card_lvl=1, card_type=0, replicable=True, rarity=0, id_nb_card = 0, human_card = True):
        """
        Initialise une nouvelle carte avec les caractéristiques spécifiées.

        Paramètres :
        ------------
        title : str
            Nom ou titre de la carte.
        cost : int
            Coût en ressources pour utiliser ou jouer la carte.
        dmg : int, optionnel
            Points de dégâts infligés par la carte (par défaut : 0).
        arm : int, optionnel
            Points d'armure ou de protection accordés par la carte (par défaut : 0).
        one_shot : bool, optionnel
            Indique si la carte est à usage unique (par défaut : False).
        unlock : bool, optionnel
            Statut de déblocage de la carte, True si disponible dans la collection (fichier chargé en mémoire à l'init)(par défaut : True).
        card_lvl : int, optionnel
            Niveau de la carte (par défaut : 1).
        card_type : int, optionnel
            Type de la carte // 0 = Action / 1 = Pouvoir / 2 = Piège (par défaut : 0).
        replicable : bool, optionnel
            Indique si la carte peut être copiée ou dupliquée (par défaut : True).
        rarity : int, optionnel
            Rareté de la carte (par défaut : 0).
        id_nb_card : int, optionnel
            Indique la clé numérique de la carte (par défaut : 0)
        card_visual : str , OBLIGATOIRE, prend le nom réel dans le dossier de l'ordinateur
            charge en mémoire le visuel de la carte.
        """
        self.title = title
        self.cost = cost
        self.dmg = dmg
        self.arm = arm
        self.one_shot = one_shot
        self.unlock = unlock
        self.card_lvl = card_lvl
        self.card_type = card_type
        self.replicable = replicable
        self.rarity = rarity
        self.id_nb_card = id_nb_card
        if human_card:
            self.card_visual = load_image(f"{card_visual}", PLAYERS_CARDS_DIR) # nom du fichier de la carte sur le pc + son extension (ex : .png)
        else:
            self.card_visual = load_image(f"{card_visual}", NMIS_CARDS_DIR) # nom du fichier de la carte sur le pc + son extension (ex : .png)
        

    def __str__(self):
        # Retourne les infos de la carte
#         if self.dmg == 0:
        return f"{self.title}||Dégâts : {self.dmg} ||Défense : {self.arm} ||Coût MANA : {self.cost} "
        return f"\n\'#'*50\n'#'*1 Tour  {tour}\n\n "
#         else:
#             return f"{self.title}, coût MANA : {self.cost}, Dégâts : {self.dmg}"

