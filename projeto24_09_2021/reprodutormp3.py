#Author: Gabriel Silva
#Date: 24/09/2021

#Programa que reproduza um de arquivo mp3

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('alok_ringtone.mp3')
pygame.mixer_music.play()
pygame.event.wait()