from mathematica.algebra import matrices


def test_add_matrices():
    a = [[1, 2], [10, 10]]
    b = [[2, 3], [5, 6]]
    assert matrices.add_matrices(a, b) == [[3, 5], [15, 16]]

def test_sub_matrices():
    a = [[1, 2], [10, 10]]
    b = [[2, 3], [5, 6]]
    assert matrices.sub_matrices(b, a) == [[1, 1], [-5, -4]]
