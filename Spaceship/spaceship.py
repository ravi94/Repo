ship="sp.png"
ship1="sp1.png"
bg= "bg.png"
db="debris.png"
sh="shot.png"
ast="asteroid.png"

import pygame,sys,math
from pygame.locals import *

import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.flushInput()


pygame.init()
screen=pygame.display.set_mode((800,600),0,32)
background=pygame.image.load(bg).convert()
shot=pygame.image.load(sh).convert_alpha()  
debris=pygame.image.load(db).convert_alpha()
astr=pygame.image.load(ast).convert_alpha()

clock=pygame.time.Clock()
s=20
d=0 ; a=0
x=0 ;speed=[0,0] ; angle = 0 ; omega =0
pos_ship=[400,300]
#[p,q]=[pos_ship[0]+40,pos_ship[1]+40]
flag=0

def cut(s):
	if s.endswith('\n'):
		return s[1:-1]
	else:
		return s[1:]


def rot_center(image, angle):
   
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
    

while True :
    u="  ";
    while(not(u[0]=='$')):
		u=ser.readline()
    y_axis=int(cut(u))	
    while(not(u[0]=='#')):
		u=ser.readline()	
    x_axis=int(cut(u))
    if (y_axis<80 and y_axis>0) :
                        #if event.key==K_UP:
                                speed[1]=-200
    elif (y_axis<255 and y_axis>150) :
                        #if event.key==K_DOWN:   
                                speed[1]=+200
    else:
		speed[1]=+0
    if (x_axis<255 and x_axis>160) :
                        #if event.key==K_UP:
                                speed[0]=-200
    elif (x_axis<94 and x_axis>0) :
                        #if event.key==K_DOWN:   
                                speed[0]=+200
    else:
		speed[0]=+0	
    forward=[math.cos(angle),math.sin(angle)]
    
    ms=clock.tick()
    sec=ms/1000.0 
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame. quit()
            sys.exit
        if event.type==KEYDOWN:
            if event.key==K_UP:
                a=True
            if event.key==K_RIGHT:
                omega=+2
            if event.key==K_LEFT:
                omega=-2
            if event.key==K_SPACE:
                     flag=1
                     
                                
        if event.type==KEYUP:
            if event.key==K_UP:
                a=False
            if event.key==K_RIGHT:
                omega=0
            if event.key==K_LEFT:
                omega=0 
    
    angle+=omega*sec
    if not a:
        speed[0]*=0.992
        speed[1]*=0.992
        Ship=ship
    elif a:
        speed[0]+=sec*forward[0]*600
        speed[1]+=sec*forward[1]*600
        Ship=ship1
        
    spaceship=pygame.image.load(Ship).convert_alpha()
    forward=[math.cos(angle),math.sin(angle)]
    spaceship1=rot_center(spaceship,-57.1*angle)
    pos_ship[0]+=speed[0]*sec   
    pos_ship[1]+=speed[1]*sec
    screen.blit(background,(0,0))
    screen.blit(debris,[x-400,30])
    screen.blit(debris,[x,30])
    screen.blit(debris,[x+400,30])
    
    screen.blit(spaceship1, pos_ship, (0, 0, 90, 90))

    if flag==1:
                sd=600*sec
                p+=sd*bullet_f[0]
                q+=sd*bullet_f[1]
                screen.blit(shot,[p,q])
                pygame.display.flip()
                pygame.display.update()
                screen
                if (p<0 or p >800 or q <0 or q > 600):        
                     flag=0
                     
    if flag==0:
                [p,q]=[pos_ship[0]+40,pos_ship[1]+40]      
                bullet_f=forward
    d=s*sec
    x+=d
    if x>400:
        x=0
    
    
    if pos_ship[0]>800:
        pos_ship[0]=0
    elif pos_ship[0]<0:
        pos_ship[0]=800
    if pos_ship[1]>600:
        pos_ship[1]=0
    elif pos_ship[1]<0:
        pos_ship[1]=600
    
    pygame.display.update()
    

