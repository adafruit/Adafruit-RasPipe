#!/usr/bin/env python

import getopt
import sys
import time

import pygame

class RasPipe:
    size = width, height = 320, 240

    delay = 70 # ms
    display_lines = 7
    font_size = 26
    input_lines = []
    tick = 0
    stars = False

    def __init__(self, infile):
        """Create a RasPipe object for a given input file."""
        self.infile = infile

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.setfont(self.font_size)

        self.fgcolor = pygame.Color(0, 0, 0)
        self.bgcolor = pygame.Color(255, 255, 255)

        # A little bit of sound.
        pygame.mixer.init()
        self.click = pygame.mixer.Sound('./tick.wav')

        # Set up the picture of a star:
        self.orig_star_img = pygame.image.load('star.png').convert_alpha()

    def setfont(self, size):
        """Set a display font of a given size."""
        self.font = pygame.font.Font(None, self.font_size) 

    def toggle_stars(self):
        self.stars = not self.stars

    def run(self):
        """Process standard input."""
        line = self.infile.readline()
        while line:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.toggle_stars()                 

            self.tick += 1
            self.scale_display()
            self.screen.fill(self.bgcolor)

            # Get last display_lines of input and scroll them up display:
            to_render = self.input_lines[-self.display_lines:]
            y = 0
            for render_line in to_render:
                render_line = render_line.rstrip()

                if self.stars:
                    star_w = star_h = len(render_line)
                    star_img = pygame.transform.smoothscale(self.orig_star_img, (star_w, star_h))
                    r = star_img.get_rect(center=(self.width / 2, y))
                    self.screen.blit(star_img, r)
                    y += star_h
                    if y > self.height:
                        break

                else:
                    text_surface = self.font.render(render_line, True, self.fgcolor)
                    r = text_surface.get_rect(left=2, top=y)
                    self.screen.blit(text_surface, r)
                    for pixel_x in range(0, len(render_line)):
                        if render_line[pixel_x] != ' ':
                            pygame.draw.line(self.screen, self.fgcolor, [pixel_x, r.bottom], [pixel_x, r.bottom], 1)
                    y += self.font_size

            if self.tick % self.display_lines == 0:
                self.click.play()
            
            # Actually display the display:
            pygame.display.flip()

            pygame.time.wait(self.delay);

            self.input_lines.append(line)
            line = self.infile.readline()

    def scale_display(self):
       """Set the current font size and delay based on amount of input."""
       original_font_size = self.font_size

       # How big should our font be, and how fast should text scroll?
       if len(self.input_lines) > 150:
           self.input_lines.pop(0)
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
       self.display_lines = int(self.size[1] / self.font_size)

# Handle running this file as a standalone script.
if __name__ == '__main__':
    rp = RasPipe(sys.stdin)

    opts, args = getopt.getopt(sys.argv[1:], 'sx:y:')
    for opt, arg in opts:
        if opt == '-x':
            rp.size[0] = (int(arg))
        if opt == '-y':
            rp.size[1] = (int(arg))
        if opt == '-s':
            rp.toggle_stars()

    rp.run()
