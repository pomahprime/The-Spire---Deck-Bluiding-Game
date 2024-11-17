import os

# Déclaration des chemins de base
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))  # Répertoire principal du projet
GRAPHICS_DIR = os.path.join(ROOT_DIR, "Graphics")  # Dossier contenant toutes les ressources graphiques
SOUNDS_DIR = os.path.join(ROOT_DIR, "Sounds")  # Dossier des fichiers audio

# Dossiers spécifiques pour les cartes
CARDS_DIR = os.path.join(GRAPHICS_DIR, "Cards")  # Dossier des cartes
PLAYERS_CARDS_DIR = os.path.join(CARDS_DIR, "Players")  # Sous-dossier des cartes des joueurs
NMIS_CARDS_DIR = os.path.join(CARDS_DIR, "NMIs")  # Sous-dossier des cartes des ennemis

# Dossiers spécifiques pour les fonds d'écran et l'interface utilisateur
BACKGROUND_ROOMS_DIR = os.path.join(GRAPHICS_DIR, "Background - Rooms")  # Dossier des fonds d'écran
UI_DIR = os.path.join(GRAPHICS_DIR, "UI")  # Dossier pour les éléments de l'interface utilisateur

#Dossiers spécifiqques pour les persssonnages
CHAR_DIR = os.path.join(GRAPHICS_DIR, "Characters")
CHAR_PLAYERS = os.path.join(CHAR_DIR, "Players")
CHAR_NMIS = os.path.join(CHAR_DIR, "NMIs")

# Vérification que les répertoires existent
def check_directory(directory):
    if not os.path.exists(directory):
        print(f"Erreur : Le répertoire {directory} n'existe pas.")
    else:
        print(f"Répertoire trouvé : {directory}")

# Vérification des répertoires nécessaires
check_directory(GRAPHICS_DIR)
check_directory(SOUNDS_DIR)
check_directory(CARDS_DIR)
check_directory(PLAYERS_CARDS_DIR)
check_directory(NMIS_CARDS_DIR)
check_directory(BACKGROUND_ROOMS_DIR)
check_directory(UI_DIR)
