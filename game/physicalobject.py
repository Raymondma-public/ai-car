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
        self.dead = False

    def update(self, dt):
        """This method should be called every frame."""
        self.y -= self.velocity_y * dt
        
        # Wrap around the screen if necessary
        self.check_bounds()
    
    def check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior"""
        min_x = 0       #-self.image.width/2
        min_y = 0       #-self.image.height/2
        max_x = 800     #+ self.image.width/2
        max_y = 600     # + self.image.height/2
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
        collision_distance = self.image.width/2 + other_object.image.width/2
        
        # Get distance using position tuples
        actual_distance = distance(self.position, other_object.position)
        
        return (actual_distance <= collision_distance)
    
    def handle_collision_with(self, other_object):
        self.dead = True
    