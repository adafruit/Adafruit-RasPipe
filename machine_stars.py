#!/usr/bin/env python

import sys
import random

import pygame

text_color = pygame.Color(0, 0, 0)
bg_color = pygame.Color(255, 255, 255)

pygame.init()
screen = pygame.display.set_mode([320, 240])
screen.fill(bg_color)

# Set up the picture of our little machine:
machine_img = pygame.image.load('machine.png').convert_alpha()
machine_img = pygame.transform.smoothscale(machine_img, (100, 112))
machine_rect = machine_img.get_rect()
machine_rect.left = 10
machine_rect.top = 120
screen.blit(machine_img, machine_rect)

# Set up the picture of a star:
orig_star_img = pygame.image.load('star.png').convert_alpha()

# This will hold some input lines:
stars_length = 0
offset = 0

# Start building a list of things to display from stdin:
display_lines = [sys.stdin.readline()]

while len(display_lines) > 0:

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

    # Blank the areas above and right of the machine image:
    screen.fill(bg_color, [0, 0, 320, 120])
    screen.fill(bg_color, [machine_rect.right, machine_rect.top, 320, 240])

    # Display the most recent lines of stdin falling into the machine,
    # in a font that gets smaller as it falls:
    font_size = 22
    y = 0 + offset
    for render_me in display_lines:
        font_size = font_size - 2
        font = pygame.font.Font(None, font_size) 
        input_text_surface = font.render(render_me.rstrip(), True, text_color)
        input_text_rect = input_text_surface.get_rect(center=(64, y))
        screen.blit(input_text_surface, input_text_rect)
        y += 20

    pygame.display.update()

    # Display stars leaving machine's output.  Stars are scaled to a random
    # height & width between 8 and 30 pixels, then displayed at a random
    # vertical location on the screen +/- 8 pixels from 185:
    if stars_length > 0:
        star_x = machine_rect.right
        for i in range(0, stars_length):
            star_w = random.randrange(8, 30)
            star_h = random.randrange(8, 30)
            star_img = pygame.transform.smoothscale(orig_star_img, (star_w, star_h))

            star_rect = star_img.get_rect()
            star_rect.left = star_x
            star_rect.top = 185 + random.randrange(-8, 8)
            screen.blit(star_img, star_rect)

            pygame.display.update()

            # Chill out for 15 milliseconds:
            pygame.time.wait(15)

            # Move start of next star to end of the current one, and quit
            # drawing stars if we've run off the edge of the screen:
            star_x += star_w
            if star_x > 320:
                break

    pygame.time.wait(100)
