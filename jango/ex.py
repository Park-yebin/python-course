def plus(a, b, *args):  # a,b-position argument/ keyword argument는 a==dkdkd 이런 거 이때는 **kwargs추가
    print(args)
    return a+b


plus(1, 2, 1, 2, 1, 2)


def argu(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return a+b


argu(2, 3, 4, 5,  6,  6, net=True)


def sum(*args):
    result = 0
    for num in args:
        result += num
    return result


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
