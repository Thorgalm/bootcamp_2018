# def add_matrices(m1, m2):
#     # np. m1 = [[1,1],[2,3]]
#     m3 = []
#     for i in range(len(m1)):  # idzie po indeksach
#         row = []
#         for j in range(len(m1[i])):
#             row.append(m1[i][j] + m2[i][j])
#         m3.append(row)
#     return m3
#
#
# def sub_matrices(m1, m2):
#     m3 = []
#     for i in range(len(m1)):  # idzie po indeksach
#         row = []
#         for j in range(len(m1[i])):
#             row.append(m1[i][j] - m2[i][j])
#         m3.append(row)
#     return m3

# wg zasady do not repeat yourself piszemy jedna ogolna funkcje

def add_matrices(m1, m2):
    return _add_or_sub_matrices(m1, m2)


def sub_matrices(m1, m2):
    return _add_or_sub_matrices(m1, m2, sign=-1)


def _add_or_sub_matrices(m1, m2, sign=1):
    """If add then sign = 1 if sub the sing = -1"""
    # np. m1 = [[1,1],[2,3]]
    m3 = []
    for i in range(len(m1)):  # idzie po indeksach
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + sign * m2[i][j])
        m3.append(row)
    return m3
