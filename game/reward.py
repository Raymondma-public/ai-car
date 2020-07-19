import math
from pyglet.window import key
# import game.physicalobject, game.resources , game.load

from . import physicalobject
from . import resources
from . import load


class Reward:
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        self.x1=0;
        self.y1 = 0;
        self.x2 = 0;
        self.y2 = 0;

        self.thrust = 1300.0
        self.rotate_speed = 200.0
        # self.slow_down_speed=
        # self.speed = 0;
        self.rotation = -90
        self.scale=0.3
        # self.y = 0;
        # self.genome = None
        self.keys = dict(left=False, right=False,up=False, down=False)

    def on_key_press(self, symbol, modifiers):

        if symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False


    def check_keys(self,dt):
        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
            # if self.x == 300:
            #     self.x -= 100
            # else:
            #     self.x = 200

        if self.keys['right']:
            self.rotation += self.rotate_speed * dt

            # if self.x == 200:
            #     self.x += 100
            # else:
            #     self.x = 300

        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            # self.speed+=.5;
        if self.keys['down']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.velocity_x * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x *= .95
            self.velocity_y *= .95

        angle_radians = -math.radians(self.rotation)
        force_x = math.cos(angle_radians) * self.velocity_x * dt
        force_y = math.sin(angle_radians) * self.thrust * dt
        self.velocity_x *= .95
        self.velocity_y *= .95

        # if self.keys['down']:
        #     self.speed-=.5;

