from fractions import Fraction

from fastapi import HTTPException

from services.equation_info import equation_to_dicts

from services.molecule_info import get_composition




def compounds_to_elements(compound_dict: dict):
    compound_list = []
    for compound in compound_dict:
        composition = get_composition(compound)
        compound_list.append(composition)


    return compound_list

def get_common_divisor(number, remainder):
    while remainder:
        number, remainder = remainder, number % remainder

    return number

def least_common_denominator(a, b):
    return a * b // get_common_divisor(a, b)




def create_matrix(all_elements, reactants, products):
    matrix = []
    for element in all_elements:
        row = []
        for reactant in reactants:
            count = 0
            if reactant.get(element,0):
                count = abs(reactant[element])

            row.append(count)
        
        for product in products:
            count = 0
            if product.get(element,0):
                count = -abs(product[element])

            row.append(count)

        matrix.append(row)

    return matrix


def solve_matrix(matrix):
    if not matrix or not matrix[0]:
        raise HTTPException(
            status_code = 422,
            detail = "Matrix missing"
        )


    column = 0
    anchor_row = 0


    for row in matrix:
        for i in range(len(row)):
            row[i] = Fraction(row[i])


    while anchor_row < len(matrix) and column < len(matrix[0]):

        pivot_row = None
        for k in range(anchor_row, len(matrix)):
            if matrix[k][column] != 0:
                pivot_row = k
        
        if pivot_row == None:
            column += 1
            continue

        matrix[anchor_row], matrix[pivot_row] = matrix[pivot_row], matrix[anchor_row]

        anchor_num = matrix[anchor_row][column]
        
        if anchor_num == 0:
            raise HTTPException(
                status_code = 422,
                detail = "Matrix mathematically invalid"
            )

        l = 0
        while l < len(matrix[anchor_row]):
            matrix[anchor_row][l] /= anchor_num
            l += 1

        l = 0
        while l < len(matrix):
            if l == anchor_row:
                l += 1
                continue

            mult_num = matrix[l][column]

            curr_column = 0
            while curr_column < len(matrix[anchor_row]):
                matrix[l][curr_column] -= matrix[anchor_row][curr_column] * mult_num
                curr_column += 1

            l += 1

        column += 1
        anchor_row += 1

    solution = [Fraction(0)] * len(matrix[0])

    pivot_columns = []

    for row in matrix:
        for j in range(len(matrix[0])):
            if row[j] != 0:
                pivot_columns.append(j) 
                break

    free_columns = []
    for j in range(len(matrix[0])):
        if j not in pivot_columns:
            free_columns.append(j)




    for j in free_columns:
        solution[j] = Fraction(1)
    
    for row in matrix:
        pivot = None

        for i in range(len(row)):
            if row[i] != 0:
                pivot = i
                break

        if pivot != None:
            sum_free = Fraction(0)
            for j in free_columns:
                sum_free += row[j] * solution[j]

            solution[pivot] = -sum_free

    denominators = []
    for i in range(len(solution)):
        denominators.append(solution[i].denominator)


    common_denominator = 1
    for denominator in denominators:
        common_denominator = least_common_denominator(common_denominator, denominator)

    for i in range(len(solution)):
        solution[i] *= common_denominator
        solution[i] = int(solution[i])

    return solution


    


def make_balanced_equation(coefficients, reactants, products):
    number = 0
    balanced_equation = ""
    for reactant in reactants:
        coefficient = str(int(coefficients[number]))
        if coefficient != "1":
            balanced_equation += coefficient
        balanced_equation += reactant
        if number < (len(reactants) -1):
            balanced_equation += " + "

        number += 1

    balanced_equation += " -> "


    for product in products:
        coefficient = str(int(coefficients[number]))
        if coefficient != "1":
            balanced_equation += coefficient
        balanced_equation += product
        if number < (len(reactants) + len(products) -1):
            balanced_equation += " + "
        
        number += 1

    return balanced_equation



def balance_equation(equation: str):
    reactants_full, products_full = equation_to_dicts(equation)

    reactants = compounds_to_elements(reactants_full)
    products = compounds_to_elements(products_full)

    reactants_elements = set()
    for reactant in reactants:
        for element in reactant:
            reactants_elements.add(element)

    products_elements = set()
    for product in products:
        for element in product:
            products_elements.add(element)

    if reactants_elements != products_elements:
        raise HTTPException(
            status_code = 422,
            detail = "Unmatched elements on sides of equation"
        )


    compounds = reactants + products
    all_elements = set()

    for compound in compounds:
        for element in compound:
            all_elements.add(element)

    matrix = create_matrix(all_elements, reactants, products)

    coefficients = solve_matrix(matrix)

    compound_amount = len(reactants) + len(products)

    if len(coefficients) != compound_amount:
        raise HTTPException(
            status_code = 422,
            detail = "Unable to get coefficients for all compounds"
        )

    balanced_equation = make_balanced_equation(coefficients, reactants_full, products_full)


    return balanced_equation, coefficients