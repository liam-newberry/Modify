# File created by: Liam Newberry
import pygame as pg

from draw_funcs import *
from main_settings import *


def nav_bar_clicks(nav_dict:dict,pos:tuple):
    for item in nav_dict:
        rect = nav_dict[item]
        if (rect[0] <= pos[0] and rect[0] + rect[2] >= pos[0]
            and rect[1] <= pos[1] and rect[1] + rect[3] >= pos[1]):
            return item
    return None

def nav_bar_update(surface,page,page_funcs,logo_image):
    surface.fill(PRIMARY_COLOR)
    draw_divider_horizantal(surface,SECONDARY_COLOR,100,5)
    nav_bar, nav_dict = draw_nav_bar(surface,page_funcs,20,100,page)
    draw_divider_vertical(surface,SECONDARY_COLOR,nav_bar+20,100,5)
    draw_logo_text(surface,logo_image,100)
    return surface.subsurface((0,0,259.5,HEIGHT)).copy(), nav_dict