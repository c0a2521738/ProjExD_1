import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    # 背景jpg
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    # こうかとんpng
    kk_img = pg.image.load("fig/3.png") 
    kk_img = pg.transform.flip(kk_img,True,False)
    # こうかとんrct
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        #押下キーに応じて移動(こうかとん)
        key_lst = pg.key.get_pressed()
        # ↓ x,y方向の移動量
        x_delta = -1 # ← 初期値-1(キー入力なしで左に流れる)
        y_delta = 0
        if key_lst[pg.K_UP]:
            y_delta -=1
        if key_lst[pg.K_DOWN]:
            y_delta +=1
        if key_lst[pg.K_LEFT]:
            x_delta -= 1
        if key_lst[pg.K_RIGHT]:
            x_delta += 2
        kk_rct.move_ip(x_delta,y_delta)
        
        #背景描画
        x = tmr % 3200                          # 0〜3199
        screen.blit(bg_img,  [-x, 0])           # original1
        screen.blit(bg_img2, [1600 - x, 0])     # flipped1
        screen.blit(bg_img,  [3200 - x, 0])     # original2
        #こうかとん描画
        screen.blit(kk_img,kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()