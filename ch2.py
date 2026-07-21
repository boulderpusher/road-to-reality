from manim import *

# Figure 2.1
class PythagoreanTheorem(Scene):
    def construct(self):
        a = np.array([-2, -1, 0])
        b = np.array([2, -1, 0])
        c = np.array([2, 1, 0])

        triangle = Polygon(a, b, c)

        mid_ab = (a + b) / 2
        mid_bc = (b + c) / 2
        mid_ac = (a + c) / 2

        angle_marker = np.array([
            b,
            b + np.array([-0.2, 0, 0]),
            b + np.array([-0.2, 0.2, 0]),
            b + np.array([0, 0.2, 0]),
        ])

        label_ab = MathTex("a").next_to(mid_ab, DOWN, buff=0.2)
        label_bc = MathTex("b").next_to(mid_bc, RIGHT, buff=0.2)
        label_ac = MathTex("c").next_to(mid_ac, UP + LEFT, buff=0.2)

        label_formula = MathTex("a^2 + b^2 = c^2").shift(DOWN * 2.5)

        self.play(Create(triangle))
        self.play(Create(Polygon(*angle_marker)))
        self.play(
            Write(label_ab), Write(label_bc), Write(label_ac)
        )
        self.play(Write(label_formula))

# Figure 2.2 - 2.4
class Tesselation(Scene):
    def construct(self):
        # Figure 2.2
        start_points = [UP + LEFT * 1.5 + (DOWN + RIGHT * 0.5) * i 
                        for i in range(3)]
        centers = [start + (RIGHT + UP * 0.5) * i
                   for start in start_points for i in range(3)]
        squares = [Square(1).shift(center) for center in centers]
        self.play(AnimationGroup([Create(sq) for sq in squares], lag_ratio = 0.1))
        self.wait(0.5)

        # Figure 2.3
        horizontals = [(centers[i * 3], centers[i*3+2]) for i in range(3)]
        verticals = [(centers[i], centers[i+6]) for i in range(3)]
        lines = VGroup(*[Line(*pts, color="green") for pts in horizontals + verticals])
        self.play(LaggedStartMap(Create, lines, lag_ratio=0.1))
        self.wait(0.5)

        # Figure 2.4
        self.play(lines.animate.shift((DOWN + LEFT) * 0.5))

# Figure 2.5
class TiltedSquare(Scene):
    def construct(self):
        big_square = Square(1)
        small_square = Square(0.5).shift(UP * 0.75 + RIGHT * 0.25)
        self.play(AnimationGroup([Create(big_square), Create(small_square)]))
