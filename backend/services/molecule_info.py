from fastapi import HTTPException

from data.elements import elements

def get_composition(formula):
    if formula:
        composition = [{}]
        current_element = ""
        amount_str = ""


        def add_element(element, amount):
            if amount == "":
                amount_int = 1
            else:
                amount_int = int(amount)

            if element not in composition[-1]:
                composition[-1][element] = amount_int
            
            else:
                composition[-1][element] += amount_int
         
        
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                if current_element != "":
                    if current_element in elements:
                        add_element(current_element, amount_str)
                        current_element = ""
                        amount_str = ""
                    else:
                        raise HTTPException(status_code=400, detail= f"Invalid element: {current_element}")

                composition.append({})

                i += 1
                
                continue
            
            elif formula[i] == ")":
                if current_element != "":
                    if current_element in elements:
                        add_element(current_element, amount_str)
                        current_element = ""
                        amount_str = ""
                    else:
                        raise HTTPException(status_code=400, detail= f"Invalid element: {current_element}")

                combo = composition.pop()

                i += 1
                multiplier_str = ""
                while i < len(formula) and formula[i].isdigit():
                    multiplier_str += formula[i]
                    i += 1

                multiplier =  int(multiplier_str) if multiplier_str else 1
                for element, amount in combo.items():
                    amount = str(int(amount) * multiplier)
                    add_element(element, amount)


                continue
            elif formula[i].isupper():
                if current_element != "":
                    if current_element in elements:
                        add_element(current_element, amount_str)
                        amount_str = ""
                    else:
                        raise HTTPException(status_code=400, detail= f"Invalid element: {current_element}")
                current_element = formula[i]
                i += 1

                continue
            elif formula[i].islower():
                
                current_element += formula[i]
                i += 1

                continue
            elif formula[i].isdigit():
                
                if current_element != "":
                    amount_str += formula[i]
                else:
                    raise HTTPException(status_code = 400, detail="Invalid formula: Digit before any element")
                
                i += 1

                continue

            else:
                raise HTTPException(status_code=400, detail= f"Invalid character: {formula[i]}")
        
    

        if current_element != "":
            add_element(current_element, amount_str)
            amount_str = ""

        return composition[0]
    
    else:
        raise HTTPException(status_code=422, detail= "No formula provided")

def get_molar_mass(composition):
    total_mass = 0.0

    for element, amount in  composition.items():

        total_mass += elements[element] * amount

    return total_mass

def get_mass_percent(total_mass, composition):
    mass_fractions = {}
    for element, ammount in composition.items():
        element_mass = elements[element] * ammount
        fraction = element_mass / total_mass
        mass_fractions[element] = fraction
    
    return mass_fractions


def convert_mass_mole(molar_mass, value, mode):

    if mode == "to_mol":
        return value / molar_mass
    
    elif mode == "to_mass":
        return value * molar_mass
