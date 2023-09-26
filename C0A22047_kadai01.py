import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img1 = pg.image.load("ProjExD2023/ex01/fig/pg_bg.jpg")
    bg_img2 = pg.image.load("ProjExD2023/ex01/fig/3.png")
    flip_image = pg.transform.flip(bg_img2, True, False)

    

    tmr = 0
    a = 0
    b = 1

    while True:
            rotate_image = pg.transform.rotate(flip_image, a)
            image_list = [flip_image, rotate_image]


            for event in pg.event.get():
                if event.type == pg.QUIT: return

            x = tmr % 1600
            screen.blit(bg_img1, [-x, 0])

            screen.blit(bg_img1, [1600 - x, 0])


            screen.blit(image_list[1], [300, 200])
            pg.display.update()
            tmr += 1

            a += b
            if a >= 10:
                 b *= -1

            elif a <= 0:
                 b *= -1

            clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()