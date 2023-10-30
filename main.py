from os import environ, pipe
import pygame 
import sys
from pygame import image
import random

from pygame.constants import KEYDOWN


pygame.init()

clock_Speed = pygame.time.Clock()

#Canvas size
wd,ht = 288,532
screen = pygame.display.set_mode((wd,ht))
bg_surface = pygame.image.load('Pictures/background-day.png')

#Floor
floor_surface = pygame.image.load("Pictures/base.png")
floor_X = 0
floor_Y = ht - 100

#bird

bird_down = pygame.image.load("Pictures/bluebird-downflap.png")
bird_midflap = pygame.image.load("Pictures/bluebird-midflap.png")
bird_upflap = pygame.image.load("Pictures/bluebird-upflap.png")

bird_frame = [bird_down, bird_midflap, bird_upflap]
bird_index = 0

BIRDFLAP = pygame.USEREVENT
pygame.time.set_timer(BIRDFLAP,200)

bird_surface = pygame.image.load("Pictures/bluebird-midflap.png")
bird_rect = bird_surface.get_rect(center = (wd/2,ht/2))

gravity = 0.07
bird_movment = 0

def rotate_bird(bird):
    rotated_bird = pygame.transform.rotate(bird,5* bird_movment)
    return rotated_bird

def bird_animation():
    new_bird = bird_frame[bird_index]
    new_rect = new_bird.get_rect(center=(wd / 2 - 40, bird_rect.centery))
    return new_bird,new_rect


#Pipes
pipe_surface = pygame.image.load("Pictures/pipe-green.png")
pipe_list = []
pipe_height = [200,250,300,350]

Spawning_pip = pygame.USEREVENT
pygame.time.set_timer(Spawning_pip,1000)

pygame.display.set_caption('Pictures/flappy bird')    

def floor_animation():
    screen.blit(floor_surface,(floor_X,floor_Y + 50))
    screen.blit(floor_surface,(floor_X + wd,floor_Y + 50))

def create_pipe():
    top_pipe = pipe_surface.get_rect(midtop=(wd * 2, random.choice(pipe_height)))
    bottom_pipe = pipe_surface.get_rect(midbottom=(wd*2, random.choice(pipe_height) - 150))
    return top_pipe,bottom_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx  -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= ht:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe, pipe)

while True:
    screen.blit(bg_surface,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movment = 0
                bird_movment -= 3

    floor_X -= 1
    floor_animation()
    if floor_X < -wd:
        floor_X = 0

    # bird
    if event.type == BIRDFLAP:
        if bird_index<2:
            bird_index += 1
        else:
            bird_index = 0

    bird_surface, bird_rect = bird_animation()

    bird_movment += gravity
    bird_rect.centery += bird_movment
    rotated_bird = rotate_bird(bird_surface)
    screen.blit(rotated_bird,bird_rect)

    if event.type == Spawning_pip:
        pipe_list.extend(create_pipe())
        #print(pipe_list)

    pipe_list = move_pipe(pipe_list)
    draw_pipes(pipe_list)

    pygame.display.update()
    floor_animation()

    clock_Speed.tick(100)

pygame.Rect(wt,ht,locationx,loctiony)