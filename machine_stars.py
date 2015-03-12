#!/usr/bin/env python3

import sys
import pygame

pygame.init()

# Set up the picture of our little machine:
machine_img = pygame.image.load('machine.png')
machine_rect = machine_img.get_rect()
machine_rect.left = 10
machine_rect.top = 120

# Set up the picture of our little machine:
star_img = pygame.image.load('star.png')
star_img = pygame.transform.smoothscale(star_img, (10, 10))
star_rect = star_img.get_rect()

font = pygame.font.Font(None, 20) 
text_color = pygame.Color(255, 255, 255)
bg_color = pygame.Color(0, 0, 0)

screen = pygame.display.set_mode([320, 240])

# This will hold some input lines:
stars_length = 0
offset = 0

display_lines = [sys.stdin.readline()]
while len(display_lines) > 0:
    screen.blit(machine_img, machine_rect)

    # Black out the areas above and right of the machine image:
    screen.fill(bg_color, [0, 0, 320, 120])
    screen.fill(bg_color, [machine_rect.right, machine_rect.top, 320, 240])

    line = sys.stdin.readline()
    if line:
        display_lines.insert(0, line)
    if (len(display_lines) > 6) or (not line):
        stars_length = len(display_lines.pop())
    if not line:
        offset = offset + 20

    # Display the input falling into the machine's input:
    y = 0 + offset
    for render_line in display_lines:
        input_text_surface = font.render(render_line.rstrip(), True, text_color)
        input_text_rect = input_text_surface.get_rect(left = 24, top = y)
        screen.blit(input_text_surface, input_text_rect)
        y = y + 20

    if stars_length > 0:
        for star_i in range(0, stars_length):
            star_rect.left = machine_rect.right + 8 + (star_i * star_rect.width)
            star_rect.top = 190
            screen.blit(star_img, star_rect)

    pygame.display.update()

    pygame.time.wait(400);
