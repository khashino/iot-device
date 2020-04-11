import pygame, sys, os
from datetime import datetime
import math
from pygame.locals import *
import time
import socket
from subprocess import check_output

os.environ["SDL_FBDEV"] = "/dev/fb1"

REMOTE_SERVER = "www.google.com"

cmd = ["""hostname -I"""]
###########################################
def wifistatus():
	wifi_ip = check_output(cmd,shell=True)
	if len(wifi_ip) <= 2:
		return False
	else:
		return True

def getmyip():
	return check_output(cmd,shell=True)


def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

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
BLACK = (0, 0, 0)
WHITE  = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 200, 200)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((160, 128), 0, 32)
#screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Clock')
hour_font = pygame.font.SysFont('Calibri', 25, True, False)
#digital_font = pygame.font.SysFont('advanced_dot_digital-7', 25, False, False)
#digital_font = pygame.font.SysFont('3X5-6OYA', 70, False, False)
digital_font = pygame.font.SysFont('QUEER___', 60, False, False)
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

digital_font2 = pygame.font.SysFont('QUEER___', 37, False, False)
digital_font3 = pygame.font.SysFont('Calibri', 15, True, False)


clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    now = datetime.now()



    network = is_connected(REMOTE_SERVER)
    wifi = wifistatus()

    if network:
    	screen.blit(get_image('/home/pi/Project/main/net-g.png'), (5, 5))
    else:
    	screen.blit(get_image('/home/pi/Project/main/net-r.png'), (5, 5))

    if wifi:
    	screen.blit(get_image('/home/pi/Project/main/wifi-g.png'), (25, 5))
    else:
    	screen.blit(get_image('/home/pi/Project/main/wifi-r.png'), (25, 5))

    myipadd = getmyip()
    myipadd = myipadd[:-1]
    myip = digital_font3.render(myipadd, False, BLUE)

    # draw digital clock
    #digital_text = now.strftime('%H:%M:%S')
    digital_text = now.strftime('%H:%M')
    #digital_text2 =  now.strftime('%S')
    text = digital_font.render(digital_text, True, WHITE)
    #text2 = digital_font2.render(digital_text2, True, WHITE)
    screen.blit(
        text,
        [
            0  ,
            digital_font.size(digital_text)[1] / 2 - 2
        ]
    )
    screen.blit(myip,[0,110])

    #screen.blit(
    #    text2,
    #    [
    #        110  ,
    #        digital_font.size(digital_text2)[1] + 20
    #    ]
    #)


    pygame.display.flip()
    clock.tick(60)
    time.sleep(30)

pygame.quit()
