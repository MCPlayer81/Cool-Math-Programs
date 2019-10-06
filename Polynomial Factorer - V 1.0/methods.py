import math


def quadratic_equation(coefficients):
    """Perform the Quadratic Equation to find the two Roots"""

    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]

    x = ((-1 * b) + (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    y = ((-1 * b) - (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    roots = [x, y]
    return roots


def extract_terms(equation):
    """Extract the individual terms from the expression"""

    equation = equation.replace("+", " ")
    equation = equation.replace("-", " -")
    terms = equation.split(" ")

    return terms


def check_terms_present(terms, degree):
    temp = 0
    while degree >= 0:
        if degree == 0:
            try:
                t = terms[temp]
            except IndexError:
                terms.insert(temp, "0")

        if degree == 1:
            if "x" not in terms[temp]:
                terms.insert(temp, "0x")

        if degree > 1:
            if "x^%d" % degree not in terms[temp]:
                terms.insert(temp, "0x^%d" % degree)
        degree -= 1
        temp += 1

    return terms


def extract_degree(terms):
    """Extract the degree from the highest term"""

    leading_term = terms[0]
    degree = 0

    for i in range(0, len(leading_term)):

        if leading_term[i] == "^":
            degree = int(leading_term[i + 1:])

        if leading_term[-1] == "x":
            degree = 1

    return degree


def extract_coefficients(terms, degree):
    """Extract the Coefficients from the Terms"""

    coefficients = []

    for i in range(0, len(terms)):
        if i == len(terms) - 1:
            coefficients.append(int(terms[i]))

        elif i == len(terms) - 2:
            if terms[i].replace("x", "") == "-":
                coefficients.append(-1)
            elif terms[i].replace("x", "") == "":
                coefficients.append(1)
            else:
                coefficients.append(int(terms[i].replace("x", "")))

        else:
            temp = "x^%d" % (degree - i)

            if terms[i].replace(temp, "") == "":
                coefficients.append(1)
            else:
                coefficients.append(int(terms[i].replace(temp, "")))

    return coefficients


def calc_remainder(coefficients, degree, x):
    products = []
    sum = 0

    for i in range(0, len(coefficients)):
        products.append(int(coefficients[i]) * (x ** (degree - i)))

    for i in products:
        sum += i

    return sum


def find_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
            factors.append(-i)

    return factors


def find_possible_roots(coefficients):
    if coefficients[0] != 1:
        factors_a = find_factors(coefficients[0])
        factors_b = find_factors(abs(coefficients[-1]))
        possible_roots = []

        if len(factors_a) > len(factors_b):
            for i in range(0, len(factors_a)):
                for j in range(0, len(factors_a)):
                    possible_roots.append(factors_b[i] / factors_a[j])

        elif len(factors_b) > len(factors_a):
            for i in range(0, len(factors_b)):
                for j in range(0, len(factors_a)):
                    possible_roots.append(factors_b[i] / factors_a[j])

        possible_roots = remove_duplicates(possible_roots)
        return possible_roots

    else:
        possible_roots = find_factors(abs(coefficients[-1]))
        return possible_roots


def remove_duplicates(x):
    return list(dict.fromkeys(x))


def test_roots(possible_roots, coefficients, degree):
    for i in range(0, len(possible_roots) - 1):
        temp = calc_remainder(coefficients, degree, possible_roots[i])
        if temp == 0:
            return possible_roots[i]


def find_other_roots(possible_roots, coefficients, degree, root):
    temp_degree = degree
    roots = [root]

    while temp_degree > 2:
        new_coefficients = []
        for i in range(0, len(coefficients) - 1):
            if i == 0:
                new_coefficients.append(coefficients[i])

            else:
                new_coefficients.append(coefficients[i] + (new_coefficients[i - 1] * roots[-1]))

        temp_degree -= 1
        coefficients = new_coefficients

        if temp_degree != 2:
            roots.append(test_roots(possible_roots, new_coefficients, temp_degree))
            possible_roots.remove(roots[-1])

    temp = quadratic_equation(coefficients)

    if temp[0].is_integer():
        roots.append(int(temp[0]))

    if temp[1].is_integer():
        roots.append(int(temp[1]))

    return roots


def display_roots(roots):
    formatted_roots = []

    for i in range(0, len(roots)):
        if roots[i] > 0:
            formatted_roots.append("(x")
            formatted_roots[0 + i] += str(int(-roots[i]))
            formatted_roots[0 + i] += ")"
        elif roots[i] < 0:
            formatted_roots.append("(x+")
            formatted_roots[0 + i] += str(int(-roots[i]))
            formatted_roots[0 + i] += ")"
        elif roots[i] == 0:
            formatted_roots.append("x")

    display = "P(x) = "

    for j in range(0, len(formatted_roots)):
        display += formatted_roots[j]

    return display
