from fastapi import HTTPException

        

def equation_to_dicts(equation:str):
    equation = equation.replace(" ", "")

    reactants = {}

    products = {}

    reactants_side, products_side = equation.split("->")


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

            elif char.isalpha():
                current_compound += char

                i+=1

            elif char == "+":
                if current_compound != "":

                    dictionary[current_compound] = int(current_coefficient) if current_coefficient else 1

                    current_compound = ""
                    current_coefficient = ""

                    i += 1
                    continue

                else:
                    raise HTTPException (status_code=422, detail="'+' Before any compound")
                
            else:
                raise HTTPException(status_code= 400, detail= f"Invalid character: {char}")
            
        if current_compound:
            dictionary[current_compound] = int(current_coefficient) if current_coefficient else 1
        
        return dictionary
    


    reactants = add_side_to_dict(reactants_side, reactants)
    products = add_side_to_dict(products_side, products)

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

        theo_yield = reac_mol * ratio

        theoretical_yields[product] = theo_yield

    return theoretical_yields
