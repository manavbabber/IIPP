import simplegui
import random
height=600
width=600
paddle1_pos=float(height/2)
paddle2_pos=float(height/2)
paddle1_vel=0.0
paddle2_vel=0.0
ball_pos=[width/2,height/2]
ball_vel=[2,2]
radius=20
pad=10
half_pad=50
score1=0
score2=0
text = "PONG"
def init(direction):
    global ball_pos,ball_vel
    ball_pos=[width/2,height/2]
    ball_vel[0]=random.randrange(60,180)//60
    ball_vel[1]=random.randrange(60,180)//60
    if direction=="left":
        ball_vel[0]=-ball_vel[0]
def keydown(key):
    global paddle1_vel,paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel-=12
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel+=12
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel-=12
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel+=12
def keyup(key):
    global paddle1_vel,paddle2_vel
    if key==simplegui.KEY_MAP["w"] or key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["up"] or key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0        
def reset():
    global score1,score2,paddle1_vel,paddle2_vel,paddle1_pos,paddle2_pos,ball_vel,radius,ball_pos,height,width
    ball_vel=[2,2]
    ball_pos=[width/2,height/2]
    init('left')
    paddle1_vel,paddle2_vel=0,0
    paddle1_pos,paddle2_pos=float(height/2),float(height/2)
    score1,score2=0,0
def draw(canvas):
    global score1,score2,paddle1_vel,paddle2_vel,paddle1_pos,paddle2_pos,ball_vel,radius,ball_pos,height,width 
    canvas.draw_line([pad,0],[pad,height],1,"White")
    canvas.draw_line([width-pad,0],[width-pad,height],1,"White")
    canvas.draw_line([width/2,0],[width/2,height],1,"White")
    canvas.draw_circle(ball_pos,radius,1,"White","White")
    canvas.draw_line([0,paddle1_pos-half_pad],[0,paddle1_pos+half_pad],pad*2,"White")
    canvas.draw_line([width,paddle2_pos-half_pad],[width,paddle2_pos+half_pad],pad*2,"White")	
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    if ball_pos[1]<=radius or height-ball_pos[1]<=radius:
        ball_vel[1]=-ball_vel[1]
    if half_pad < paddle1_pos + paddle1_vel < height - half_pad:
        paddle1_pos += paddle1_vel
    if half_pad < paddle2_pos + paddle2_vel < height - half_pad:
        paddle2_pos += paddle2_vel
    
    if ball_pos[0] <= radius+pad:
        if paddle1_pos-half_pad <= ball_pos[1] <= paddle1_pos+half_pad:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0],ball_vel[1]=ball_vel[0]*1.2,ball_vel[1]*1.2
        else:
            score2+=1
            init('right')
    if width-ball_pos[0] <= radius+pad:
        if paddle2_pos-half_pad <= ball_pos[1] <= paddle2_pos+half_pad:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0],ball_vel[1]=ball_vel[0]*1.2,ball_vel[1]*1.2
        else:
            score1+=1
            init('left')
            
    canvas.draw_text(str(score1),[(width/4)-10,half_pad],40,"White")
    canvas.draw_text(str(score2),[(width/4)*3-10,half_pad],40,"White")
    canvas.draw_text(text,[(width/2-50),height],40,"White")
frame=simplegui.create_frame("Pong",width,height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset",reset,100)
frame.start()