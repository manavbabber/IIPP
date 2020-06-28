import simplegui
import random
import math
secret_num=0
num_range=100
guess_left=7
def new_game():
    global num_range
    global secret_num
    global guess_left
    secret_num=random.randrange(0,num_range)
    guess_left=math.ceil(math.log(num_range,2))
    print ""
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is",guess_left
def range1():
    global num_range
    global guess_left
    num_range=100
    guess_left=7
    new_game()
def range2():
    global num_range
    global guess_left
    num_range=1000
    guess_left=10
    new_game()
def input_guess(guess):
    global guess_left
    global secret_num
    guess_num = int(guess)
    print ""
    print "Guess was ", guess_num
    print "Number of remaining guesses is", guess_left    
    if guess_num == secret_num:
        print "Correct!"
        new_game()
    elif guess_num < secret_num:
        print "Higher!"
        guess_left -=1
    elif guess_num > secret_num:
        print "Lower!"
        guess_left -=1
    elif guess_left == 0:
        print "Remaining Guesses are zero now. Actually the number is",secret_num
        new_game()
frame=simplegui.create_frame("My Frame",500,500)
frame.add_button("Range is [0,100]",range1,100)
frame.add_button("Range is [0,1000]",range2,100)
frame.add_input("Enter the random number",input_guess,100)
frame.start()
new_game()