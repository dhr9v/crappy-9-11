import pygame
import time
import random
pygame.font.init()

scroll_speed = 1

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy 9/11")

PLAYER = pygame.transform.scale(pygame.image.load("the_plane.png"), (80, 100))
X_POSITION, Y_POSITION = 300, 250

BACKGROUND = pygame.transform.scale(pygame.image.load("bg.jpg"), (1000, 800))

# PIPE IMAGES
top_pipe_image = pygame.image.load("top_pipe_image.png")
bottom_pipe_image = pygame.image.load("bottom_pipe_image.png")
FONT = pygame.font.SysFont("martian mono", (40))

CLOCK = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0

colour = "light blue"

PLAYER_VEL = 5

class Pipe(pygame.sprite.Sprite):
   def __init__(self, x, y, image):
       self.image = image
       self.rect = self.image.get_rect()
       self.rect.x, self.rect.y = x, y
   
   def update(self):
       self.rect.x -= scroll_speed
       if self.rect.x <= -WIDTH:
           self.kill()
           
def draw(player, elapsed_time, BACKGROUND):
    WIN.blit(BACKGROUND, (0,0))
    time_text = FONT.render(f"SCORE: {round(elapsed_time)}", 1, "black")
    WIN.blit(time_text, (10, 10))
    
    WIN.blit(PLAYER, player)

    pygame.display.update()

       
def main():
    run = True

    # PIPES -
    pipe_timer = 0
    pipes = pygame.sprite.Group()
        
    
    player = PLAYER.get_rect(center=(X_POSITION, Y_POSITION))

    while run:
        CLOCK.tick(60)
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_s] and player.y + PLAYER_VEL <= 800:
            player.y += PLAYER_VEL

        # draw and update pipes
        
        pipes.draw(WIN)
        pipes.update()   

        # spawn pipes
        if pipe_timer <= 0:
            x_top, x_bottom = 800, 800
            y_top = random.randint(-600, -400)
            y_bottom = y_top + random.randint(90, 130) + bottom_pipe_image.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_image))
            pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1    
          

        draw(player, elapsed_time, BACKGROUND)
        

        
    
    pygame.quit()

if __name__ == "__main__":
    main()