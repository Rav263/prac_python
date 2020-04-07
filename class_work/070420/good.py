"""module writed by RAV to prac"""
import math
import sys


def main():
    """square roots finding"""
    coof_a, coof_b, coof_c = (float(x) for x in sys.argv[1:])

    discr = coof_b**2 - 4 * coof_a * coof_c
    now = math.sqrt(discr)

    y_1 = (-coof_b + now) / (2 * coof_a)
    y_2 = (-coof_b - now) / (2 * coof_a)

    roots = list()

    if y_1 > 0:
        roots.append(math.sqrt(y_1))
        roots.append(-math.sqrt(y_1))
    elif y_1 == 0:
        roots.append(0.)

    if y_2 > 0:
        roots.append(math.sqrt(y_2))
        roots.append(-math.sqrt(y_2))
    elif y_2 == 0:
        roots.append(0.)

    print(*roots)


if __name__ == "__main__":
    main()
