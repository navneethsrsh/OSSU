import math

def polysum(n, s):
    """
    Sum the area and square of the perimeter for a regular polygon
    
    Formula:
    ----------------------------------------
    area + (perimeter ** 2)
    
    Parameters:
    -----------------------------------------
    n -> int:
        Represents number of sides of regular polygon
        
    s -> int/float:
        Represents the length of each side 
    
    Return Value:
    -----------------------------------------
    For valid parameters:
        A single value of type float calculated as defined in
        the "Formula" section, rounded to 4 decimal places
        
    Else:
        0(zero)
    
    """

    if not poly_valid(sides=n, length=s):
        return 0

    result =  area(sides=n, length=s) + (perimeter(sides=n, length=s) ** 2)   
    return round(result, 4)


def poly_valid(sides, length):
    """
    Checks if the parameter provided can produce a valid polygon
    
    Parameters:
    ----------------------------------------
    sides -> int:
        Represents number of sides of regular polygon
        
    length -> int/float:
        Represents the length of each side 
    
    Return Value:
    ----------------------------------------
    A boolean value
    
    Criterion:
    ----------------------------------------
    > The number of sides provided must be at least  3
    > The provided length must be at least 0.0001
    
    """
    
    margin = 0.0001
    if sides < 3 or abs(length - 0) <= margin:
        return False
    else:
        return True
    
    
def area(sides=3, length=1):
    """
    Calculate the area of a regular polygon

    Formula:
    ----------------------------------------
    (0.25 * sides * (length ** 2))/tan(pi/n)

    Parameters:
    ----------------------------------------
    sides -> int:
        Represents number of sides of regular polygon
        
    length -> int/float:
        Represents the length of each side

    Return Value:
    ----------------------------------------
    An int/float value calculated as defined in the
    "Formula" section.

    Variables:
    ----------------------------------------
    rad -> float: Angle in radians
    num -> float: Numerator in formula
    den -> float: Denominator in formula

    """

    if not poly_valid(sides, length):
        return 0
    
    rad = math.pi/sides
    num = (0.25 * sides * (length ** 2))
    den = math.tan(rad)
    return num/den


def perimeter(sides=3, length=1):
    """
    Calculate the perimeter of a regular polygon

    Formula:
    ----------------------------------------
    sides * length

    Parameters:
    ----------------------------------------
    sides -> int:
        Represents number of sides of regular polygon
        
    length -> int/float:
        Represents the length of each side

    Return Value:
    ----------------------------------------
    An int/float value calculated as defined in the
    "Formula" section.

    """

    if not poly_valid(sides, length):
        return 0
    
    return sides * length
