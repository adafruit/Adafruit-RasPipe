#!/usr/bin/env bash
export SDL_FBDEV=/dev/fb1
./listener.js | ./raspipe.py
