import math


def F1_formula(sum_x, m, k):

    f1 = math.sqrt(sum_x/(m*(m+1)/k))*550

    return f1


def F2_formula(n, c):

    f2 = math.sqrt((n/c))*300

    return f2


def F3_formula(p):

    f3 = ((p ** 2 + 5)/54*150)

    return f3


def P1_formula(f1, f2, f3):

    p1 = (f1 + f2 + f3)/10

    return p1


def P_formula(sum_x, n , p):

    f1 = F1_formula(sum_x, m=403, k=2)
    f2 = F2_formula(n, c=112)
    f3 = F3_formula(p)

    P1 = P1_formula(f1, f2, f3)
    P = round(P1)

    return P