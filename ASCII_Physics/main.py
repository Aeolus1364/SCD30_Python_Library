import time
import object
import os
import random
import string


class Main:
    def __init__(self):
        self.running = True
        self.framerate = 200
        self.time_grain = 10
        self.dim = (75, 20)
        self.r = Renderer(self.dim, False)
        self.objs = []
        self.load_text("Very large amount of text that keeps going on and on\ninto the next line and the line after that\nit just won't stop!", (0, 19))
        self.counter = 0
        #
        # for i in range(100):
        #     self.objs.append(object.Object(pos=(random.randint(0, self.dim[0]), random.randint(0, self.dim[1])), vel=(random.randint(-5, 5), random.randint(-5, 5)), acc=(0, -4), char=random.choice(string.ascii_letters)))

    def loop(self):
        while self.running:
            time_initial = time.time()

            self.counter += 1
            if self.counter > 1:
                for obj in self.objs:
                    obj.update(self.time_grain, self.dim)
            self.r.render()
            self.r.update(self.objs)


            # for i in self.objs:
            #     print(round(i.x, 2), round(i.y, 2))
            #     print(round(i.vx, 2), round(i.vy, 2))

            difference = time.time() - time_initial
            sleep_time = (1 / self.framerate) - difference
            if sleep_time < 0:
                sleep_time = 0
            time.sleep(sleep_time)

    def load_text(self, text, offset=(0,0)):
        x = offset[0]
        y = offset[1]
        for c in text:
            if c == "\n":
                y -= 1
                x = offset[0]
            else:
                x += 1
                self.objs.append(object.Object(pos=(x, y), vel=(0, 0), acc=(0, -3), char=c))


class Renderer:
    def __init__(self, dim, trails=False):
        self.dim = dim
        self.grid = []
        self.clear()
        self.text = ""
        self.trails = trails

    def render(self):
        os.system("clear")
        self.text = ""
        self.text += "=" * (self.dim[0] + 2) + "\n"
        for x in self.grid:
            self.text += "|"
            for y in x:
                self.text += y
            self.text += "|" + "\n"
        self.text += "=" * (self.dim[0] + 2) + "\n"
        print(self.text)

    def update(self, objs):
        if not self.trails:
            self.clear()
        for obj in objs:
            if 0 <= obj.x < self.dim[0] and 0 <= obj.y <= self.dim[1]:
                self.grid[self.dim[1] - 1 - int(obj.y)][int(obj.x)] = obj.char

    def clear(self):
        self.grid = []
        for y in range(self.dim[1]):
            self.grid.append([])
            for x in range(self.dim[0]):
                self.grid[y].append(" ")


main = Main()
main.loop()
