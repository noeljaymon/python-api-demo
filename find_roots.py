import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the roots using the quadratic formula
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    # Return the roots as a tuple
    return (root1, root2)

# Example for 2 different roots as solution
roots = find_roots(2, 10, 8)

# Uncomment below code for example  for only 1 root as solution

# roots = find_roots(1, 4, 4)

print(roots)
