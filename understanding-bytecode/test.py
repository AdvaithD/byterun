import dis


def cond():
    x = 3
    if x < 5:
        return 'yes'
    else:
        return 'no'


def loops():
    x = 100
    while(x > 0):
        return 'yes'
    else:
        return 'no'


dis.dis(loops)
