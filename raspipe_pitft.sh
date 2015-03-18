#!/usr/bin/env bash

# A wrapper for displaying raspipe.py output on /dev/fb1

export SDL_FBDEV=/dev/fb1
cat /dev/stdin | ./raspipe.py $@
