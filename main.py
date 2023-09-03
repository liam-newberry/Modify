# File created by: Liam Newberry
from eyed3 import load as e3
# import io
# import os
import pygame as pg

from draw_funcs import *
from event_funcs import *
from folder_funcs import *
from main_settings import *
from player import Player

class Main:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption("Modify")
        self.logo_image = pg.image.load(os.path.join(main_folder,"logo.png")).convert()
        self.logo_image = pg.transform.scale(self.logo_image,(70,70))
        pg.display.set_icon(self.logo_image)
    def new(self):
        self.page = "songs"
        self.page_funcs = {"songs":draw_page_songs(),
                           "artists":draw_page_artists(),
                           "albums":draw_page_albums(),
                           "playlists":draw_page_playlists(),
                           "search":draw_page_search()}
        self.nav_bar_surface, self.nav_dict = nav_bar_update(self.screen,self.page,
                                                             self.page_funcs,self.logo_image)
    def events(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                new_selection = nav_bar_clicks(self.nav_dict,pos)
                if new_selection != None:
                    self.page = new_selection
                    self.nav_bar_surface, self.nav_bar = nav_bar_update(self.screen,self.page,
                                                            self.page_funcs,self.logo_image)
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.should_quit = True
    def update(self):
        self.now = pg.time.get_ticks()
    def draw(self):
        self.screen.fill(PRIMARY_COLOR)
        # x = pg.image.load(get_song_info("sample_id")["image"]).convert()
        # pg.transform.scale(x,(100,100))
        # self.screen.blit(x,x.get_rect())
        draw_divider_horizantal(self.screen,SECONDARY_COLOR,100,5)
        self.screen.blit(self.nav_bar_surface,(0,0))
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
    
def game_loop():
    while True:
        m = Main()
        m.new()
        should_quit = m.run()
        if should_quit:
            break
    pg.quit()
    pg.mixer.quit()
        
game_loop()
rename_folder_contents()
