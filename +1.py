"""
This is your basic template, use this ;)

"""

import random 

import os, sys
import pygame
from pygame.locals import *
import math

from spritesheet_functions import SpriteSheet
pygame.init()

#Font,size,bold,italics
font = pygame.font.SysFont('Calibri',25,True,False)


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error.message:
      return sound


import time

# Define some colors, add more if you want to

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
gray = (100, 100, 100)

EXPLOSION_1 = (41,0,41,46)
EXPLOCION_2 = (82,0,41,46)
EXPLOSION_3 = (123,0,41,46)
EXPLOSION_4 = (164,0,41,46)
EXPLOSION_5 = (205,0,41,46)
EXPLOSION_6 = (246,0,41,46)

#Screen Dimentions
screen_width = 900
screen_height = 600

#I think you'll want to add the drawing parts here, so you can call them
#later, remember, it's with "def"

score=0

minuscount= score+1

"""
def main():
    ""Main program is here. ""
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
 
    # Get the score from the current game
    score = 0
    try:
        # Ask the user for his/her score
        score = int(input("What is your score? "))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")
 
    # See if we have a new high score
    if score > high_score:
        print("Yea! New high score!")
 
        # We do! Save to disk
        try:
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(current_score))
            high_score_file.close()
        except IOError:
            # Hm, can't write it.
            print("Too bad I couldn't save it.")
    else:
        print("Better luck next time.")
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()


"""
      

#Put here all the class stuff, it's the most important
                
class MinusEgg(pygame.sprite.Sprite):
    
    def reset_pos(self):
        self.rect.y = random.randrange(-1000,-50)
        self.rect.x = random.randrange(-10,screen_width+10)
    
    def update(self):
        #move the drop
        self.rect.y +=1
        if self.rect.y > screen_height +100 :
            self.rect.y = random.randrange(-1050, -170)
            self.rect.x = random.randrange(0, screen_width)
        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Load the image

        self.image = pygame.image.load("MinusSprite.png")

        self.rect = self.image.get_rect()

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Load umb
        self.image = pygame.image.load("Laser.png")
        self.rect = self.image.get_rect()

    def update(self):

        #move da bullet
        self.rect.y -= 10
        

class Manta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Load umb
        self.image = pygame.image.load("Plusprite.png")
        self.rect = self.image.get_rect()
    def update(self) :

        self.rect.x = x_coord
        self.rect.y = y_coord

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)

        #Load umb
        self.image = pygame.image.load("Bullet.png")
        self.rect = self.image.get_rect()
        self.max= 3
        self.dx = random.uniform(-self.max,self.max)
        self.dy = random.uniform(-self.max,self.max)
      
        
    def update(self) :

        self.rect.x += self.dx 
        self.rect.y += self.dy
          
        
class Hitbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load("Hitbox.png")
        self.rect = self.image.get_rect()

    def update(self) :
        self.rect.x = x_coord+64
        self.rect.y = y_coord+50

        if self.rect.x != x_coord+64:
            self.rect.x = x_coord+64

class Explosion(pygame.sprite.Sprite):
    explosion_frames = []
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Explosion.png")
        image = sprite_sheet.get_image(41,0,41,46)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(82,0,41,46)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(123,0,41,46)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(164,0,41,46)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(205,0,41,46)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(246,0,41,46)
        self.explosion_frames.append(image)

        self.image = self.explosion_frames[0]
        self.rect = self.image.get_rect()

    def update(self):
        self.image=self.explosion_frames[0]

        
pygame.init()



#Position of graphics

back_position = [0, 0]
concrete_position = [-50, 550]

#Put here all the awesome graphics, F**k Yeah!

title_screen = pygame.image.load("Titlescreen.png")
back_image = pygame.image.load("Sea.png")
laser_image = pygame.image.load("Laser.png")
MinEgg_image = pygame.image.load("MinusSprite.png")
MinBull_image = pygame.image.load("Bullet.png")
Manta_image = pygame.image.load("Plusprite.png")

