#imported modules

import random
import simplegui
import math

# global variables
width_canvas=400
height_canvas=500
width_dash=80
radius =10
pos_ball=[200,250]
pos_dash=[[width_canvas/2,500],[width_canvas/2+width_dash,500]]

x=random.choice([random.randint(-60,-15),random.randint(15,60)])
y=random.randint(50,100)
vel_x=x/math.sqrt(math.pow(x,2)+math.pow(y,2))
vel_y=y/math.sqrt(math.pow(x,2)+math.pow(y,2))
vel=[3*vel_x,3*vel_y]
vel_dash=0
score=0
norm=[0,0]
que=[]
n=10

class Ball():
    def __init__(self,raidus,color):
        self.radius=radius
        self.color=color
        self.pos=[width_canvas/2,height_canvas/2]
        x=random.choice([random.randint(-60,-15),random.randint(15,60)])
        y=random.randint(50,100)
        vel_x=x/math.sqrt(math.pow(x,2)+math.pow(y,2))
        vel_y=y/math.sqrt(math.pow(x,2)+math.pow(y,2))
        self.vel=[2*vel_x,2*vel_y]
             
    
    def reflect(self):
        global norm
        norm=normal(self.pos)
        self.vel[0]=self.vel[0] - 2*self.vel[0]*norm[0]
        self.vel[1]=self.vel[1] - 2*self.vel[1]*norm[1]
        
    def get_pos(self):
        return self.pos
        
    
    def update(self):
        global score
        if self.pos[1] < height_canvas + 30 and self.pos[1] >-2 :
            self.pos[0]+=2*self.vel[0]
            self.pos[1]+=2*self.vel[1]
            
            if (self.pos[1]<= self.radius+40):
                    self.vel[0]= 1.1*self.vel[0]
                    self.vel[1]= 1.1*self.vel[1]
                
            if not inside(self.pos,self.radius):
                self.reflect()
               
        elif self.pos[1] >= height_canvas + 30:
            self.pos[1]=-535
            score-= len(que)*50
         
    def draw(self,canvas):
        canvas.draw_circle(self.pos,self.radius,1,self.color,self.color)
        


def draw(canvas): 
       global score 
       if len(que) ==0:
            canvas.draw_text("Your Score is :"+str(score), (width_canvas/2-150, height_canvas/2), 40, "Red")
       for balls in que:
           c=balls.get_pos() 
           if c[1]==-535:
                que.pop(que.index(balls))
           balls.update()
           balls.draw(canvas)
                
       if pos_dash[0][0]>=0 and pos_dash[1][0]<=400:
           pos_dash[0][0]+= vel_dash 
           pos_dash[1][0]+= vel_dash 
       if pos_dash[0][0]<0 :     
            pos_dash[0][0]+= 1 
            pos_dash[1][0]+= 1
       if pos_dash[1][0]>400:
            pos_dash[0][0]-= 1
            pos_dash[1][0]-= 1 
            
       canvas.draw_polygon(pos_dash, 25, "Green")
       
       canvas.draw_line((0, 40), (400, 40), 1, "Blue")      
       canvas.draw_text('Score : '+str(score), (10,30), 20, "indigo") 
       canvas.draw_text('Number of extra balls left :'+str(n), (150,30), 20, "indigo")      
       canvas.draw_text('Made by : Ravi', (300,498), 15, "red")           
        
def inside(pos,radius):
    
    if (pos[0]>= radius) and (pos[0] <= width_canvas-radius) and (pos[1]>= radius+40) and (pos[1] <= float(height_canvas-(radius+12))):
        return True
    else :
        return False
        
    
def normal(pos):
    global width_canvas,height_canvas,score,pos_dash
    a=pos_dash[0][0]
    b=pos_dash[1][0]
    c=pos[0]     
    
    if pos[0]<=radius or (pos[0] >= width_canvas-radius):
        return [1,0]
    elif (pos[1] >= float(height_canvas-12-radius) and c>=a and c<=b):
            score+=10
            return [0,1]             
    elif pos[1]<=radius +40:
        return [0,1]
    else:
        return [0,0]
        
    
def key_down(key):
    global vel_dash
    vel_dash=5
    if key==simplegui.KEY_MAP["left"]:
        vel_dash=-5
    elif key==simplegui.KEY_MAP["right"]:
         vel_dash= +5
    else:
        vel_dash=0        
        
def key_up(key):
    global vel_dash
    vel_dash=0
    
    
def add_ball():
    global n
    if n>0:
        color=["red","green","blue","white","yellow","olive"]
        ball1=Ball(10,random.choice(color))
        que.append(ball1)
        n=n-1
        
ball=Ball(10,"red",)  
que.append(ball)

def play():
    global que,n
    que=[]
    ball=Ball(10,"red",)  
    que.append(ball)
    n=10
    

frame = simplegui.create_frame("Home", width_canvas, height_canvas)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_draw_handler(draw)
frame.add_button("Play Again",play, 200)
label = frame.add_label(" ")
label = frame.add_label("Add more balls on screen to get more points.")
label = frame.add_label("")
frame.add_button("More ball", add_ball, 200)
label = frame.add_label("")
label = frame.add_label("Rule: Gain 10 point by saving one ball and lose 50 (times the number of ball that was present on screen) points by leaving the ball to fall.")
label = frame.add_label("")
label = frame.add_label("Note : Speed of the ball increases every time it hits the upper blue line. ")
frame.set_canvas_background("khaki")



# Start the frame animation
frame.start()




