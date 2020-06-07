# Façca um programa que leia e execute um arquivo mp3.
from pygame import mixer
mixer.init()
mixer.music.load('naruts.mp3')
mixer.music.play()
input('Sadness')