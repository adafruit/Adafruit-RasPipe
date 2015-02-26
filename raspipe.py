#!/usr/bin/env python
# encoding: utf-8

import sys
import pygame
import re

pygame.init()

size = width, height = 320, 240

black = (0, 0, 0)
white = (255,255,255)
font_big = pygame.font.Font(None, 40) 

screen = pygame.display.set_mode(size)

line = sys.stdin.readline()
while line:
    stars = re.sub('\S', '★', line)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    screen.fill(black)

    text_surface = font_big.render(line, True, white)
    rect = text_surface.get_rect(center=(160,120))
    screen.blit(text_surface, rect)

#   a = 100
#   if pygame.key.get_focused():
#     press = pygame.key.get_pressed()
#     for i in xrange(0,len(press)):
#       if press[i] == 1:
#         name = pygame.key.name(i)
#         text = font_big.render(name, True, white)
#         screen.blit(text, (100, a))
#         a=a+100
#         if name == "q":
#           sys.exit()

    pygame.display.flip()

    line = sys.stdin.readline()
