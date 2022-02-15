def isprime(x):
    '''
    :param x:nr intreg
    :return: returneaza daca x este prim sau nu
    '''
    d = 0
    i = 0
    if x == 1:
        return False
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            d = d + 1
    if d == 1:
        return True
    else:
        return False


def get_goldbach(n):
    '''
    :param n:nr intreg
    :return:returneaza p1 si p2 daca se verifica conditia sau anunta imposibilitatea unei solutii
    '''
    if n % 2 == 1:
        p1 = 2
        p2 = n - 2
        if isprime(p2) == 1:
            return p1, p2
    else:
        ok = 0
        for i in range(1, n // 2 + 1, 2):
            p1 = i
            p2 = n - p1
            if isprime(p1) and isprime(p2) and p1 + p2 == n:
                return p1, p2


def test_get_goldbach():
    '''
    Functie de testare
    :return:
    '''
    assert get_goldbach(0) == None
    assert get_goldbach(4) == None
    assert get_goldbach(89098) == (11, 89087)
    assert get_goldbach(8) == (3, 5)
    assert get_goldbach(11) == None
    assert get_goldbach(2131991) == None
    assert get_goldbach(1231) == (2, 1229)
    assert get_goldbach(6) == (3, 3)
    print("Programul ruleaza corespunzator")


def get_newton_sqrt(n, steps):
    '''
    :param n: nr intreg
    :param steps: nr intreg
    :return: aproximarea radicalului lui n in steps pasi
    '''
    x = 2
    for i in range(0, steps):
        x = x / 2 + n / (2 * x)
    return x


def test_get_newton_sqrt():
    '''
    :return: comentariu in cazul in care ruleaza corespunzator
    '''
    assert get_newton_sqrt(15, 10) == 3.872983346207417
    assert get_newton_sqrt(4, 10) == 2
    assert get_newton_sqrt(10, 5) == 3.162277660168379
    assert get_newton_sqrt(9, 1) == 3.25
    assert get_newton_sqrt(9, 2) == 3.0096153846153846
    print("Functia de testare ruleaza corespunzator!")


def is_palindrome(n):
    '''
    :param n: nr intreg
    :return: true daca este palindrom , false in caz contrar
    '''
    x = n
    inv = 0
    while x != 0:
        inv = inv * 10 + x % 10
        x = x // 10

    if inv == n:
        return True
    else:
        return False


def test_is_palindrome():
    '''

    :return: Fucntia de testare ruleaza corespunzator
    '''
    assert is_palindrome(1) == True
    assert is_palindrome(121) == True
    assert is_palindrome(515151) == False
    assert is_palindrome(19) == False
    assert is_palindrome(999) == True
    assert is_palindrome(1114111) == True
    print("Functia de testare ruleaza corespunzator!")


def main():
    '''
    Functia de consola
    :return:
    '''
    shouldRun = True
    while shouldRun:
        print("1.Conjectura lui GoldBach")
        print("2.Calculul radicalului folosind metoda de aproximare a lui Newton")
        print("3.Determinarea daca un numar este palindrom")
        print("x.Iesire")
        option = input("Alege problema:")
        if option == "1":
            print("1.Functia de calcul a primei probleme")
            print("2.Functia de testare a primei probleme")
            option2 = input("Alegeti intre functia de calcul si functia de testare:")
            if option2 == "1":
                n = int(input("Introduceti numarul dorit spre verificare:"))
                print(get_goldbach(n))
            elif option2 == "2":
                test_get_goldbach()
            else:
                print("Optiunea aleasa nu exista, mai incercati!")
        elif option == "2":
            print("1.Functia de aproximare a problemei doi")
            print("2.Functia de testare a problemei doi")
            option2 = input("Alegeti intre functia de calcul si functia de testare:")
            if option2 == "1":
                n = int(input("Dati un numar:"))
                steps = int(input("Alegeti un numar de pasi:"))
                print(get_newton_sqrt(n, steps))
            elif option2 == "2":
                test_get_newton_sqrt()
        elif option == "3":
            print("1.Functia de aproximare a problemei trei")
            print("2.Functia de verificare a problemei trei")
            option2 = input("Alegeti intre functia de verificare si functia de testare:")
            if option2 == "1":
                n = int(input("Alegeti numarul dorit spre verificare:"))
                print(is_palindrome(n))
            elif option2 == "2":
                test_is_palindrome()
            else:
                print("Optiunea aleasa nu exista, mai incercati!")
        elif option == "x":
            shouldRun = False
        else:
            print("Optiunea aleasa nu exista, incercati inca o data!")


main()

'''Pentru problema 1 N are solutie pentru orice numar par mai mare decat 2 '''
