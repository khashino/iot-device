import pygame, sys, os
from datetime import datetime
import math
from pygame.locals import *
import time
import socket
from subprocess import check_output
import ConfigParser
import io
import random



BLACK = (0, 0, 0)
WHITE  = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 200, 200)
GREEN = (0, 255, 0)
PINK = (255, 0, 255)
YELLOW = (255, 254, 0)
LBLUE = (0, 255, 255)

CLCOLORS = [WHITE,RED,BLUE,GREEN,YELLOW,PINK,LBLUE]
#BGCOLORS = [BLACK,BROWN,DGREEN]
BACKGROUND = BLACK


with open("/project/config.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

status_file = config.get('status', 'statusfile')
uisleep = int(config.get('ui', 'uisleep'))

os.environ["SDL_FBDEV"] = "/dev/fb1"

def status():
    f = open(status_file, "r")
    temp = f.read()
    f.close()
    return(temp)


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
##########################################


##########################################
def initialize():
    pygame.init()
    screen = pygame.display.set_mode((160, 128), 0, 32)
    pygame.display.set_caption('Clock')
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    return screen

def alarm(msg,bgc,clr):
    #while not done:
    screen = initialize()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bgc)
    digital_font = pygame.font.SysFont('Calibri', 40, False, False)
    msgs = digital_font.render(msg, True, clr)
    msg_rect = msgs.get_rect(center=(160/2, 128/2))
    screen.blit(msgs, msg_rect)
    pygame.display.flip()
    #time.sleep(uisleep)

def clockmain():
    screen = initialize()
    hour_font = pygame.font.SysFont('Calibri', 25, True, False)
    digital_font = pygame.font.SysFont('QUEER___', 60, False, False)
    digital_font2 = pygame.font.SysFont('QUEER___', 37, False, False)
    digital_font3 = pygame.font.SysFont('Calibri', 15, True, False)

    ##while not done:
    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        done = True

    now = datetime.now()

    #if int(now.strftime('%S'))%15 == 0:
    #    CLOCKCL = random.choice(CLCOLORS)
    #    #BACKGROUND = BACKGROUND
    clock = pygame.time.Clock()
    screen.fill(BACKGROUND)
    wifi_ip="on"
    network=" "
    try:
        stat = str(status()).split(",")
        wifi_ip = str(stat[1])[:-1]
        network = stat[0]
    except Exception as e:
        print(e)
        #raise

    #myip = digital_font3.render(wifi_ip, False, BLUE)

    if network == 'on':
    	screen.blit(get_image('/project/img/int-b.png'), (5, 5))
    else:
    	screen.blit(get_image('/project/img/int-r.png'), (5, 5))

    if not wifi_ip:
    	screen.blit(get_image('/project/img/wifi-r.png'), (28, 5))
    else:
    	screen.blit(get_image('/project/img/wifi-b.png'), (28, 5))


    digital_text = now.strftime('%H:%M')
    secound = now.strftime('%S')
    text = digital_font.render(digital_text, True, WHITE)
    text2 = digital_font2.render(secound, True, WHITE)
    text_rect = text.get_rect(center=(160/2, 128/2))
    text_rect2 = text.get_rect(center=(160+20, 128-5))
    screen.blit(text, text_rect)
    screen.blit(text2, text_rect2)

    #screen.blit(myip,[0,110])

    pygame.display.flip()
    #clock.tick(60)
    #time.sleep(uisleep)

    #pygame.quit()
