import pygame,sys
import pygame.camera
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode([160,128])

cam = pygame.camera.Camera("/dev/video0", (160,128))
cam.start()

while 1:
image = cam.get_image()
screen.blit(image,(0,0))
pygame.display.update()

for event in pygame.event.get():
if event.type == pygame.QUIT:
sys.exit()