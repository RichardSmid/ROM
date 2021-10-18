from manim import *

class komutativnizakon(Scene):
    def construct(self):
        text = MarkupText(f'3+5<span fgcolor="#038C65">=</span> <span fgcolor="#F20505">8</span>', color=#F2EBDF)
        self.play(Write(text))

