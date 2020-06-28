import simplegui

t=0
count=0
success=0
total=0
countsuccess=0
interval=1000

def start():
    timer.start()
    
def stop():
    global count,success,countsuccess
    timer.stop()
    if(count%60 == 0 and count != 0):
        success+=1
        countsuccess+=1
    elif(count != 0):
        countsuccess += 1
def reset():
    global count,success,countsuccess,total,t
    t=0
    count=0
    success=0
    total=0
    countsuccess=0

def format(t):
    a=t%60
    b=(t/60)%60
    d=(t/3600)%24
    string = str(d)+":"+str(b)+":"+str(a)
    return string

def draw(canvas):
    text = format(count)
    canvas.draw_text( text, (80, 125), 42, "white")
    canvas.draw_text(str(success) + '/' + str(countsuccess), (190,30), 24, "pink") 

def tick():
    global count
    count += 1

timer = simplegui.create_timer(interval,tick)
frame = simplegui.create_frame("Stopwatch",250,200)
frame.set_draw_handler(draw)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.start()