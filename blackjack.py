import simplegui
import random

CARD_SIZE=(73,98)
CARD_CEN=(36.5,49)
RANKS=list("A23456789TJQK")
SUITS=list("CSHD")
VALUES={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':10,'Q':10,'K':10}
rank=random.choice(RANKS)
suit=random.choice(SUITS)



card_image=pygame.image.load("cards.png").convert()
card_back=simplegui.load_image("card_back.jpg").convert()
user=[]
comp=[]
u_value=0
c_value=0

in_play=True
msg=""

class Card:
    def __init__(self,p):
        self.suit=p[0]
        self.rank=p[1]
    
    def get_suit(self):
        return self.suit
   
    def get_rank(self):
        return self.rank    
        
    def draw(self,canvas,loc,who):
        k=0
        for c in who:           
            i=RANKS.index(c[1])
            j=SUITS.index(c[0])
            card_pos=[CARD_CEN[0]+ i*CARD_SIZE[0],
                      CARD_CEN[1]+ j*CARD_SIZE[1]]
            canvas.draw_image(card_image,card_pos,CARD_SIZE,[loc[0]+(k*(CARD_SIZE[0]+10)),loc[1]],CARD_SIZE)
            k+=1

# Handler to draw on canvas
def draw(canvas):
    global msg,in_play,u_value,c_value
    card_user.draw(canvas,[170,420],user)
    card_comp.draw(canvas,[170,200],comp)
    canvas.draw_text("BLACKJACK", (200,50), 40, "lime")
    canvas.draw_image(card_back,(116,103), CARD_SIZE, (80,310), CARD_SIZE)
    canvas.draw_image(card_back,(116,103), CARD_SIZE, (83,313), CARD_SIZE)
    canvas.draw_image(card_back,(116,103), CARD_SIZE, (86,316), CARD_SIZE)
    canvas.draw_image(card_back,(116,103), CARD_SIZE, (77,307), CARD_SIZE)
    canvas.draw_text("YOUR's Card Value : "+str(u_value), (130,500), 20, "yellow")
    canvas.draw_text("COMPUTER's Card Value : "+str(c_value), (130,130), 20, "yellow")    
    if not in_play:
        canvas.draw_text(msg, (300,350), 30, "indigo")
    else:
        canvas.draw_text("Hit OR Stand ?", (200,350), 20, "white")

def deal():
    global in_play,u_value,c_value,user,comp
    user=[]
    comp=[]
    u_value=0
    c_value=0
    in_play=True
    card_user=Card(card_maker()) 
    user.append([card_user.get_suit(),card_user.get_rank()])
    card_user=Card(card_maker()) 
    user.append([card_user.get_suit(),card_user.get_rank()])   
    card_comp=Card(card_maker())
    comp.append([card_comp.get_suit(),card_comp.get_rank()])
    u_value=calc_value(user)
    c_value=calc_value(comp) 

def stand():
    global in_play,comp_state,c_value,msg
    if in_play:
        while(c_value<=17):
            card=Card(card_maker())
            if VALUES[card.get_rank()]<7:
                comp.append([card.get_suit(),card.get_rank()]) 
                c_value=calc_value(comp)
            
        in_play=False    
        if c_value<=21 and (c_value>u_value):
             msg="You lose,Dealer wins" 
        elif c_value<=21 and (c_value<u_value):   
             msg="You win,Dealer lose"
        elif c_value<=21 and (c_value==u_value):
             msg="TIE"
        else:       		 
            msg="You win,Dealer Busted"                     
                
def hit():
    global in_play,u_value,c_value,msg
    if in_play:
           card=Card(card_maker())
           user.append([card.get_suit(),card.get_rank()]) 
           u_value=calc_value(user)
           if u_value>21:
                in_play=False
                msg="You BUSTED"
                
def card_maker():
    global RANKS,SUITS
    return random.choice(SUITS),random.choice(RANKS)

def calc_value(l):
    value=0
    for x in l:
        value=value+VALUES[x[1]]
    
    a=0
    for x in l:
       if x[1]=='A':
            a+=1
    if a==0:
        return value
    else:
        if (value+10)<=21:
            return value+10
    
        else:
            return value


card_user=Card(card_maker()) 
user.append([card_user.get_suit(),card_user.get_rank()])
card_user=Card(card_maker()) 
user.append([card_user.get_suit(),card_user.get_rank()])
card_comp=Card(card_maker())
comp.append([card_comp.get_suit(),card_comp.get_rank()])
u_value=calc_value(user)
c_value=calc_value(comp) 


frame = simplegui.create_frame("Home", 600, 600)
frame.set_canvas_background("Green")
frame.add_button("Deal", deal, 200)
label = frame.add_label("")
frame.add_button("Hit", hit, 200)
label = frame.add_label("")
frame.add_button("Stand", stand, 200)
label = frame.add_label("")
label = frame.add_label("Your Card value must be less than 21 and greater than dealer's card value to WIN. For more querry on rule check the rules of blackjack on google")

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

