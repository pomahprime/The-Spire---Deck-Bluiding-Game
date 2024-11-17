import os
import pygame


# Exemple de chargement d'images
# card_visual_player = load_image("Attack.png", PLAYERS_CARDS_DIR)
# card_visual_npc = load_image("JetAcide.png", NPC_CARDS_DIR)

def load_image(image_name, directory):
    image_path = os.path.join(directory, image_name)
    if os.path.exists(image_path):
        return pygame.image.load(image_path).convert_alpha()
    else:
        print(f"Erreur : Le fichier {image_path} n'a pas été trouvé.")
        return None
    



# Exemple de chargement de son
# attack_sound = load_sound("attack_sound.wav", SOUNDS_DIR)
# Exemple de fonction pour charger un son
def load_sound(sound_name, directory):
    sound_path = os.path.join(directory, sound_name)
    if os.path.exists(sound_path):
        return pygame.mixer.Sound(sound_path)
    else:
        print(f"Erreur : Le fichier {sound_path} n'a pas été trouvé.")
        return None