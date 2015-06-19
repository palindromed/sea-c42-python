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

