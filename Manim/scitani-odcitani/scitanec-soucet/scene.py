from manim import *

class operation(Scene):
    def construct(self):
        two = Tex("2 ")
        plus = Tex(" + ").next_to(two,RIGHT ,buff=SMALL_BUFF)
        four = Tex("4").next_to(plus, RIGHT,buff=SMALL_BUFF)
        equal = Tex("=").next_to(four, RIGHT,buff=SMALL_BUFF)
        six = Tex("6").next_to(equal, RIGHT,buff=SMALL_BUFF).set_color(PURE_RED)

        operation = VGroup(two,plus,four,equal,six).scale(3)

        added1 = Tex("sčítanec").next_to(two,DOWN,buff = SMALL_BUFF)
        added2 = Tex("sčítanec").next_to(four,DOWN,buff = SMALL_BUFF)
        sum = Tex("součet").next_to(six,DOWN,buff = SMALL_BUFF).set_color(PURE_RED)

        description = VGroup(added1,added2,sum)

        all = VGroup(description,operation).shift(LEFT * .5)

        self.add(all)