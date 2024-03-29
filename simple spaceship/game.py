# images 
ship="sp.png"
ship1="sp1.png"
bg= "bg.png"
db="debris.png"
sh="shot1.png"
ast="asteroid.png"
e="explosion.png"
start = "start.jpg"



import pygame,time,random,math
from pygame.locals import *

import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.flushInput()
# variable declaration
Ship=ship
shots=[]
s=30
d=0 ; a=0
x=800 ;speed=[0,0] ; 
pos_ship=[100,201]
flag=0
done0=True ; done=True ; done2=True
[a,b]=[pos_ship[0]+60,pos_ship[1]+28]
[p,q]=[800,random.randint(90,510)]
ae =0 ; sh_e=0
score=0
level=0 ; left=0
astr_s=201 ; t=200

pygame.init()
screen=pygame.display.set_mode((800,600),0,32)
background0=pygame.image.load(start).convert()
background=pygame.image.load(bg).convert()
background2=pygame.transform.flip(background,1,0)
shot=pygame.image.load(sh).convert_alpha()    
debris=pygame.image.load(db).convert_alpha()
astr=pygame.image.load(ast).convert_alpha()
explosion=pygame.image.load(e).convert_alpha()


font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 80)

text3 = font1.render("Game Over", 1, (255, 0, 0))
text4 = font1.render("Press any key to Quit...", 1, (255, 0, 0))
text6 = font1.render("Press any key to Start....", 1, (255, 0, 0))
Pause=False



def dist((e,f),(g,h)):
        return math.sqrt( (e-g)**2 + (f-h)**2)

def cut(s):
        if s.endswith('\n'):
                return s[1:-1]
        else:
                return s[1:]


        
while done0 : 
	screen.blit(background0,(0,0))   
	screen.blit(text6,[100,201])
        pygame.display.update()
        
        for event in pygame.event.get():
                        if event.type==QUIT:
                                done0=False
				done=False
				done2=False	
                                
                        if event.type==KEYDOWN:
                                done0=False
	
clock=pygame.time.Clock()	
	 
while done :
 
        u="  ";
        while(not(u[0]=='$')):
                u=ser.readline()
        y_axis=int(cut(u))      
        while(not(u[0]=='#')):
                u=ser.readline()        
        x_axis=int(cut(u))
        if (y_axis<90 and y_axis>-22) :
                        #if event.key==K_UP:
                                speed[1]=-250
        elif (y_axis<255 and y_axis>130) :
                        #if event.key==K_DOWN:   
                                speed[1]=+250
        else:
                speed[1]=+0
        if (x_axis<255 and x_axis>140) :
                        #if event.key==K_UP:
                                speed[0]=-250
        elif (x_axis<114 and x_axis>0) :
                        #if event.key==K_DOWN:   
                                speed[0]=+250
        else:
                speed[0]=+0     
        
        text1 = font.render("Score : "+str(score), 1, (255, 0, 0))
        text2 = font.render("Level : "+str(level), 1, (255, 0, 0))
        text5 = font.render("Unshot Asteroid : "+str(left), 1, (255, 0, 0))
        
# defining Clock        
        ms=clock.tick()
        sec=ms/1000.0
        
        
# score and level check        
        if score == 10:
                astr_s+=(0.5*astr_s)
                score=0
                level+=1
                t+=30
                
           
        spaceship=pygame.image.load(Ship).convert_alpha()
        

# Key control        
        for event in pygame.event.get():
                if event.type==QUIT:
                        done=False
                        done2=False
                
                if event.type==KEYDOWN:
                        #if (mat<94 and mat>0) :
                        if event.key==K_UP:
                                speed[1]=-t
                        #if (mat<255 and mat>160) :
                        if event.key==K_DOWN:   
                                speed[1]=+t
                                
                        if event.key==K_RIGHT:
                                speed[0]=+t
                                
                        if event.key==K_LEFT:
                                 speed[0]=-t
                                 
                        if event.key==K_SPACE:
                                flag=1
			if event.key==K_ESCAPE:
                                Pause=True				
				
                if event.type==KEYUP:
                        if event.key==K_UP:
                                speed[1]=0
                        if event.key==K_DOWN:
                                speed[1]=0
                        if event.key==K_RIGHT:
                                Ship=ship
                                speed[0]=0
                        if event.key==K_LEFT:
                                speed[0]=0

	while (Pause==True):
		if event.key==K_ESCAPE:
                                Pause=False	

