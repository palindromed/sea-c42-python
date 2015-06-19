def fibonacci(n):
    '''return the nth value of the fibonacci sequence'''
    if (n > 1):
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        if (n < 0):
            return None
        elif (n == 0):
            return 0
        elif (n == 1):
            return 1

def fibonacci1(n):
    num1, num2 = 0, 1
    for num in range(n):
        num1, num2 = num2, num1 + num2
    return num1


def lucas(n):
    '''return the nth Lucas value'''
    if (n > 1):
        return lucas(n - 1) + lucas(n - 2)
    else:
        if (n < 0):
            return None
        elif (n == 0):
            return 2
        elif (n == 1):
            return 1

def lucas1(n):
    num1, num2 = 2, 1
    for num in range(n):
        num1, num2 = num2, num1 + num2
    return num1


def sum_series(n, n0=0, n1=1):
    if (n > 1):
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)
    else:
        if (n < 0):
            return None
        if (n == 0):
            return n0
        elif (n == 1):
            return n1


