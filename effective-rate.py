# Effective Rate
import math


def effectiverate(r, n):  # r = interest rate per year, n = times of compounding per year
    """The effective annual interest rate is the real return on a savings account or any interest-paying
    investment when the effects of compounding over time are taken into account. It also reveals the real 
    percentage rate owed in interest on a loan, a credit card, or any other debt."""

    E = round(((((1 + r / n) ** n) - 1) * 100), 2)
    return E


print(effectiverate(0.062, 365))

print(effectiverate(0.0625, 2))

# Comparing two investment acoounts


def comparing_annual_yield(x, y):
    def effectiverate(r, n):  # r = interest rate per year, n = times of compounding per year
        """The effective annual interest rate is the real return on a savings account or any interest-paying
        investment when the effects of compounding over time are taken into account. It also reveals the real 
        percentage rate owed in interest on a loan, a credit card, or any other debt."""

        E = round(((((1 + r / n) ** n) - 1) * 100), 2)
        return E
    x = effectiverate(r, n)
    y = effectiverate(r, n)
    if x > y:
        print("x investment is better with an annual yield of " + x + "%")
    elif x < y:
        print("y investment is better with an annual yield of " + y + "%")
    else:
        print("there's no difference")


print(comparing_annual_yield((0.062, 365), (.0625, 2)))
