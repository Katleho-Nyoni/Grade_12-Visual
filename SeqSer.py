from manim import *
 #manim. 

class Test(Scene):
    def construct(self):
        # Let *** denote index
        # Let b*** denote boxes or surrounding shapes
        # Let h*** denote heading
        # Let s*** denote sentences
        # Let m*** denote mathematical expressions

        head1 = Tex("Sequence and Series").to_edge(UL,buff = 0.5)       
        h1 = Tex("Sequence")
        h2 = Tex("Series")
        b1 = SurroundingRectangle(h1,color = BLUE,buff = 2).scale(0.4)
        self.play(Write(head1))       
        self.play(head1.animate.scale(0.5).to_edge(UR),run_time = 2)
        self.wait(2)
        self.play(Create(VGroup(h1,b1)))
        self.wait()
        self.play(Transform(h1,h2))
        self.wait()        
        self.play(FadeOut(b1),FadeOut(h1))
        # 1.1 SEQUENCE
        h1 = Tex("SEQUENCE")
        self.play(Write(h1))
        self.play(h1.animate.to_edge(UL,buff = 1))
        self.wait(2)
        s1 = Tex("a list of ordered numbers separated by a comma")
            # b3 = SurroundingRectangle(s1,color = BLUE,buff = 0.5)
        m1 = MathTex("3,6,9,12,...,3n")
        # More Variables
        s_1 = Tex("Where").to_edge(DL,buff = 3)
        s_2 = Tex("is the").to_edge(ORIGIN,buff = 3)
        s_3 = Tex("denoted").to_edge(DR,buff = 3)
        m_1 = MathTex("3")
        m_2 = MathTex("6")
        m_3 = MathTex("9")
        m_4 = MathTex("12")
        m_n = MathTex("3n")
        mm_1 = MathTex("T_1")       
        mm_2 = MathTex("T_2")       
        mm_3 = MathTex("T_3")       
        mm_4 = MathTex("T_4")       
        mm_n = MathTex("T_n")       
        mm_n1 = MathTex("T_n = 3n")       
        m2 = MathTex("T_1,T_2,T_3,T_4,...,T_n").to_edge(DOWN,buff = 2)
        self.play(Write(s1),run_time = 4)
        self.play(FadeOut(s1))
        self.wait()
        self.play(Write(m1),run_time = 3)
        # self.play(Write(s_1))
        self.play(Create(m2),run_time = 4)
        self.wait()
        # 1.2 SERIES
        h2 = Tex("SERIES").to_edge(UR,buff = 1)
        self.play(h1.animate.to_edge(UR,buff = 1))
        self.play(Transform(h1,h2),FadeOut(m1),FadeOut(m2))
        self.wait()
        s2 = Tex("the sum of individual terms separated by an operator")
        m3 = MathTex("3+6+9+12+...+3n")
        m4 = MathTex("\sum_{n=1}^\infty S_k = T_1+T_2+T_3+T_4+...+T_k").to_edge(DOWN,buff = 2)
        self.play(Write(s2),run_time = 3)
            # self.play(Create(b3))       
        self.play(FadeOut(s2))
        self.wait()
        self.play(Write(m3),run_time = 3)
        self.play(Create(m4),run_time = 4)
        self.wait()
        h3 = Tex("Arithmetic Sequence").to_edge(UL,buff = 1)
        self.play(h2.animate.to_edge(UL,buff = 1),Transform(h2,h3),FadeOut(h2),FadeOut(m3),FadeOut(m4))
        self.wait(2)
        x = Tex("Fucked!")
        self.play(Write(x),run_time = 2)
        self.wait(3)



        

