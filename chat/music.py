import pygame
from config import *

class Music:
    def __init__(self):
        self.sound_on = True
        self.music_home = pygame.mixer.Sound(MUSIC)
        self.channel = None

    def music_play(self):
        if not self.channel:
            self.channel = self.music_home.play(-1)

    def music_pause(self):
        if self.sound_on and self.channel:
            self.channel.stop()  # Arrêter la musique
            self.channel = None  # Réinitialiser le canal
        else:
            self.channel = self.music_home.play(-1)  # Relancer la musique

        self.sound_on = not self.sound_on  # Inverser l'état du son