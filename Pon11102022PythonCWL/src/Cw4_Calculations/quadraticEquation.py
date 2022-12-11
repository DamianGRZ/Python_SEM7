import math

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        x1 = x2 = -b / (2 * a)
        im = math.sqrt(-discriminant) / (2 * a)
        return {x1, -im}, {x2, im}


def main():
    print(quadratic_equation(1, -10, 25))
    print(quadratic_equation(1, -3, 4))

if __name__ == "__main__":
    main()
