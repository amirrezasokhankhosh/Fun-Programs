class Planet:
    def __init__(self, name, radius, distance, color, angle, x, y, velocity):
        self.name = name
        self.radius = radius
        self.distance = distance
        self.color = color
        self.angle = angle
        self.x = x
        self.y = y
        self.velocity = velocity
        
    def update_angle(self):
        self.angle += self.velocity
        
        