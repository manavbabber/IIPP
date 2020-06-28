"""
A simple adaptation of the game 'Flappy Bird'. The player controlles a 'bird' that is always falling
and it is their job to flap the bird's wings to propel it up, down, left, and right to stay on the screen
while avoiding 'pipes' that limit the playfield. 
Author: Jesse Battalino
Created by: Dong Nguyen, All Rights Reserved
Version: 1.0, 5/31/2018

Current features:
- Bird falls if there is no input and can be moved in any direction using the arrow keys.
- Pipes are generated with a passageway somewhere on the playfield.
- Touching the solid portions of the pipes, the ceiling, the floor, or the right-most edge of the
playfield results in death.
- Bird 'bounces' off left-most wall if moved into it, but is not penalized for doing so.
- Passing a pipe increments the player's current score by 1.
- Keeps track of high score over the course of subsequent plays.
- Waits for spacebar input to begin each game.
- Can pause the game with the spacebar.
- Pipes will generate and move across the screen faster based on current score.

Possible updates:
- Allow the player to enter their name to display next to their high score.
- Improve velocity to be a changing value over time to better represent the physics of falling.
- Allow pipes to alter the size of their passageways as score increases to increase difficulty.
- Allow pipes to alter their widths as score increases to increase difficulty.

"""

import simplegui
import random

WIDTH = 600
HEIGHT = 400
r = 20
DIED = False
high_score = 0

class Bird:
    """ The player controlled character with a pos and vel. """
    def __init__(self):
        self.pos = [WIDTH // 4, HEIGHT // 4]
        self.vel = [0, 4]
        
    def move(self):
        for i in range(2):
            self.pos[i] += self.vel[i]
            
    def hit_left_wall(self):
        if self.pos[0] - r < 0:
            self.vel[0] = 4

class Pipe:
    """ An obstacle that the player must flap through. """
    def __init__(self, y):
        self.x = WIDTH
        self.y = y
        self.size = 40
        self.spawner = False
        self.passed = False
        
    def update(self, score):
        self.x -= (2 + (score // 4))
        
    def draw_pipe(self, canvas):
        canvas.draw_line([self.x, 0], [self.x, self.y - 50], self.size, "White")
        canvas.draw_line([self.x, self.y + 50], [self.x, HEIGHT], self.size, "White")
        
    def collide(self, bird):
        global DIED
        # find the span of the x plane that bird is occupying
        bird_x_field_left 	= bird.pos[0] - r
        bird_x_field_right	= bird.pos[0] + r
        bird_y_field_up		= bird.pos[1] - r
        bird_y_field_down	= bird.pos[1] + r
        
        # check if bird has hit ceiling or floor
        if bird_y_field_up < 0 or bird_y_field_down > HEIGHT or bird_x_field_right > WIDTH:
            DIED = True
            return True
        
        # check as we approach an oncoming pipe or back up into a passed pipe
        if ((bird_x_field_right > self.x and bird_x_field_right < self.x + self.size) or
            (bird_x_field_left < self.x + self.size and bird_x_field_left > self.x)):
            # bird is occupying the same x coordinate as a pipe
            if (bird_y_field_up < self.y - 75 or
               bird_y_field_down > self.y + 75):
                DIED = True
                return True
        return False
            
        
def spawn_pipe():
    return Pipe(random.randrange(64, HEIGHT - 64))
            
def start_game():
    global bird, ready, start_message, pipes, hole, score, DIED, high_score, high_score_message
    score = 0
    hole = 50
    bird = Bird()
    ready = False
    DIED = False
    start_message = "Press Spacebar To Start! Tap Arrow Keys To Play."
    high_score_message = "High Score: " + str(high_score)
    
    pipes = []
    pipes.append(spawn_pipe())
        
def draw(canvas):
    global pipes, ready, start_message, score, high_score
    canvas.draw_text(start_message, [WIDTH // 10, (3 * HEIGHT) // 4], 24, "Blue")
    canvas.draw_text(high_score_message, [WIDTH // 8, 18], 18, "Red")
    
    if ready:
        canvas.draw_circle(bird.pos, r, 2, "Red", "Black")
        # update bird
        bird.move()
        bird.hit_left_wall()
        for pipe in pipes:
            # draw current pipe
            pipe.draw_pipe(canvas)
            
            # check if bird is touching pipe
            if pipe.collide(bird):
                ready = False
                start_message = "Ouch! Your score is " + str(score) + ". Hit Spacebar to restart."
                if score > high_score:
                    high_score = score
            
            pipe.update(score)
            
            # check if bird is passed pipe and update score
            if (bird.pos[0] - r > pipe.x + pipe.size) and not pipe.passed:
                score += 1
                pipe.passed = True
            
            # spawn new pipe
            if pipe.x < (WIDTH // 3) and not pipe.spawner:
                pipes.append(spawn_pipe())
                pipe.spawner = True
                
    canvas.draw_text("Score: " + str(score), [WIDTH // 8, HEIGHT // 8], 36, "Yellow")

def keydown(key):
    global ready, start_message
    map = simplegui.KEY_MAP
    
    if not ready and not DIED:
        if key == map["space"]:
            ready = True
            start_message = ""
    elif not ready and DIED:
        if key == map["space"]:
            start_game()
    else:
        if key == map["space"]:
            ready = False
            start_message = "Hit Spacebar to continue."
    
    if key == map["up"]:
        bird.vel[1] -= 8
    elif key == map["right"]:
        bird.vel[0] += 4
    elif key == map["left"]:
        if bird.pos[0] - r < 0:
            bird.pos[0] += 1
        else:
            bird.vel[0] -= 4
    elif key == map["down"]:
        bird.vel[1] += 6
        
def keyup(key):
    map = simplegui.KEY_MAP
    if key == map["up"]:
        bird.vel[1] = 4
    elif key == map["right"]:
        bird.vel[0] = 0
    elif key == map["left"]:
        bird.vel[0] = 0
    elif key == map["down"]:
        bird.vel[1] = 4

frame = simplegui.create_frame("Flppy", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

start_game()
frame.start()