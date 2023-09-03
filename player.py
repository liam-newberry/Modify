# File created by: Liam Newberry
# from eyed3 import load as e3
import pygame as pg
# import os
# import io

from folder_funcs import *
from player_settings import *

class Player:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption("Title")
        # pg.display.set_icon(icon)
    def new(self):
        pass
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.should_quit = True
    def update(self):
        self.now = pg.time.get_ticks()
    def draw(self):
        self.screen.fill(BLACK)
        x = pg.image.load(get_song_info("a0700f226d5341f9")["image"]).convert()
        # pg.transform.scale(x,(100,100))
        self.screen.blit(x,x.get_rect())
        pg.display.flip()
    def run(self):
        self.should_quit = False
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        return self.should_quit