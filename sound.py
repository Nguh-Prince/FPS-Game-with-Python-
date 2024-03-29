import pygame as pg
from settings import *

class Sound:
    def __init__(self, game) -> None:
        self.game = game
        pg.mixer.init()
        self.path = os.path.join(
            abs_folder_path, 'resources/sound/'
        )
        self.shotgun = pg.mixer.Sound(os.path.join(self.path, 'shotgun.wav'))