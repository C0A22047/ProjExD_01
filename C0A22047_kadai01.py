import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img1 = pg.image.load("ProjExD2023/ex01/fig/pg_bg.jpg")
    bg_img2 = pg.image.load("ProjExD2023/ex01/fig/3.png")
    flip_image = pg.transform.flip(bg_img2, True, False)
    rotate_image = pg.transform.rotate(flip_image, 10)
    image_list = [flip_image, rotate_image]