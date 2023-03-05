from manim import *

max_x = config.frame_width / 2
max_y = config.frame_height / 2

class Hello(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        x = max_x
        y = max_y
        while y >= -max_y:
            line = Line(np.array([-x, y, 0]), np.array([x, y, 0]))
            if y in [max_y, -max_y]:
                line.set_stroke(color=BLUE, width=1, opacity=1)
            else:
                line.set_stroke(color=BLUE, width=1, opacity=0.25)
            self.add(line)
            y = y - max_y/16
        y = max_y
        x = max_x
        while x > -max_x:
            line = Line(np.array([x, -y, 0]), np.array([x, y, 0]))
            if x in [max_x, -max_x]:
                line.set_stroke(color=BLUE, width=1, opacity=1)
            else:
                line.set_stroke(color=BLUE, width=1, opacity=0.25)
            self.add(line)
            x = x - max_x/16
        line = Line(np.array([-max_x, -y, 0]), np.array([-max_x, y, 0]))
        line.set_stroke(color=BLUE, width=1, opacity=1)
        self.add(line)
        self.wait(12 * 60 * 60)
