from mathematica.geometry import figures
from mathematica.algebra import matrices

def test_square_area():
    figures.square_area(5) == 25

def test_triangle_area():
    figures.triangle_area(a=10, h=2) == 10