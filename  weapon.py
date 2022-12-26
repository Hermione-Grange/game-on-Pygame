from tools import *


class Arrow:
    def __init__(self, display, start, end, speed, gravity):
        self.display = display
        self.gravity = gravity
        self.x = start[0]
        self.y = start[1]
        targetx = end[0]
        targety = end[1]
        angle = math.atan2(targety - self.y, targetx - self.x)
        degrees = round(to_deg(angle))