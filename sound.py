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
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.3)