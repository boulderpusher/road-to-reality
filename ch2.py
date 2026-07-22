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

# Figure 2.2 - 2.5
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
        big_square = Square(1).shift(UP * 0.5)
        small_square = Square(0.5).shift(UP * 1.25 + RIGHT * 0.25)
        tilted_square = Square(1.25**0.5, color="green") \
            .shift((UP + RIGHT) * (1.25**0.5 - 1)/2) \
            .rotate(np.arctan(0.5), about_point=(LEFT + DOWN) * 0.5)
        tilted_square.shift(UP * 0.5)
        self.add(big_square, small_square, tilted_square)
        self.play(AnimationGroup(FadeOut(*squares), FadeOut(*lines)))
        pts = tilted_square.get_vertices()
        upper_triangle = Polygon(pts[0], pts[1], [pts[0][0], pts[1][1], 0],
                                stroke_width=0)
        left_triangle = Polygon(pts[1], pts[2], [pts[2][0], pts[1][1],0],
                                stroke_width=0)
        upper_triangle.set_fill("red", opacity=0.8)
        left_triangle.set_fill("blue", opacity=0.8)
        middle = Union(
            Intersection(big_square, tilted_square),
            Intersection(small_square, tilted_square)
        )
        middle.set_fill("green", opacity=0.8)
        middle.stroke_width = 0
        self.play(AnimationGroup(FadeIn(upper_triangle), FadeIn(left_triangle), FadeIn(middle)))
        self.play(AnimationGroup(
            upper_triangle.animate.shift(DOWN + RIGHT * 0.5),
            left_triangle.animate.shift(RIGHT + UP * 0.5)
        ))
        self.pause(1)
        self.play(FadeOut(upper_triangle, left_triangle, middle))
        lower_right = np.array([pts[3][0], pts[2][1], 0])
        c = Line(pts[2], pts[3], color="purple", stroke_width=8)
        a = Line(pts[2], lower_right, color="red", stroke_width=8)
        b = Line(lower_right, pts[3], color="blue", stroke_width=8)
        self.play(AnimationGroup(Create(a), Create(b), Create(c)))

class Squares(Scene):
    def construct(self):
        l = 0.5
        squares = [[Square(l)]]
        for r in range(1, int(9/l)):
            edge_squares = []
            for i in range(r):
                edge_squares.append(Square(l).shift(RIGHT*i*l + UP*(r-i)*l))
                edge_squares.append(Square(l).shift(RIGHT*(r-i)*l + DOWN*i*l))
                edge_squares.append(Square(l).shift(LEFT*i*l + DOWN*(r-i)*l))
                edge_squares.append(Square(l).shift(LEFT*(r-i)*l + UP*i*l))
            squares.append(edge_squares)
        self.play(AnimationGroup([FadeIn(*edge_squares)
                                  for edge_squares in squares],
                                  lag_ratio=0.1,
                                  run_time=3))
