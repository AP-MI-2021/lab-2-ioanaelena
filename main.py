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
    assert get_perfect_squares(100, 170) == [100, 121, 144, 169]
    assert get_perfect_squares(10,30) == [16,25]

#Problema 5
def is_palindrome(n):
    cop=n
    pal=0
    while n!=0 :
        c=n%10
        pal=pal * 10 + c
        n=n//10
    if pal == cop :
        return True
    else
        return False

def test_is_palindrome() :
    assert is_palindrome(232) is True
    assert is_palindrome(25) is False



if __name__ == '__main__':
    test_get_leap_years()
    test_get_perfect_squares()
    test_is_palindrome()