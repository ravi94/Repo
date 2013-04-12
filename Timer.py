import simplegui
mins=0
sec=0
s=0
message='0:0:0'


def timer_handler():
    global message,sec,mins,s,draw
    
    if sec==59:
        sec=0
        mins+=1
    if s==9:
        s=0
        sec+=1
    else:
        s+=1  
    message = str(str(mins) + ':' + str(sec) + ':' +str(s))
    
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")
    
def time_start():
   timer.start() 
    
def time_stop():
   timer.stop()       

def time_reset():
    timer.stop()
    global mins,sec,s,message
    mins=0
    sec=0
    s=0
    message = str(str(mins) + ':' + str(sec) + ':' +str(s))
    
    


# Create a frame and assign callbacks to event handlers
timer = simplegui.create_timer(100, timer_handler)
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Start", time_start,100)

frame.add_button("Stop", time_stop,100)
frame.add_button("Reset", time_reset,100)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


