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

# Figure 2.6
class Lattice(Scene):
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
        self.play(AnimationGroup([FadeOut(*edge_squares)
                                  for edge_squares in squares[::-1]],
                                  lag_ratio=0.1,
                                  run_time=3))

# Figure 2.7
class SquareConstruction(Scene):
    def construct(self):
        base_line = Line(LEFT + DOWN, RIGHT + DOWN)
        self.play(FadeIn(base_line))

        left_line = base_line.copy()
        right_line = base_line.copy()

        bottom_left = base_line.get_start()
        bottom_right = base_line.get_end()
        
        self.play(
            Rotate(left_line, PI/2, about_point=bottom_left),
            Rotate(right_line, -PI/2, about_point=bottom_right)
        )

        self.play(
            Create(RightAngle(left_line, base_line, length=0.2)),
            Create(RightAngle(right_line, base_line, quadrant=(-1,-1), length=0.2))
        )

        top_left = left_line.get_end()
        top_right = right_line.get_start()
        left_half = Line(top_left, midpoint(top_left, top_right), color="red")
        right_half = Line(top_right, midpoint(top_left, top_right), color="red")

        self.play(
            Create(left_half),
            Create(right_half)
        )

        self.play(
            Create(Angle(left_half, left_line, color="red", quadrant=(1,-1), other_angle=True, radius=0.2)),
            Create(Angle(right_half, right_line, color="red", radius=0.2))
        )

# Figure 2.8
class ParallelPostulate(Scene):
    def construct(self):
        m_a = -1/6
        m_b = 1/18
        a = Line(LEFT * 3 + UP/2, ORIGIN)
        b = Line(LEFT * 3 + DOWN/2, DOWN * 1/3)
        c = Line(LEFT * 2.5 + UP, LEFT * 2 + DOWN, color="blue")

        self.play(Create(a), Create(b))
        self.play(Create(c))
        angle_a = Angle(a, c, other_angle=True, radius=0.2, color="blue")
        angle_b = Angle(b, c, quadrant=(1, -1), radius=0.2, color="blue")
        self.play(
            Create(angle_a), 
            Create(angle_b)
        )

        a_ext = DashedLine(a.get_end(), a.get_end() + RIGHT * 3 + UP * m_a * 3, color="green")
        b_ext = DashedLine(b.get_end(), b.get_end() + RIGHT * 3 + UP * m_b * 3, color="green")
        self.play(Create(a_ext), Create(b_ext))
        b_over = Line(b_ext.get_start(), b_ext.get_end())
        self.play(Create(b_over), *map(FadeOut, [a, c, angle_a, angle_b, a_ext]))
        l = Line(b.get_start(), b_over.get_end())
        self.add(l)
        self.remove(b)
        self.remove(b_ext)
        p = Circle(radius=0.05, color="red", fill_color="red").shift(l.get_midpoint() + UP / 2)
        p.set_fill(RED, opacity=1)
        self.play(Create(p))
        parallel = l.copy()
        parallel.set_color("green")
        self.play(parallel.animate.shift(UP / 2))
        
