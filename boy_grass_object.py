from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,31)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(50,700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(20, 750), 599
        self.BorS = random.randint(0,2)
        self.speed = random.randint(5,15)
        self.image1 = load_image('ball21X21.png')
        self.image2 = load_image('ball41X41.png')
    def update(self):
        if self.BorS == 0:
            if self.y - 10 > 50:
                self.y -= self.speed
        else:
            if self.y - 20 > 50:
                self.y -= self.speed
    def draw(self):
        if self.BorS == 0:
            self.image1.clip_draw(0,0,21,21,self.x,self.y)
        else:
            self.image2.clip_draw(0,0,41,41,self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

team = [Boy() for i in range(11)]
twenty = [Ball() for i in range(20)]
grass = Grass()

running = True

# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()
    for ball in twenty:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in twenty:
        ball.draw()
    update_canvas()
    delay(0.05)

# finalization code
close_canvas()