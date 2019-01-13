# isinstance(lista,list)
def splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element, list):
            for el in splaszcz(element):
                out.append(el)
        else:
            out.append(element)

    return out


# rozwiązanie bez ostatniego testu, tylko dla 1 zagniezdzenia
# def splaszcz(lista):
#     out=[]
#     for element in lista:
#         if isinstance(element, list):
#             for el in element:
#                 out.append(el)
#         else:
#             out.append(element)
#
#     return out


def test_splaszcz_pusta_lista():
    assert splaszcz([]) == []


def test_splaszcz_plaska_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]


def test_splaszcz_zagniezdzona_lista():
    assert splaszcz([1, 2, 3, [4, 5, [6], 7]]) == [1, 2, 3, 4, 5, 6, 7]


# moje
"""
def splaszcz(lista):
    for i in lista:
        if isinstance(i,list) == False:
            a = list(lista)
        
    return a

print(splaszcz([1, 2, 3]))

print(splaszcz([1, 2, 3,[4]]))


def test_splaszcz_pusta_lista():
    assert splaszcz([]) == []


def test_splaszcz_plaska_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

# def test_splaszcz_zagniezdzona_lista():
#     assert splaszcz([1,2,3,[4,5,[6],7]])==[1,2,3,4,5,6,7]
"""
