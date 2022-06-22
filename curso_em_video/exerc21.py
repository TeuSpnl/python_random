import pygame as pg

pg.init()

pg.mixer.music.load('hot_air_balloon.mp3')
pg.mixer.music.play()

pg.event.wait()