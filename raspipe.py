#!/usr/bin/env python3
# encoding: utf-8

import math
import os
import pygame
import random
import re
import sys
import getopt

class RasPipe:
    size = width, height = 320, 240
    # size = width, height = 480, 320

    font_size = 48
    delay = 70
    input_buffer_size = 100
    input_lines = []
    display_lines = 7

    def __init__(self, infile):
        self.infile = infile
        pygame.init()
        exit
        self.screen = pygame.display.set_mode(self.size)
        self.setfont(self.font_size)

        self.bgcolor = pygame.Color(0, 0, 0)
        self.fgcolor = pygame.Color(255, 255, 255)

        # A little bit of sound.
        pygame.mixer.init()
        self.click = pygame.mixer.Sound('./tick.wav')

    def setfont(self, size):
        self.font = pygame.font.Font(None, self.font_size) 

    def run(self):
        tick = 0

        self.click.play()

        line = self.infile.readline()
        while line:
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                sys.exit()

            tick = tick + 1

            self.scale_display()

            self.screen.fill(self.bgcolor)

            # Get last display_lines of input...
            to_render = self.input_lines[-self.display_lines:]

            # ...and scroll them up the display:
            y = 0
            for render_line in to_render:
                y += self.font_size
                text_surface = self.font.render(render_line.rstrip(), True, self.fgcolor)
                # TODO: allow centering text
                # rect = text_surface.get_rect(center=((self.width / 2), y))
                rect = text_surface.get_rect(left=2, top=y)
                self.screen.blit(text_surface, rect)
            
            # A progress bar of sorts
            progress = (self.width / 100) * (len(self.input_lines) / 10)
            self.screen.fill(self.fgcolor, [0, 0, progress, self.font_size])

            if tick % self.display_lines == 0:
                self.click.play()
                # self.bgcolor.r = random.randrange(0, 255)
                # self.bgcolor.g = random.randrange(0, 255)
                # self.bgcolor.b = random.randrange(0, 255)
                # self.bgcolor.a = random.randrange(0, 255)
            
            # Acutally display the display:
            pygame.display.flip()

            pygame.time.wait(self.delay);

            self.input_lines.append(line)
            line = self.infile.readline()

    def scale_display(self):
       """Set the current font size and delay based on amount of input"""
       original_font_size = self.font_size

       # How big should our font be, and how fast should text scroll?
       if len(self.input_lines) > 150:
           self.font_size = 18
           self.delay = 5
       elif len(self.input_lines) > 60:
           self.font_size = 20
           self.delay = 10
       elif len(self.input_lines) > 30:
           self.font_size = 24
           self.delay = 20

       if self.font_size != original_font_size:
           self.setfont(self.font_size)
   
       # How many lines of text to display?
       self.display_lines = int(self.size[1] / self.font_size) - 1

if __name__ == '__main__':
    rp = RasPipe(sys.stdin)

    opts, args = getopt.getopt(sys.argv[1:], 'f:')
    for opt, arg in opts:
        if opt == '-f':
            rp.setfont(int(arg))

    rp.run()
