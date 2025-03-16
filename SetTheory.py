from manim import *
# manim. 

class Sets(Scene):
    def construct(self):
        # Let *** denote index
        # Let b*** denote boxes or surrounding shapes
        # Let h*** denote heading
        # Let s*** denote sentences
        # Let m*** denote mathematical expressions

        head1 = Tex("Set Theory").to_edge(UL,buff = 0.5)                     
        self.play(Write(head1))       
        self.play(head1.animate.scale(0.5).to_edge(UR),run_time = 2)
        self.wait(2)
        s1 = Tex("What is a SET")
        self.play(Write(s1))
        self.wait()
        self.play(FadeOut(s1))
        h1 = Tex("SET")
        self.play(h1.animate.to_edge(UL,buff = 1))