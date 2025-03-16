from manim import *

class Pit(Scene): # line 3 & 4 are always included
    def construct(self):

        sq = Square(side_length = 5,stroke_color = GREEN,fill_color = BLUE,fill_opacity = 0.75)
        self.play(Create(sq),run_time = 3)
        self.wait() # to run the file manim ManimCourse.py Pit -pqm

class Test(Scene): # line 3 & 4 are always included
    def construct(self):
        name = Tex("Testing").to_edge(UL,buff = 0.5)
        sq = Square(side_length = 4,fill_color = RED,fill_opacity = 0.7).shift(LEFT*2)
        tri = Triangle().scale(1.4).to_edge(DR)
        self.play(Write(name))
        self.play(DrawBorderThenFill(sq),run_time =2)
        self.play(Create(tri))
        self.wait()
        self.play(name.animate.to_edge(UR),run_time = 2)
        self.play(sq.animate.scale(0.5).center(),tri.animate.to_edge(DL),run_time = 2)

class Getters(Scene):
    def construct(self):
        c = Circle(radius = 2).to_edge(DOWN)
        s = Square(side_length = 2).to_edge(UP)
        arrow = Line(start = s.get_bottom(),end = c.get_top()).add_tip()
        self.play(Create(VGroup(s,c,arrow)))
        self.wait()

class Updaters(Scene):
    def construct(self):
        
        nm = MathTex("ln(2)")

        bx = always_redraw(lambda : SurroundingRectangle(nm,color = BLUE,fill_opacity = 0.4,fill_color = RED,buff = 2))
        
        name = always_redraw(lambda: Tex("Logarithm").next_to(bx,DOWN,buff = 0.25))

        self.play(Create(VGroup(nm,bx,name)))
        self.play(nm.animate.shift(RIGHT*2),run_time = 2)
        self.wait()

class ValTracker(Scene):
    def construct(self):

        k = ValTracker(5)
        num = always_redraw(lambda : DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(0),run_time = 5,rate_func = linear)

class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-4,4,2],x_length = 7,y_range = [0,16,4],y_length = 8).to_edge(DOWN)
        parab = plane.get_graph(lambda x : x**2,x_range=[-4,4],color = GREEN)

        self.play(DrawBorderThenFill(plane))
        self.play(Create(parab))
        self.wait()
    

        




































