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

if __name__ == '__main__':

    #Test accuracy of fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    #Test accuracy of lucas
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    #Test that fibonacci matches sum_series
    for num in range(0, 11):
        assert fibonacci(num) == sum_series(num)

    #Test that lucas matches sum_series
    for num in range(0, 11):
        assert lucas(num) == sum_series(num, 2, 1)
