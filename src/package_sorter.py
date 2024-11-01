def sort(width, height, length, mass):
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("Dimensions and mass must be positive numbers.")
    
    volume = width * height * length
    
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
