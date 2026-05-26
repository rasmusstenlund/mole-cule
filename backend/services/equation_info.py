from fastapi import HTTPException

import re       

from services.molecule_info import get_molar_mass, get_composition

def equation_to_dicts(equation:str):
    equation = equation.replace(" ", "")

    reactants = {}
    products = {}

    reactants_side, products_side = equation.split("->")


    def add_side_to_dict(side: str, dictionary: dict):
        compounds = side.split("+")


        for compound in compounds:
            match = re.match("\d+", compound)

            count = 1
            if match:
                count = match.group()
                compound = compound[len(count):]
                count = int(count)

            if compound == "":
                raise HTTPException(    
                    status_code = 422,
                    detail = "Number unassigned to compound"
                )
            
            dictionary[compound] = dictionary.get(compound, 0) + count



    add_side_to_dict(reactants_side, reactants)
    add_side_to_dict(products_side, products)

    return reactants, products
  

    
def get_limiting_ratios(reactants:dict, reactants_mol:dict):

    ratios_dict = {}

    for reactant, coefficient in reactants.items():
        mol = reactants_mol.get(reactant)

        if mol is None:
            raise HTTPException(status_code = 422, detail = f"Missing mol for {reactant}")

        ratio = mol / coefficient

        ratios_dict[reactant] = ratio

    return ratios_dict 




def get_limiting_reactant(ratios_dict: dict):
    min_ratio =  min(ratios_dict.values())

    limiting_reactant = [compound for compound, ratio in ratios_dict.items() if ratio == min_ratio]

    return limiting_reactant[0]



def get_theoretical_yields(limiting_reactant: str, reactants: dict, products: dict, reactants_mol: dict):

    theoretical_yields = {}

    reac_coefficient = reactants[limiting_reactant]
    reac_mol = reactants_mol[limiting_reactant]

    for product, prod_coefficient in products.items():

        ratio = prod_coefficient / reac_coefficient

        yield_mol = reac_mol * ratio

        composition = get_composition(product)

        molar_mass = get_molar_mass(composition)

        yield_mass = yield_mol * molar_mass

        theoretical_yields[product] = {
            "mol": yield_mol,
            "grams": round(yield_mass, 3)
        }



    return theoretical_yields



def get_excess_remnants(limiting_reactant: str, reactants: dict, reactants_mol: dict):
    
    remnants = {}

    limiting_count = reactants[limiting_reactant]

    limiting_mol = reactants_mol[limiting_reactant]

    limiting_ratio = limiting_mol / limiting_count

    for compound, count in reactants.items():
        if compound == limiting_reactant:
            remnants[compound] = {"mol": 0.000, "grams": 0.0}
        else:
            used_mol = limiting_ratio * float(count)
            excess_mol = float(reactants_mol[compound]) - used_mol

            composition = get_composition(compound)

            molar_mass = get_molar_mass(composition)

            excess_mass = excess_mol * molar_mass

            remnants[compound] = {"mol": round(excess_mol, 3), "grams": round(excess_mass, 3)}

    return remnants