from manim import *

class HelloWorld(Scene):
    def construct(self):
        circle = Circle(color=WHITE)
        square = Square()
        
        text = Text("Hello")

        text.to_edge(UP)

        
        self.add(square)
        self.play(
            Write(text, run_time=3)
        )

        self.play(
            Transform(text,circle),
            run_time=3,
            rate_func=smooth
        )

        self.add(circle)