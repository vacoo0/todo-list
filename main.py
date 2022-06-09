import turtle
import pygame
from pygame.locals import *
from pygame import mixer
screen = turtle.Screen()
screen.title("OOP")
image = "test.gif"
screen.addshape(image)
turtle.shape(image)


#muzyczka
mixer.init()
mixer.music.load('Music File/bensound-summer_wav_music.wav')
mixer.music.play()

screen.exitonclick()

#rozzijamy wariataa
print("halo wojtyla")

screen.exitonclick()

#florian to jets zią i rybak
#zmiana

