def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    tl = matrix[0][0]
    br = matrix[-1][-1]
    bl = matrix[-1][0]
    tr = matrix[0][-1]

    tlbr_sum = tl + br
    bltr_sum = bl + tr
    total = tlbr_sum + bltr_sum
    print(total)
    

m1 = [
    [1,   2],
    [30, 40],
]
sum_up_diagonals(m1)
        

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
sum_up_diagonals(m2)