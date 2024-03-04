import pygame
import sys

# Initialisieren von Pygame
pygame.init()

# Laden und Abspielen der Musik
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play(-1)  # Der Parameter -1 l�sst die Musik in einer Endlosschleife laufen
# Setzen der Lautst�rke
pygame.mixer.music.set_volume(0.2)  # Setzt die Lautst�rke auf die H�lfte
# Setzen der Fenstergr��e
win_size = (320, 320)
win = pygame.display.set_mode(win_size)
# Setzen des Fenstertitels
pygame.display.set_caption('Bitte warte, es wird verarbeitet.....')

# Setzen der FPS (Frames per Second)
clock = pygame.time.Clock()
FPS = 60

# Laden des Auto-Bildes
auto = pygame.image.load('auto.png')
auto_rect = auto.get_rect()

# Laden des Hintergrundbildes
bg = pygame.image.load('background.jpg')
bg_rect = bg.get_rect()

# Definieren der Position des Autos und des Hintergrunds
x = 250
y = 150
bg_x1 = 0
bg_x2 = bg_rect.width
vel = 5

# Hauptspiel-Schleife
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Das Auto f�hrt automatisch nach links
    x -= vel

    # Der Hintergrund bewegt sich nach rechts
    bg_x1 += vel
    bg_x2 += vel

    # Wenn das Auto den linken Rand des Fensters erreicht, l�sst es es auf der rechten Seite erscheinen
    if x < 0 - auto_rect.width:  # linker Rand
        x = win_size[0]

    # Wenn das Hintergrundbild den rechten Rand des Fensters erreicht, l�sst es es auf der linken Seite erscheinen
    if bg_x1 > win_size[0]:  # rechter Rand
        bg_x1 = 0 - bg_rect.width
    if bg_x2 > win_size[0]:  # rechter Rand
        bg_x2 = 0 - bg_rect.width

    win.blit(bg, (bg_x1, 0))  # Zeichnet den ersten Hintergrund
    win.blit(bg, (bg_x2, 0))  # Zeichnet den zweiten Hintergrund
    win.blit(auto, (x, y))  # Zeichnet das Auto
    pygame.display.update()  # Aktualisiert das Display

pygame.quit()
