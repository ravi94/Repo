from distutils.core import setup
import py2exe
import pygame,time,random,math

from pygame.locals import *

ship="sp.png"
ship1="sp1.png"
bg= "bg.png"
db="debris.png"
sh="shot1.png"
ast="asteroid.png"
e="explosion.png"

 
setup(console=['game.py'])
