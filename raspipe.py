#!/usr/bin/env python3
# encoding: utf-8

import sys
import pygame

class RasPipe:
    size = width, height = 320, 240
    font_size = 30
    delay = 70
    black = (0, 0, 0)
    white = (255,255,255)
    input_buffer_size = 100
    input_lines = []
    display_lines = 7

    def __init__(self, infile):
        self.infile = infile
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.Font(None, self.font_size) 

    def run(self):
        line = self.infile.readline()
        while line:
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                sys.exit()

            self.scale_display()

            self.screen.fill(self.black)

            # Get last 7 lines of input...
            to_render = self.input_lines[-self.display_lines:]

            # ...and scroll them up the display.
            y = 0
            for render_line in to_render:
                y += self.font_size
                text_surface = self.font.render(render_line.rstrip(), True, self.white)
                rect = text_surface.get_rect(center=(160, y))
                self.screen.blit(text_surface, rect)

            pygame.display.flip()

            pygame.time.wait(self.delay);

            self.input_lines.append(line)
            line = self.infile.readline()

    def scale_display(self):
       original_font_size = self.font_size

       # How big should our font be?
       if len(self.input_lines) > 20:
           self.delay = 30
           self.font_size = 20

       if len(self.input_lines) > 50:
           self.delay = 20
           self.font_size = 15

       if len(self.input_lines) > 100:
           self.delay = 5
           self.font_size = 10

       if self.font_size != original_font_size:
           self.font = pygame.font.Font(None, self.font_size) 

       # How many lines of text to display?
       self.display_lines = int(self.size[1] / self.font_size) - 1

rp = RasPipe(sys.stdin)
rp.run()
