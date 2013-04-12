import random
import simplegui

temp=[]

move=0

i=1
b=[1,2,3,4,5,6,7,8,9,10,11,12]
d = list("youwin"*2)
random.shuffle(d)  
c=dict(zip(b,d))  


def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

def indexing(position):
    j=1 
    while(j<=12):        
        if position[0] in (range(50*(j-1),50*j)):
           return j    
        j+=1           


# Handler for mouse click
def click(pos):
    global temp,move
    temp=uniq(temp)
    x=indexing(pos)
    if x not in temp:
        move+=1

    if len(temp)==2 :
        if c[temp[-1]]!=c[temp[-2]]:
                temp.pop()
                temp.pop()
                temp.append(x)
        else:
             temp.append(x)
    
    if len(temp)<2 :
        temp.append(x)
        
    if len(temp)>2:
        if c[temp[-1]]!=c[temp[-2]]:
                if c[temp[-2]]!=c[temp[-3]]:
                  temp.pop()
                  temp.pop()
                  temp.append(x)
                else:
                    temp.append(x) 
        else:
            
            temp.append(x)
    print move
    label.set_text("Move = "+ str(move))
       
       
# Handler to draw on canvas
def draw(canvas): 
    global c
    i=1    
    while(i<13):
        canvas.draw_line([50*i, 0], [50*i, 100], 2, "Blue")
        i+=1     
    if len(temp)==12:
        c=dict(zip(b,"! YOU WIN ! "))         
    for n in temp:
         canvas.draw_text(c[n], ((50*(n-1)+10), 60), 50, "Red")

def restart():
    global temp,move,c,b,d
    temp=[]
    move=0
    b=[1,2,3,4,5,6,7,8,9,10,11,12]
    d = list("youwin"*2)
    random.shuffle(d)  
    c=dict(zip(b,d))  
    label.set_text("Move = 0")
       
    frame.start()

            
     
frame = simplegui.create_frame("Memory Game", 600, 100)    
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
label = frame.add_label("Moves = 0")
button1 = frame.add_button("Play Again", restart)


# Start the frame animation
frame.start()

