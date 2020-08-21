import pygame, random, os, time
from pygame.locals import *

#statheres xrwmatwn,megethwn kai rologiou
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)
WIDTH  = 600
HEIGHT = 400
FPS = 60
# initialize tou font, tou score kai tou gameover
pygame.font.init()
SCORE_FONT = pygame.font.SysFont("Comic Neue", 30)
GAME_OVER_FONT = pygame.font.SysFont("Comic Neue", 40)
# initialize tou paixnidiou
pygame.init()
pygame.mixer.init()
# initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
#titlos
pygame.display.set_caption("Bouncing Babies")
#icon paixnidiou
icon = pygame.image.load('newborn.png')
pygame.display.set_icon(icon)
#hxos tou paixnidiou
ball_to_paddle = pygame.mixer.Sound("ball.wav")
ball_to_walls = pygame.mixer.Sound("ball_walls.wav")
powr_up = pygame.mixer.Sound("power_up.wav")

class Ball(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("baby.png").convert()
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image,(60,60))
        self.rect = self.image.get_rect()
	self.rect.center = (50, 10)
        self.x_speed = random.randrange(-3, 3)
        self.y_speed = 3
        self.rotation = 0
        self.y_direction = "down"
        self.score = 0
        self.total_score = 1
        self.score_text = SCORE_FONT.render("score: "+str(self.score),
         False,(green))
        self.game_over_text = GAME_OVER_FONT.render("Game over", False,(red))
        self.game = "on"


    def update(self):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed
        if self.y_direction == "down" and self.rect.colliderect (player.rect):
            ball_to_paddle.play()
            player.rect.y += 5
            self.y_speed *= -1
            self.y_direction = "up"
        if self.y_direction == "up" and self.rect.top <= 60:
            self.x_speed = self.get_random_move()
            self.y_speed *= -1
            self.y_direction = "down"
        if self.rect.left <= 0:
            self.x_speed *= -1
	if self.rect.right >= WIDTH:
	    self.x_speed = 0
	    self.y_speed = 0
            self.score +=1
            self.total_score +=1
            self.score_text = score_text = SCORE_FONT.render("score: "+str(self.score), True (green))
 	    self.game = "off"
        if self.y_direction == "down"and self.rect.top > HEIGHT:
            self.game = "off"
           
    def get_random_move(self):
        return random.randrange(1,4)
def make_ball():
	ball = Ball()
        ball.image = pygame.image.load("baby.png").convert()
        ball.image.set_colorkey(black)
        ball.image = pygame.transform.scale(self.image,(60,60))
        ball.rect = self.image.get_rect()
	ball.rect.center = (50, 10)
        ball.x_speed = random.randrange(-3, 3)
        ball.y_speed = 3
        ball.rotation = 0
        ball.y_direction = "down"
        ball.score = 0
        ball.total_score = 1
        ball.score_text = SCORE_FONT.render("score: "+str(self.score),
         False,(green))
        ball.game_over_text = GAME_OVER_FONT.render("Game over", False,(red))
        ball.game = "on"
	return ball


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width_size = 100
        self.height_size = 5
        self.image = pygame.image.load("paddle.png").convert()
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image,(self.width_size, self.height_size))
        self.rect = self.image.get_rect()
        self.rect.center =(WIDTH/2, HEIGHT/1 -10)
        self.x_speed = 0
        self.x_stop= 0 
        self.left_speed = -4
        self.right_speed = 4 


    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x_speed = self.left_speed
        if keystate[pygame.K_RIGHT]:
            self.x_speed = self.right_speed
        if keystate[pygame.K_DOWN]:
            self.x_speed = self.x_stop
        self.rect.x += self.x_speed
        if self.rect.left <0 :
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.y == 393:
            self.rect.y = 388



# Objects
all_s = pygame.sprite.Group()
player = Player()
ball = Ball(player)


all_s.add(player)
all_s.add(ball)

def main():
    running = True
    #loop gia treximo paixnidiou
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
	    #an kanoume quit stamata na trexei to paixnidi
            if event.type == pygame.QUIT:
                running = False
            
        all_s.update()

        screen.fill(black)
        screen.blit(ball.score_text,(10,10))
        all_s.draw(screen)
        if ball.game == "off":
            screen.blit(ball.game_over_text,(220,150))
            running = False

        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()

