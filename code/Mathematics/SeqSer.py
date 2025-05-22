from manim import *
 #manim. 

        # Let *** denote index
        # Let b*** denote boxes or surrounding shapes
        # Let h*** denote heading
        # Let s*** denote sentences
        # Let m*** denote mathematical expressions

class ZenosDichotomy(Scene):
    def construct(self):
        total_length = 10  
        origin = LEFT * total_length / 2

        full_line = Line(start=origin, end=origin + RIGHT * total_length, color=WHITE)
        self.play(Create(full_line))

        # Label the full length as 1
        one_label = Tex("1").next_to(full_line.get_end(), DOWN)
        self.play(Write(one_label))

        # Draw subdivisions
        current_x = origin
        length = total_length
        terms = 6  # Number of subdivisions to show
        labels = []

        for i in range(1, terms + 1):
            length /= 2
            next_x = current_x + LEFT * length
            arc = ArcBetweenPoints(current_x, next_x, angle=-PI/2, color=BLUE)
            label = Tex(f"1/{2**i}").scale(0.6).next_to(arc, UP, buff=0.1)
            labels.append(label)

            # Show arc and label
            self.play(Create(arc), Write(label), run_time= 2)
            current_x = next_x

        self.wait(2)

class Motivation(Scene):
    def construct(self):
        ImPath= "C:/Users/Lord Eagle/Documents/GitHub/Grade_12-Visual/images"
               
        Logo = ImageMobject(f"{ImPath}\\Logo.png")
        self.play(FadeIn(Logo));self.wait()
        self.play(Logo.animate.scale(0.1).to_corner(DR));self.wait(2)
        head = Tex("Sequence and Series").to_edge(UR,buff = 0.5).set_color_by_gradient(PINK,BLUE)       
        h1 = Tex("Sequence"); h2 = Tex("Series")
        hh1 = Tex("SEQUENCE").to_edge(UL,buff = 1).set_color(PINK); hh2 = Tex("SERIES").to_edge(UR,buff = 1).set_color(BLUE)   

        self.play(Write(head))       
        self.play(head.animate.scale(0.5).to_edge(UL),run_time = 2)
        self.wait(2)
        History = Tex("HISTORY").to_edge(UP,buff = 1).set_color(BLUE);self.play(Write(History)); self.wait(1)
        Zeno = ImageMobject(f"{ImPath}\\ZenoVanElea.jpg").scale(1.5)
        self.play(FadeIn(Zeno));self.wait(2)
        Motivation = Tex("APPLICATIONS").to_edge(UP,buff = 1).set_color(BLUE)
        self.play(FadeOut(Zeno),Transform(History, Motivation));self.wait()
        Im1 = ImageMobject(f"{ImPath}\\Satellite.jpg").scale(1.5)
        Im2 = ImageMobject(f"{ImPath}\\Heat-wave.jpg").scale(1.5)
        Im3 = ImageMobject(f"{ImPath}\\MeerKATDeep2Composite.jpg").scale(1.5)
        Im4 = ImageMobject(f"{ImPath}\\DEEP2heatCropped.jpg").scale(1.5)
        self.play(FadeIn(Im1)); self.wait()
        self.play(Transform(Im1,Im2)); self.wait()
        self.play(Transform(Im1,Im3)); self.wait()
        self.play(Transform(Im1,Im4)); self.wait()
        self.play(Im1.animate.rotate(2*PI),run_time = 2); self.wait()




class Katieum(Scene):
    def construct(self):
        ImPath= "C:/Users/Lord Eagle/Documents/GitHub/Grade_12-Visual/images"
               
        # MOTIVATION 
        Logo = ImageMobject(f"{ImPath}\\Logo.png")
        self.play(FadeIn(Logo));self.wait()
        self.play(Logo.animate.scale(0.1).to_corner(DR));self.wait(2)
        head = Tex("Sequence and Series").to_edge(UR,buff = 0.5).set_color_by_gradient(PINK,BLUE)       
        h1 = Tex("Sequence"); h2 = Tex("Series")
        hh1 = Tex("SEQUENCE").to_edge(UL,buff = 1).set_color(PINK); hh2 = Tex("SERIES").to_edge(UR,buff = 1).set_color(BLUE)   

        self.play(Write(head))       
        self.play(head.animate.scale(0.5).to_edge(UL),run_time = 2)
        self.wait(2)
        History = Tex("History").to_edge(UP,buff = 1).set_color(BLUE);self.play(Write(History)); self.wait(1)
        Zeno = ImageMobject(f"{ImPath}\\ZenoVanElea.png")


        self.play(Write(h1)); self.wait() 
        self.play(Transform(h1,h2)); self.wait(2)    
        self.play(ReplacementTransform(h1,hh1))
        self.wait(2)
        # 1.1 SEQUENCE
        s1 = Tex("a list of ORDERED numbers separated by a comma").set_color(BLUE)
        m1 = MathTex("3,6,9,12,...,3k").to_edge(UP,buff = 2)
        m_1 = MathTex("T_1 = 3"); m_2 = MathTex("T_2 = 6"); m_3 = MathTex("T_3 = 9"); m_n = MathTex("T_n = 3k")
        m2 = MathTex("T_1,T_2,T_3,T_4,...,T_n").to_edge(DOWN,buff = 2)
        
        self.play(Write(s1),run_time = 2); self.wait(2)
        self.play(FadeOut(s1)); self.wait()
        self.play(Write(m1),run_time = 3); self.wait(2)


        self.play(Write(m_1)); self.wait(2)
        self.play(Transform(m_1,m_2)); self.wait(2)
        self.play(Transform(m_1,m_3)); self.wait(3)
        self.play(Transform(m_1,m_n)); self.wait(2)
        self.play(FadeOut(m_1)); self.wait()
        self.play(Write(m2),run_time = 3); self.wait(2)
        self.play(FadeOut(m1),FadeOut(m2)); self.wait()

        # 1.2 SERIES
        self.play(ReplacementTransform(hh1,hh2))
        self.wait(2)

        s2 = Tex("the sum of individual terms separated by an operator").set_color(PINK)
        m3 = MathTex("3+6+9+12+...+3k").to_edge(UP,buff = 2)
        m_1 = MathTex("S_1 = 3"); m_2 = MathTex("S_2 = 3 + 6"); m_3 = MathTex("S_3= 3 + 6 + 9")
        mm1 = MathTex("S_1 = T_1").next_to(m_1); mm2 = MathTex("S_2 = T_1 + T_2").next_to(m_2); mm3 = MathTex("S_3 = T_1 + T_2 + T_3").next_to(m_3)
        m4 = MathTex("\sum_{n=1}^\infty S_k = T_1+T_2+T_3+T_4+...+T_k").to_edge(DOWN,buff = 2)
        self.play(Write(s2),run_time = 3); self.wait(2)
        self.play(FadeOut(s2)); self.wait()
        self.play(Create(m3),run_time = 3); self.wait(2)
        # self.play(Create(m4),run_time = 4)
        # self.wait()
        # h3 = Tex("Arithmetic Sequence").to_edge(UL,buff = 1)
        # self.play(h2.animate.to_edge(UL,buff = 1),Transform(h2,h3),FadeOut(h2),FadeOut(m3),FadeOut(m4))
        # self.wait(2)
        



        

