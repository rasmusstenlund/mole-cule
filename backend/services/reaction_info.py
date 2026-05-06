from fastapi import HTTPException

from services.molecule_info import get_composition, get_molar_mass   
    
    

def reaction_to_dict(reaction:str):
    reaction = reaction.replace(" ", "")

    reactants = {}

    products = {}

    reactants_side, products_side = reaction.split("->")


    def add_side_to_dict(side: str, dictionary: dict):
        current_compound = ""
        current_coefficient = ""
        i = 0
        while i < len(side):
            char = side[i]
            if char.isdigit():
                if current_compound == "":
                   current_coefficient += char
                else:
                    current_compound += char
                i += 1
                continue
            if char.isalpha():
                current_compound += char
                
    

    add_side_to_dict(reactants_side, reactants)
    add_side_to_dict(products_side, products)

    return reactants, products
  
    
def get_lim_compound(equation: str, reactant_dict: dict):
    reactant_side, product_side = equation.split("->")

    reactants = reactant_side.split("+")

    ratios_dict = {}

    for compound in reactants.items():
        coefficient = ""
        new_compound = ""
        
        i = 0
        while i < len(compound):
            if compound[i].isdigit() and new_compound == "":

                coefficient += compound[i]

                i += 1
                continue
            elif compound[i].isdigit() or compound[i].isalpha():

                new_compound += compound[i]

                i +=1
                continue
            else:
                raise HTTPException(status_code = 400, detail= f"Invalid character: {compound[i]}")
        
        if new_compound == "":
            raise HTTPException(status_code= 400, detail= "No reactant, just coefficient provided")
        
        coefficient = coefficient or "1"
        
        mol = 0
        if reactant_dict[new_compound]:
            mol = reactant_dict[new_compound]

        else:
            raise HTTPException(status_code= 422, detail= f"Ammount (Mol) of {new_compound} not imputted")

        value = int(mol) / int(coefficient)

        ratios_dict[new_compound] = value

    limiting_reactant = min(ratios_dict, ratios_dict.get)
        
    return limiting_reactant

def get_theo_yeild():

    return
