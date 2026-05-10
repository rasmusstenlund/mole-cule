from fastapi import HTTPException

import re

from data.elements import elements_list



def get_composition(formula):
    if formula:
        composition = [{}]


        items = re.findall("[A-Z][a-z]*|\d+|\(|\)", formula)

        unknown = re.sub("[A-Z][a-z]*|\d+|\(|\)", "", formula)
        if unknown != "":
            raise HTTPException(
                status_code = 422,
                detail = f"Unknown characters: {unknown}"
            )
        
        i = 0
        while i < len(items):

            if items[i] == "(":
                composition.append({})

                i +=1
                continue
            elif items[i] == ")":

                if len(composition) == 1:
                    raise HTTPException(
                        status_code = 422,
                        detail = "Too many ')'"
                    )
                
                group = composition.pop()

                multiplier = 1

                if i + 1 < len(items) and items[i + 1].isdigit():
                    multiplier = int(items[i + 1])
                    i += 1
                
                for element, count in group.items():
                    count = int(count)

                    composition[-1][element] = composition[-1].get(element, 0) + (count * multiplier) 

                i += 1
                continue

            elif items[i].isdigit():
                raise HTTPException(
                    status_code = 422,
                    detail = "Number unassigned to group or element"
                )
            

            else:
                element = items[i]

                count = 1

                if i + 1 < len(items) and items[i + 1].isdigit():
                    count = int(items[i + 1])
                    i += 1

                composition[-1][element] = composition[-1].get(element, 0) + count

                i += 1
                continue
        
        if len(composition) != 1:
            raise HTTPException(
                status_code = 422,
                detail = "Unclosed parenthesis"
            )

        return composition[0]
    
    else:
        raise HTTPException(status_code=422, detail= "No formula provided")


def get_molar_mass(composition: dict):
    total_mass = 0.0

    for element, amount in  composition.items():

        total_mass += elements_list[element]["atomic_mass"] * amount

    return total_mass

def get_mass_percent(total_mass, composition):
    mass_fractions = {}
    for element, amount in composition.items():

        element_mass = elements_list[element]["atomic_mass"] * amount

        fraction = element_mass / total_mass
        mass_fractions[element] = fraction
    
    return mass_fractions


def convert_mass_mole(molar_mass, value, mode):

    if mode == "to_mol":
        return value / molar_mass
    
    elif mode == "to_mass":
        return value * molar_mass
