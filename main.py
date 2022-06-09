import turtle
import getpass
import pygame
from pygame.locals import *
from pygame import mixer


USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    #file path to sciezka do pliku na kompie
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)



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

