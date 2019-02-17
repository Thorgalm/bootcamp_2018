# import sys
# print(sys.path) #lista sciezek, w ktorych szuka importow, jak dodamy mark directory as -> source root to doda tą sciezke w pycharm, ale jak uruchamiamy e terminalu to ma tylko te podstawowe sciezki

from A import dodaj as dodaj_liczby
from B import dodaj as dodaj_napisy

print(dodaj_liczby(3, 4))