#Put here all the musci, because no game is game without it :3
pygame.mixer.music.load('Riko.ogg')
pygame.mixer.music.play()        

# Set the width and height of the screen [width, height]
mistmove = 100
screendrop = 1500
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("+1")

#Put here lists of "sprites". Each block in the program is
#added to this list
#The list is managed by a class called "Group."

minusegg_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
manta_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
explosion_list = pygame.sprite.Group()

#This is a list of every sprite.
# All sprites :)
all_sprites_list = pygame.sprite.Group()


for i in range (7):
        #MinusEgg
        minusegg = MinusEgg()
        #Random location
        minusegg.rect.x = random.randrange(screen_width)
        minusegg.rect.y = random.randrange(screendrop)

        #adding to list
        minusegg_list.add(minusegg)
        all_sprites_list.add(minusegg)
    




#Manta control
manta = Manta()
hitbox = Hitbox()
bullet= Bullet()
explosion = Explosion()
all_sprites_list.add(manta)
all_sprites_list.add(hitbox)

laser_sound = pygame.mixer.Sound("ATTACK3.wav")
manta_sound = pygame.mixer.Sound("TWINKLE3.wav")
ded_sound = pygame.mixer.Sound("DED.wav")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

# Speed in pixels per frame
x_speed = 0
y_speed = 0
  
# Current position
x_coord = 400
y_coord = 400

# -------- Main Program Loop -----------


while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            
    # --- Game logic should go here

                  
             
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed =- 5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed =- 5
            elif event.key == pygame.K_DOWN:
                y_speed = 5

            elif event.key == pygame.K_x:
                laser = Laser()
                laser.rect.x = manta.rect.x+64
                laser.rect.y = manta.rect.y+5

                all_sprites_list.add(laser)
                laser_list.add(laser)
                manta_sound.play()
            
    # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed=0
            elif event.key == pygame.K_RIGHT:
                x_speed=0
            elif event.key == pygame.K_UP:
                y_speed=0
            elif event.key == pygame.K_DOWN:
                y_speed=0
            
        
    if x_coord > 820:
                x_coord = 819
    if x_coord < -60:
                x_coord = -59
    if y_coord < -20:
                y_coord = -19
    if y_coord > 530:
                y_coord = 529
                
    #minusegg_hit_list = pygame.sprite.spritecollide(Laser,minusegg_list,False)



   
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    all_sprites_list.update()



    for laser in laser_list:

            
        minusegg_hit_list = pygame.sprite.spritecollide(laser, minusegg_list, False)

        for minusegg in minusegg_hit_list:
            
            laser_list.remove(laser)
            all_sprites_list.remove(laser)
            score += 1
            print (score)
            laser_sound.play()
            explosion=Explosion()
            explosion.rect.x = minusegg.rect.x+2
            explosion.rect.y = minusegg.rect.y+2
            explosion_list.add(explosion)
            for i in range(score):
                bullet= Bullet()
                bullet.rect.x = minusegg.rect.x+5
                bullet.rect.y = minusegg.rect.y+5
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            minusegg.reset_pos()

            
        if laser.rect.y < -15:
            laser_list.remove(laser)
            all_sprites_list.remove(laser)
            
        if bullet.rect.y < -15:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        if bullet.rect.y > 545:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        if bullet.rect.x < -15:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        if bullet.rect.x > 810:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    if pygame.sprite.spritecollide(hitbox, minusegg_list, True):
        ded_sound.play
        
        done=True
        
    if pygame.sprite.spritecollide(hitbox, bullet_list, True):
        ded_sound.play
        
        done=True         
        

    all_sprites_list.update()
        
        
    # --- Drawing code should go here


    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.blit(back_image, back_position)

    text = font.render("Score: " + str(score), True, WHITE)

    screen.blit(text, [10, 10])
    
    minusegg_list.update()
    
    all_sprites_list.draw(screen)
    #screen.blit(cloud,[-80,-200])


        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.



    
pygame.quit()
