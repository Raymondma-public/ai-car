import pyglet, math


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)

class PhysicalObject(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""
    
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        
        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0
        # self.dead = False
        # self.new_objects=[]

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        # """This method should be called every frame."""
        # self.y -= self.velocity_y * dt
        #
        # # Wrap around the screen if necessary
        self.check_bounds()
    
    def check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior"""
        min_x = -self.image.width/2
        min_y = -self.image.height/2
        max_x = 1500 + self.image.width/2
        max_y = 800 + self.image.height/2
        # min_x = 0       #-self.image.width/2
        # min_y = 0       #-self.image.height/2
        # max_x = 800     #+ self.image.width/2
        # max_y = 600     # + self.image.height/2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
    
    def collides_with(self, other_object):
        """Determine if this object collides with another"""
        
        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        collision_distance = self.image.width/2 + other_object.image.width
        
        # Get distance using position tuples
        actual_distance = distance(self.position, other_object.position)
        
        return (actual_distance <= collision_distance)

    def collides_point_circle(self,px, py, r):
        distX = px - self.x
        distY = py - self.y
        distance = math.sqrt((distX * distX) + (distY * distY))
        return distance <= r

    def collides_line_point(self,x1, y1, x2, y2, px, py):

        d1 = distance((px, py), (x1, y1));
        d2 = distance((px, py), (x2, y2));

        lineLen = distance((x1, y1), (x2, y2));

        buffer = 0.1;

        return (d1 + d2 >= lineLen - buffer) and (d1 + d2 <= lineLen + buffer)

    def collides_line_circle(self,x1, y1, x2, y2, r):
        inside1 = self.collides_point_circle(x1, y1, r)
        inside2 = self.collides_point_circle(x2, y2, r)
        if (inside1 or inside2):
            return True

        distX = x1 - x2
        distY = y1 - y2
        len = math.sqrt((distX * distX) + (distY * distY))

        dot = (((self.x - x1) * (x2 - x1)) + ((self.y - y1) * (y2 - y1))) / pow(len, 2)

        closestX = x1 + (dot * (x2 - x1))
        closestY = y1 + (dot * (y2 - y1))

        onSegment = self.collides_line_point(x1, y1, x2, y2, closestX, closestY)
        if (not onSegment):
            return False

        # fill(255, 0, 0)
        # noStroke()
        # ellipse(closestX, closestY, 20, 20)

        distX = closestX - self.x
        distY = closestY - self.y
        float
        distance = math.sqrt((distX * distX) + (distY * distY))
        return distance <= r

    def handle_collision_with(self, other_object):
        self.dead = True
    
