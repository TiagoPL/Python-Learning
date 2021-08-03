import pygame

pygame.init()
pygame.mixer.music.load('your_music_file.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy:
    pass
