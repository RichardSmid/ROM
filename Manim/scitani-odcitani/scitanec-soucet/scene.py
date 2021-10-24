from manim import *

class operation(Scene):
    def construct(self):
        operation = MarkupText(f'2 + 4 = <span fgcolor="#F20505">6</span>', color="#F2EBDF", font_size=90).shift(UP * .45)
        description = MarkupText(f'addend    addend   <span fgcolor="#F20505">sum</span>', color="#F2EBDF", font_size=40).shift(DOWN * .45)

        self.add(operation)     
        self.add(description)     
