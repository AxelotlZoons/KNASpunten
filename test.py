# Hardcoded dictionary with single numbers and ranges as keys
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
    range(65, 96): 200,
    range(97, 129): 250
}

def ranking_to_base_points(num):
    # Iterate through the dictionary and check if the number matches a single key or is in any range
    for key, points in points_dict.items():
        if isinstance(key, range):  # If the key is a range
            if num in key:
                return points
        elif num == key:  # If the key is a single number
            return points
    return None  # Return None if no matching key is found

# Test the function
print(ranking_to_base_points(5))
