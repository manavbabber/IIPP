import simplegui

# Global Variables
t=0
count=0
success=0
countsuccess=0
interval=100

def start():
    timer.start()

def stop():
    global count,success,countsuccess
    timer.stop()
    if(count%10==0 and count!=0):
        success+=1
        countsuccess+=1
    elif(count!=0):
        countsuccess+=1

def reset():
    global t,success,countsuccess,count
    count=0
    success=0
    countsuccess=0
    
def tick():
    global count
    count+=1
    
def format(t):
    d=str(t%10)
    c=str((t/10)%10)
    b=str((t/100)%6)
    a=str((t/600)%600)
    string=a+":"+b+c+":"+d
    return string

def draw(canvas):
    text = format(count)
    canvas.draw_text( text, (80, 125), 42, "white")
    canvas.draw_text(str(success) + '/' + str(countsuccess), (190,30), 24, "pink")     

#Creating Frame   
frame = simplegui.create_frame("Stopwatch game", 250, 250)

#Add Buttons
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

frame.set_draw_handler(draw)

#Creating Timer
timer = simplegui.create_timer(interval, tick)

frame.start()