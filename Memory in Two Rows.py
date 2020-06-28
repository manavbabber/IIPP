import simplegui
import random
card1=0
card2=0
turns=0
state=0
def newgame():
    global deck_cards,turns,state,exposed_cards
    turns=0
    deck_cards=[i%8 for i in range(32)]
    exposed_cards=[False for i in range(32)]
    random.shuffle(deck_cards)
    label.set_text("Turns = "+str(turns))
def mouseclick(pos):
    global deck_cards,card1,card2,turns,state,exposed_cards
    choice=int(pos[0]/50) 
    if(int(pos[1]/100)>0):
        choice+=16
    print choice
    if state==0:
        state=1
        card1=choice
        exposed_cards[card1]=True
    elif state==1:
        if not exposed_cards[choice]:
            state=2
            card2=choice
            exposed_cards[card2]=True
            turns+=1
    else:
        if not exposed_cards[choice]:
            if deck_cards[card1]==deck_cards[card2]:
                pass
            else:
                exposed_cards[card1]=False
                exposed_cards[card2]=False
            state=1
            card1=choice
            exposed_cards[card1]=True
            label.set_text("Turns = "+str(turns))
def draw(canvas):
    for i in range(32):
        if i>=0 and i<=15:
            j=0
        else:
            j=1
        if i>=0 and i<=15:
            if exposed_cards[i]:
                canvas.draw_text(str(deck_cards[i]),[50*i+10,70*(j+1)],45,"Yellow")
            else:
                canvas.draw_polygon([(50*i,100*j),(50*(i+1),100*j),(50*(i+1),100*(j+1)),(50*i,100*(j+1))],5,"Red","Blue")
        else :
            if exposed_cards[i]:
                canvas.draw_text(str(deck_cards[i]),[50*(i-16)+10,80*(j+1)],45,"Yellow")
            else:
                canvas.draw_polygon([(50*(i-16),100*j),(50*((i-16)+1),100*j),(50*((i-16)+1),100*(j+1)),(50*(i-16),100*(j+1))],5,"Red","Blue")
            
frame=simplegui.create_frame("Memory Game",800,200)
frame.add_button("Reset",newgame)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)
label=frame.add_label("Turns=0")
newgame()
frame.start()