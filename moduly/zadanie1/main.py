# najpierw prawym guzikiem na zadanie1 i wybieramy: Mark Directory as -> Sources Root
# domyslnie jest sys.path, mozna sprawdzic w terminalu:
# for x in sys.path:
#     print x
# zeby uruchomic z terminala bedac w folderze moduly to: python zadanie1\main.py

from mathematica.geometry import figures
from mathematica.algebra import matrices

# figures.square_area()
# matrices.add_matrices()

a = [[1, 2], [10, 10]]
b = [[2, 3], [5, 6]]
c = matrices.add_matrices(a, b)
print(c)
d=matrices.sub_matrices(b, a)
print(d)