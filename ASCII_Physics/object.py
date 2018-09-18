class Object:
    def __init__(self, pos=(0,0), vel=(0,0), acc=(0,0), char="x"):
        self.x = pos[0]
        self.y = pos[1]
        self.vx = vel[0]
        self.vy = vel[1]
        self.ax = acc[0]
        self.ay = acc[1]
        self.char = char

    def update(self, grain, dim):
        self.vx += self.ax / grain
        self.x += self.vx / grain
        self.vy += self.ay / grain
        self.y += self.vy / grain

        if self.x > dim[0]:
            self.vx = -self.vx*0.99
            self.x = dim[0]
        elif self.x < 0:
            self.vx = -self.vx*0.99
            self.x = 0
        if self.y > dim[1]:
            self.vy = -self.vy*0.99
            self.y = dim[1]
        elif self.y < 0:
            self.vy = -self.vy*0.99
            self.y = 0