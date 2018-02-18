#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.mixer
import time

pygame.mixer.init()
pygame.mixer.music.load('XXX.mp3')
pygame.mixer.music.play(1) # loop count
time.sleep(5)
pygame.mixer.music.stop()
