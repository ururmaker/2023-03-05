import math
from manimlib import *
from pypinyin import lazy_pinyin, Style

class Hello(Scene):
    def construct(self):
        rect = Rectangle(
            width=FRAME_WIDTH,
            height=4,
            fill_color="#CC5266",
            fill_opacity=1,
            stroke_width=0
        )
        rect.shift(2 * UP)
        self.add(rect)
        rect = Rectangle(
            width=FRAME_WIDTH,
            height=4,
            fill_color="#3971BF",
            fill_opacity=1,
            stroke_width=0
        )
        rect.shift(2 * DOWN)
        self.add(rect)
        line = Line(LEFT, RIGHT)
        line.set_width(FRAME_WIDTH)
        line.set_stroke(BLACK, 2)
        self.add(line)
        image_a = ImageMobject("Avatars\\1455555019_users-9_icon-icons.com_53249.png")
        image_a.set_height(2.5)
        image_a.shift(2.3 * UP).to_edge(LEFT, buff=0)
        self.add(image_a)
        image_b = ImageMobject("Avatars\\1455555016_users-15_icon-icons.com_53267.png")
        image_b.set_height(2.5)
        image_b.shift(1.8 * DOWN).to_edge(RIGHT, buff=0)
        self.add(image_b)
        self.wait(2)

        zh = "国挪"
        en = "Hello!"
        zh_texts = VGroup()
        for c in zh:
            if c in "，。：；“”‘’？！":
                zh_text = Text(c, font="Noto Sans SC Medium", font_size=60)
                square = Square(side_length=0.75, stroke_width=1)
                if c in "，。":
                    zh_text.shift(0.175 * DL)
                zh_text = VGroup(square, zh_text)
            else:
                zh_text = Text(c, font="Noto Sans SC Medium", font_size=60)
                square = Square(side_length=0.75, stroke_width=1, stroke_color=WHITE)
                square.set_stroke(opacity=1)
                zh_text = VGroup(square, zh_text)
                pinyin = lazy_pinyin(c, style=Style.TONE)[0]
                py_text = Text(pinyin, font="FZYiHeiS", font_size=20, color=YELLOW)
                py_text.next_to(zh_text, UP, buff=0)
                if "g" in pinyin:
                    a = Text(pinyin, font="FZYiHeiS", font_size=20, color=YELLOW)
                    b = Text(pinyin.replace("g", ""), font="FZYiHeiS", font_size=20, color=YELLOW)
                    down_num = a.get_top()[1] - b.get_top()[1]
                    down_num = 0.024
                    py_text.shift(down_num * DOWN)
                    print(down_num)
                print(pinyin)
                print(py_text.get_top())
                zh_text = VGroup(py_text, zh_text)
            zh_texts.add(zh_text)
        zh_texts.arrange_in_grid(math.ceil(len(zh_texts) / 12), 12, aligned_edge=DOWN, buff=0)
        en_text = Text("What is your problem?", font="Sitka Small", font_size=30, color="#DDDDDD")
        text = VGroup(zh_texts, en_text)
        text.arrange(DOWN, aligned_edge=LEFT)
        text.shift(2 * UP)
        text.next_to(image_a, RIGHT)
        self.play(FadeIn(zh_texts), run_time=2)
        self.play(Write(en_text), run_time=3)
        self.wait()
        