# Ship Control
        if sh_e==0:
                if pos_ship[0]>-1 and pos_ship[0]+81<801:
                        
                        pos_ship[0]+=speed[0]*sec
                elif pos_ship[0]<0:
                        pos_ship[0]+=2
                elif pos_ship[0]+81>800:
                        pos_ship[0]-=2
                                
                if pos_ship[1]>-1 and pos_ship[1]+81<601:        
                        pos_ship[1]+=speed[1]*sec
                elif pos_ship[1]<0:
                        pos_ship[1]+=2
                elif pos_ship[1]+81>600:
                        pos_ship[1]-=2
        screen.blit(background,(0,0))       
        screen.blit(debris,[x-400,30])
        screen.blit(debris,[x,30])
        screen.blit(debris,[x-800,30])
        screen.blit(text1, [0,0])
        screen.blit(text2, [600,0])
        screen.blit(text5, [250,0])
        d=s*sec
        x-=d
        if x<400:
                x=800
        if not sh_e == 1 : 
                screen.blit(spaceship, pos_ship)
        
# generate a asteroid and move it
        astr_c=[p+45,q+45]
        ship_c=[pos_ship[0]+40,pos_ship[1]+40]
       
        if (p<=0):
               [p,q]=[800,random.randint(90,510)]
               left+=1
               if left==10:
                       done=False

        elif(not ae==1):
                sa=astr_s*sec
                p-=sa
                if p <850:
                        screen.blit(astr,[p,q])
                        pygame.display.update()        
# fire a bullet        
        if flag==1:
                sd=800*sec
                a+=sd
                screen.blit(shot,[a,b])
                pygame.display.update()
                if dist([a,b],astr_c)<50:
                        r=astr_c
                        score+=1
                        ae=1
                        ta=8
                        a=801 ;[p,q]=[800,random.randint(90,510)]
                        
                if (a>800):        
                     flag=0
                     
        if flag==0:        
                [a,b]=[pos_ship[0]+60,pos_ship[1]+28]

# do explosion

        if ae==1 :
                if ta<72:
                        ei=[ta%9, (ta//9)%9]
                        screen.blit(explosion,(r[0]-45,r[1]-45),[(50+ei[0]*100)-45,(50+ei[0]*100)-45,100,100])
                        pygame.display.update()
                        ta+=1
                else:
                         ae=0
                         

        if dist(ship_c,astr_c)<70:
                sh_e=1
                ts=8
                p=900
    
        if sh_e==1 :
                if ts<72:
                        ei=[ts%9, (ts//9)%9]
                        screen.blit(explosion,(pos_ship[0],pos_ship[1]),[(50+ei[0]*100)-45,(50+ei[0]*100)-45,100,100])
                        screen.blit(explosion,(astr_c[0]-45,astr_c[1]-45),[(50+ei[0]*100)-45,(50+ei[0]*100)-45,100,100])
                        pygame.display.update()
                        ts+=1
                else:
                        done=False

        pygame.display.update()

while done2:
        
        screen.blit(text3,[100,201])
        screen.blit(text4,[100,400]) 
        pygame.display.update()
        
        for event in pygame.event.get():
                        if event.type==QUIT:
                                done2=False
                                
                        if event.type==KEYDOWN:
                                done2=False
ser.flushInput()
pygame.quit()
                 
"""
1. ===> Grnd
2. ===> 3.3
3. ===> 5V
4. ===> A4
5. ===> A5
"""                                               
                                
