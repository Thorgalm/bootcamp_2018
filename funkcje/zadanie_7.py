"""jak sie napisze test i ustawi kursow na funckji wcisnie alt+enter to sam doda szkielet funkcji"""
""" doct string jak na poczatku funkcji wstawimy 3 x " i enter to automatycznie wstawi paramentry funkcji, które teraz mozemy opisac, ta dokumentacja pojawi sie jak wpiszemy help(przytnij)"""

def przytnij(data, start, stop):
    """

    :param data: list
    :param start: function
    :param stop: funkction
    :return: list
    """
    out = []
    for element in data:
        if start(element):
            out.append(element)
            if stop(element):
                break
    return out

#print(przytnij(list(range(1000)), start=lambda x: x>100, stop=lambda x%11 ==0))
def test_przytnij():
    assert przytnij(data=[1, 2, 3, 4, 5, 6, 7], start=lambda x: x > 3, stop=lambda x: x == 6) == [4, 5, 6]
