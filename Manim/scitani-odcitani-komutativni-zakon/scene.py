from manim import *

class komutativnizakon(Scene):
    def construct(self):
        text = MarkupText(f'3+5<span fgcolor="{038C65}">=</span> <span fgcolor="{#F20505}">8</span>', color=#F2EBDF)
        self.play(Write(text))



 
        # framebox1 = SurroundingRectangle(text[1], buff = .1)
        # framebox2 = SurroundingRectangle(text[3], buff = .1)
        # self.play(
            # Create(framebox1),
        # )
        # self.wait()
        # self.play(
            # ReplacementTransform(framebox1,framebox2),
        # )
        # self.wait()