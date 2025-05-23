from manim import *

class ZenosDichotomy(Scene):
    def construct(self):
        total_length = 10  
        origin = LEFT * total_length / 2

        full_line = Line(start=origin, end=origin + RIGHT * total_length, color=WHITE)
        self.play(Create(full_line))

        # Label the full length as 1
        one_label = Tex("1").next_to(full_line.get_end(), DOWN)
        self.play(Write(one_label))

        # Draw subdivisions (arcs above the line from right to left)
        start_point = origin + RIGHT * total_length  # Start at the right end (labeled "1")
        length = total_length
        terms = 6  # Number of subdivisions to show
        arcs = []
        labels = []

        current_x = start_point
        for i in range(1, terms + 1):
            length /= 2
            next_x = current_x + LEFT * length
            arc = ArcBetweenPoints(current_x, next_x, angle=PI/2, color=BLUE)
            label = Tex(f"1/{2**i}").scale(0.6).next_to(arc, UP, buff=0.1)
            arcs.append(arc)
            labels.append(label)

            # Show arc and label
            self.play(Create(arc), Write(label), run_time=2)
            current_x = next_x

        self.wait(2)
        geom = Tex(f"$$...;\\left(\\frac{1}{2}\\right)^n;...;\\frac{1}{8};\\frac{1}{4};\\frac{1}{2};1 $$").to_edge(DOWN,buff = 1)
        self.play(Write(geom));self.wait(2)

        Geom = Tex(f"$$ 1; \\frac{1}{2};\\frac{1}{4};\\frac{1}{8};...;\\left(\\frac{1}{2}\\right)^n;... $$")
        self.play(
            FadeOut(full_line),
            FadeOut(one_label),
            *[FadeOut(arc) for arc in arcs],
            *[FadeOut(label) for label in labels],
        )
        self.play(Transform(geom,Geom))

        self.play(geom.animate.to_edge(ORIGIN))

        