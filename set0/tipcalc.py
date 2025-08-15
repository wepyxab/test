def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # $50.00 > 50.00 float
    d = float(d[1:])
    return d


def percent_to_float(p):
    # 15% > 0.15
    p = float(p[:-1]) / 100
    return p


main()