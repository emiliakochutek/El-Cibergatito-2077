import pygame
pygame.font.init()

INFINITIVES_FILE_PATH = 'game_data/indefinido.txt'
with open(INFINITIVES_FILE_PATH) as file:
    INFINITIVES = [word for line in file for word in line.split()]

INFINITIVES_IRREGULAR_FILE_PATH = 'game_data/irregulars_indefinido.txt'
with open(INFINITIVES_IRREGULAR_FILE_PATH) as file:
    INFINITIVES_IRREGULAR = [line.split()[0] for line in file]

WIDTH, HEIGHT = 800, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

## background
NIGHT_SURF = pygame.image.load('images/nightbuildings.jpg').convert()
GROUND_SURF = pygame.image.load('images/ground.png').convert()
PAPER_BG_SURF = pygame.image.load('images/paper_bg.jpg').convert()

## fonts
SCORE_FONT = pygame.font.Font('font/FutureTech.ttf', 40)
FONT_ON_PAPER = pygame.font.Font('font/Futuristic_Armour.ttf', 30)
MESSAGE_FONT = pygame.font.Font('font/Futuristic_Armour.ttf', 20)

## start screen
CAT_STAND = pygame.image.load('images/cat_standing.png').convert_alpha()
CAT_STAND = pygame.transform.rotozoom(CAT_STAND, 0, 2)
CAT_RECT = CAT_STAND.get_rect(midbottom = (WIDTH/2, HEIGHT/2 + 25))
NAME_SURF = SCORE_FONT.render('El cibergatito 2077', True, 'Black')
NAME_RECT = NAME_SURF.get_rect(center = (WIDTH/2, HEIGHT/2 + 75))
MESSAGE_SURF1 = MESSAGE_FONT.render('Help el Cibergatito learn Indicativo!', True, 'Black')
MESSAGE_SURF2 = MESSAGE_FONT.render('Press space to start', True, 'Black')
MESSAGE_SURF3 = MESSAGE_FONT.render('You lost! Press space to try again', True, 'Black')
MESSAGE_RECT1 = MESSAGE_SURF1.get_rect(center = (WIDTH/2, 310))
MESSAGE_RECT2 = MESSAGE_SURF2.get_rect(center = (WIDTH/2, 330))
MESSAGE_RECT3 = MESSAGE_SURF3.get_rect(center = (WIDTH/2, 310))

## spanish word-endings
GROUP_AR = {
    'singular 1st': 'e',
    'singular 2nd': 'aste',
    'singular 3rd': 'o',
    'plural 1st': 'amos',
    'plural 2nd': 'asteis',
    'plural 3rd': 'aron'
    }

GROUP_ER_IR = {
    'singular 1st': 'i',
    'singular 2nd': 'iste',
    'singular 3rd': 'io',
    'plural 1st': 'imos',
    'plural 2nd': 'isteis',
    'plural 3rd': 'ieron'
    }

PERSONS = {
    'singular 1st': 1,
    'singular 2nd': 2,
    'singular 3rd': 3,
    'plural 1st': 4,
    'plural 2nd': 5,
    'plural 3rd': 6
    }