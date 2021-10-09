# from manim import *

# class Output(Scene):
#     def construct(self, text):
#         # text = Text(text[0]+ "+" + text[1] + "=" + text[2])
#         text = Text("sdffdsdfsdfsdf")
#         self.add(text)

from manim import *

class SlantsExample(Scene):
    def construct(self):
        a = Text(str(3) + "+" + str(5) + "=" + str(9))
        self.play(Create(a))