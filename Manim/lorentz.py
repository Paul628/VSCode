from manim import *
import math

class grid(Scene):
    def construct(self):
        
        line = Line(start=([-4, -4, 0]), 
                    end=([4, 4, 0]),
                    color=YELLOW
                    )
       
        line2 = Line(start=([-4, 4, 0]), 
                     end=([4, -4, 0]),
                     color=RED
                     )
        
        plane = NumberPlane(
            x_range=(-5,5,1),
            y_range=(-5,5,1)
        )
        lfunc = plane.plot(lambda x: x, color = WHITE)
        lfunc2 = plane.plot(lambda x: x+2, color = WHITE)

        equation = MathTex(r"y=x")
        equation2 = MathTex(r"y=x+2")

        equation.to_corner(UL)
        equation2.to_edge(UL)

        plane.add_coordinates()
        self.add(plane)
        #self.add(line)
        #self.add(line2)
        self.add(equation)


        self.play(
            Write(lfunc),
           run_time = 3,
            
        )
        self.wait(duration=2)

        self.play(
             Transform(lfunc,lfunc2),
             Transform(equation,equation2),
             run_time = 3,
        )

        self.wait(duration=5)