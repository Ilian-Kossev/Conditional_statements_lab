from math import pi

figure_type = input()
if figure_type == "square":
    square_side = float(input())
    square_area = square_side * square_side
    print(f"{square_area:.3f}")
if figure_type == "rectangle":
    rec_side_1 = float(input())
    rec_side_2 = float(input())
    rectangle_area = rec_side_2 * rec_side_1
    print(f"{rectangle_area:.3f}")
if figure_type == "circle":
    radius = float(input())
    circle_area = pi * radius * radius
    print(f"{circle_area:.3f}")
if figure_type == "triangle":
    triangle_side = float(input())
    triangle_h = float(input())
    triangle_area = triangle_side * triangle_h / 2
    print(f"{triangle_area:.3f}")

