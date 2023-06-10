import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1600, 800
 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))#Window Size (Tupple passed)
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("images\pxfuel.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 20   # Const of Player size
PLAYER_HEIGHT = 30

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3


FONT = pygame.font.SysFont("Digital-7", 25)


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"{round(elapsed_time)} Sec", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (0, 255, 68), player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)# My character size

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 1000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment: # '_' is a blank placeholder so that I can itterate 3 times. 
            for _ in range(1):
                star_x = random.randint(0, WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) # '-STARHEIGHT' gives a negative y coordanate.
                stars.append(star)

            star_add_increment = max(10,star_add_increment - 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.w <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]: # dynamically copy to edit list
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player): # This handles collision of stars with player
                stars.remove(star)
                hit = True
                break
        

        if hit: 
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)
    
    pygame.quit()

if __name__ == "__main__":
    main()