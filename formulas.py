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


def percentage_formula(sum_x, n , p):

    f1 = F1_formula(sum_x, m=403, k=2)
    f2 = F2_formula(n, c=112)
    f3 = F3_formula(p)

    P1 = P1_formula(f1, f2, f3)
    percentage = round(P1)

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
    range(9, 12): 700,
    range(13, 16): 600,
    range(17, 24): 500,
    range(25, 32): 400,
    range(33, 48): 350,
    range(49, 64): 300,
    range(65, 96): 250,
    range(97, 129): 200
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
    print(F"base points: ", base_points)
    
    points = int(base_points) * int(percentage)/100
    print(F"points: ", points)

    print(comp_type)

    # Jeugdschermer, die punten haalt op een wedstrijd van 33% of meer in een hogere leeftijdscategorie dan zijn eigen categorie, wordt het behaalde aantal punten met 1,1 vermenigvuldigd voor zijn eigen ranglijst.
    
    # Punten behaald op WB-wedstrijden worden met een factor 2 vermenigvuldigd. Punten behaald op ECC-wedstrijden worden met een factor 2 vermenigvuldigd.	
    if comp_type == 'WB' or comp_type == 'ECC':
        points = 2*points

    # Punten behaald op wedstrijden met een percentage van 50% of meer (met uitzondering van het NK en WB-wedstrijden) voor senioren en junioren ranglijsten worden met een factor 2 vermenigvuldigd.	
    if percentage > 50 and comp_type not in ['NK', 'WB']:
        print('gggijobbu')
        points = 2*points

    # Punten behaald op wedstrijden met een percentage van 30% of meer (met uitzondering van het NK, ECC-wedstrijden en WB-wedstrijden) voor cadetten ranglijsten worden met een factor 2 vermenigvuldigd.	
    
    # Punten behaald op keurmerk-wedstrijden worden met een factor 1,1 vermenigvuldigd.	
    # points = points * 1.1
    # Punten behaald op keurmerk-wedstrijden met 2 voorronden en A en B-poules of poule unique worden met een factor 1,05 vermenigvuldigd.

    return points