import math
from knas_worldranking import knas_worldranking


def F1_formula(sum_x, m, k):

    print(f"sum_x: {sum_x}")
    print(f"m: {m}")
    print(f"k: {k}")

    f1 = math.sqrt(sum_x/(m*(m+1)/k))*550

    return f1


def F2_formula(n, c):

    print(f"n: {n}")
    print(f"c: {c}")
    f2 = math.sqrt((n/c))*300

    return f2


def F3_formula(p):

    print(f"p: {p}")
    f3 = ((p ** 2 + 5)/54*150)

    return f3


def P1_formula(f1, f2, f3):

    p1 = (f1 + f2 + f3)/10
    print(f"p1: {p1}")

    return p1


def percentage_formula(sum_x, n , p):

    f1 = F1_formula(sum_x, m=len(knas_worldranking), k=2)
    f2 = F2_formula(n, c=112)
    f3 = F3_formula(p)
    print(f"f1: {f1}")
    print(f"f2: {f2}")
    print(f"f3: {f3}")

    P1 = P1_formula(f1, f2, f3)
    percentage = round(P1)
    print(f"percentage: {percentage}%")

    return percentage



def ranking_to_base_points(num):

    final_ranking = int(num)

    points_dict = {
    1: 1000,
    2: 950,
    3: 925,
    4: 900,
    5: 830,
    6: 820,
    7: 810,
    8: 800,
    range(9, 13): 700,
    range(13, 17): 600,
    range(17, 25): 500,
    range(25, 33): 400,
    range(33, 49): 350,
    range(49, 65): 300,
    range(65, 97): 250,
    range(97, 129): 200,
    range(129, 161): 190,
    range(161, 999): 0
    }

    # Iterate through the dictionary and check if the number matches a single key or is in any range
    for key, points in points_dict.items():
        if isinstance(key, range):  # If the key is a range
            if final_ranking in key:
                return points
        elif final_ranking == key:  # If the key is a single number
            return points


def points_formula(percentage, comp_type, final_ranking=1):

    base_points = ranking_to_base_points(final_ranking)

    if base_points == 0:
        points = 0

    else:
        points = int(base_points) * int(percentage)/100

        # Jeugdschermer, die punten haalt op een wedstrijd van 33% of meer in een hogere leeftijdscategorie dan zijn eigen categorie, wordt het behaalde aantal punten met 1,1 vermenigvuldigd voor zijn eigen ranglijst.

        # Punten behaald op WB-wedstrijden worden met een factor 2 vermenigvuldigd. Punten behaald op ECC-wedstrijden worden met een factor 2 vermenigvuldigd.
        if comp_type == 'WB' or comp_type == 'ECC':
            points = 2*points

        # Punten behaald op wedstrijden met een percentage van 50% of meer (met uitzondering van het NK en WB-wedstrijden) voor senioren en junioren ranglijsten worden met een factor 2 vermenigvuldigd.
        if percentage > 50 and comp_type not in ['NK', 'WB']:
            points = 2*points

        # Punten behaald op wedstrijden met een percentage van 30% of meer (met uitzondering van het NK, ECC-wedstrijden en WB-wedstrijden) voor cadetten ranglijsten worden met een factor 2 vermenigvuldigd.

        # Punten behaald op keurmerk-wedstrijden worden met een factor 1,1 vermenigvuldigd.
        # points = points * 1.1 ### gaat blijkbaar om nederlands wedstrijden met een keurmerk

        # Punten behaald op keurmerk-wedstrijden met 2 voorronden en A en B-poules of poule unique worden met een factor 1,05 vermenigvuldigd.

    print(points)
    return round(points)