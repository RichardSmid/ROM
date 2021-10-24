from typing import Text
from manim import *

class komutativnizakon(Scene):
    def construct(self):
        first = MarkupText(f'3+5=<span fgcolor="#F20505">8</span>', color="#F2EBDF")
        second = MarkupText(f'5+3=<span fgcolor="#F20505">8</span>', color="#F2EBDF")

        self.play(Write(first))
        self.play(Transform(first, second))
