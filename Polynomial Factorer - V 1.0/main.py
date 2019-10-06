from methods import extract_terms, find_other_roots, test_roots, extract_degree, extract_coefficients, \
    check_terms_present, find_possible_roots, display_roots
from classes import equation

Equation = equation()
Equation.expression += input("Enter a Polynomial Expression > ").lower()
temp_terms = extract_terms(Equation.expression)
print(temp_terms)
Equation.degree = extract_degree(temp_terms)
print(Equation.degree)
Equation.terms = check_terms_present(temp_terms, Equation.degree)
print(Equation.terms)
Equation.coefficients = extract_coefficients(Equation.terms, Equation.degree)
print(Equation.coefficients)
Equation.possible_roots = find_possible_roots(Equation.coefficients)
print(Equation.possible_roots)
temp_root = test_roots(Equation.possible_roots, Equation.coefficients, Equation.degree)
print(temp_root)
Equation.possible_roots.remove(temp_root)
Equation.roots = find_other_roots(Equation.possible_roots, Equation.coefficients, Equation.degree, temp_root)
print("P(x) = " + Equation.expression)
print(display_roots(Equation.roots))
