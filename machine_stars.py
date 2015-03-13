#!/usr/bin/env python3

import sys
import pygame
import random

pygame.init()

# Set up the picture of our little machine:
machine_img = pygame.image.load('machine.png')
machine_rect = machine_img.get_rect()
machine_rect.left = 10
machine_rect.top = 120

# Set up the picture of a star:
original_star_img = pygame.image.load('star.png')

text_color = pygame.Color(255, 255, 255)
bg_color = pygame.Color(0, 0, 0)

screen = pygame.display.set_mode([320, 240])

# This will hold some input lines:
stars_length = 0
offset = 0

# Start building a list of things to display from stdin:
display_lines = [sys.stdin.readline()]

while len(display_lines) > 0:
    screen.blit(machine_img, machine_rect)

    # Black out the areas above and right of the machine image:
    screen.fill(bg_color, [0, 0, 320, 120])
    screen.fill(bg_color, [machine_rect.right, machine_rect.top, 320, 240])

    # Get the next available line from stdin:
    line = sys.stdin.readline()

    if line:
        display_lines.insert(0, line)

    # If there're more than 6 lines to display, or we're not getting
    # any more input, pop the last line off the list and turn it into
    # a number of stars to show:
    if (len(display_lines) > 6) or (not line):
        stars_length = len(display_lines.pop())

    # If there's no more input, start offsetting display from the top
    # of the screen so it seems to fall downwards:
    if not line:
        offset = offset + 20

    # Display the most recent lines of stdin falling into the machine,
    # in a font that gets smaller as it falls:
    font_size = 22
    y = 0 + offset
    for render_me in display_lines:
        font_size = font_size - 2
        font = pygame.font.Font(None, font_size) 
        input_text_surface = font.render(render_me.rstrip(), True, text_color)
        input_text_rect = input_text_surface.get_rect(center = (64, y))
        screen.blit(input_text_surface, input_text_rect)
        y = y + 20

    pygame.display.update()

    # Display stars leaving machine's output:
    if stars_length > 0:
        star_x = machine_rect.right
        for i in range(0, stars_length):
            star_w = random.randrange(10, 28)
            star_h = random.randrange(10, 28)
            star_x = star_x + star_w
            star_img = pygame.transform.smoothscale(original_star_img, (star_w, star_h))
            star_rect = star_img.get_rect()
            pygame.display.update()
            pygame.time.wait(15)
            star_rect.left = star_x
            star_rect.top = 185 + random.randrange(-5, 5)
            screen.blit(star_img, star_rect)

    # Chill out for for 400 milliseconds:
    pygame.time.wait(200)
