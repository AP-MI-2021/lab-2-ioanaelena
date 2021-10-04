import math


# Problema 11 :
def get_leap_years(start: int, end: int):
    leap_years = []
    while start <= end:
        if start % 4 == 0:
            if start % 100 != 0:
                leap_years.append(start)
        if start % 400 == 0:
            leap_years.append(start)
        start += 1
    return leap_years


# Functia de test
def test_get_leap_years():
    assert get_leap_years(start=2000, end=2021) == [2000, 2004, 2008, 2012, 2016, 2020]
    assert get_leap_years(start=1800, end=1809) == [1804, 1808]


# Problema 12 :
def get_perfect_squares(start: int, end: int):
    perfect_squares = []
    for i in range(start, end + 1):
        if int(math.sqrt(i)) ** 2 == i:
            perfect_squares.append(i)
    return perfect_squares


def test_get_perfect_squares():
    assert get_perfect_squares(2, 20) == [4, 9, 16]
    assert get_perfect_squares(start=20, end=40) == [25, 36]


if __name__ == '__main__':
    test_get_leap_years()
    test_get_perfect_squares()
