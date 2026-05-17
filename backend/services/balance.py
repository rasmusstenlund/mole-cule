from fractions import Fraction

from services.equation_info import equation_to_dicts

from services.molecule_info import get_composition




def compounds_to_elements(compound_dict: dict):
    compound_list = []
    for compound in compound_dict:
        composition = get_composition(compound)
        compound_list.append(composition)


    return compound_list



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
    column = 0
    anchor_row = 0
    while anchor_row < len(matrix) and column < len(matrix[0]):

        pivot_row = None
        for k in range(anchor_row, len(matrix)):
            if matrix[k][column] != 0:
                pivot_row = k
                break
        
        if pivot_row == None:
            column += 1
            continue

        matrix[anchor_row], matrix[pivot_row] = matrix[pivot_row], matrix[anchor_row]

        anchor_num = matrix[anchor_row][column]
            

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

    return matrix    

def get_full_coefficients(coefficients):
        fraction_coefficients = [Fraction(coefficient).limit_denominator(1000) for coefficient in coefficients]
        last_coefficient = 1
        while True:
            test_coefficients = []

            for coefficient in fraction_coefficients:
                test_coefficients.append(coefficient * last_coefficient)

            all_whole = True

            for coefficient in test_coefficients:
                if coefficient.denominator != 1:
                    all_whole = False

            if all_whole:

                final_coefficients = []
                for coefficient in test_coefficients:
                    final_coefficients.append(coefficient.numerator)

                final_coefficients.append(last_coefficient)

                

                return final_coefficients
            
            last_coefficient += 1




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
        if number < (len(products) -1):
            balanced_equation += " + "
        
        number += 1

    return balanced_equation



def balance_equation(equation: str):
    reactants_full, products_full = equation_to_dicts(equation)

    reactants = compounds_to_elements(reactants_full)
    products = compounds_to_elements(products_full)

    compounds = reactants + products
    all_elements = set()

    for compound in compounds:
        for element in compound:
            all_elements.add(element)

    matrix = solve_matrix(create_matrix(all_elements, reactants, products))

    coefficients = []

    for row in matrix:
        if row[-1] != 0:
            coefficients.append(abs(row[-1]))


    coefficients = get_full_coefficients(coefficients)
    
    balanced_equation = make_balanced_equation(coefficients, reactants_full, products_full)

    return balanced_equation