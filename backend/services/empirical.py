from fastapi import HTTPException

from fractions import Fraction

from data.elements import elements_list

from services.molecule_info import get_molar_mass

def reorder_elements(elements: list):
    temporary_elements = elements
    
    reordered_elements = []

    if "C" in temporary_elements:
        temporary_elements.remove("C")
        reordered_elements.append("C")
        if "H" in temporary_elements:
            temporary_elements.remove("H")
            reordered_elements.append("H")

    temporary_elements.sort()

    for element in temporary_elements:
        reordered_elements.append(element)


    return reordered_elements


def composition_to_formula(composition: dict, elements: list):
    formula = ""
    
    for element in elements:
        formula += element

        amount = str(int(round(composition[element])))

        if amount != "1":
            formula += amount

    return formula



def verify_whole(composition: dict):
    rounding_tolerance = 0.05
    all_whole = True

    for element, mol in composition.items():
        rounded_mol = round(mol)
        distance_whole = abs(mol - rounded_mol)
        
        if distance_whole > rounding_tolerance:
            all_whole = False

    return all_whole



def get_multiplied_composition(composition: dict, molar_mass, empirical_mass):
    formula_units = molar_mass /empirical_mass

    multiplied_composition = {}

    if formula_units < 1:
        raise HTTPException(
            status_code = 422,
            detail = "Invalid molar mass: less than empirical mass"
        )
    
    for element, mol in composition.items():
        multiplied_composition[element] = mol * formula_units

    

    return multiplied_composition



def composition_to_mol(composition: dict):
    moles = []

    elements_mol = {}
    
    for element, mass in composition.items():
        if mass <= 0: 
            raise HTTPException(
                status_code = 422,
                detail = f"Invalid mass for {element}"
            )


        atomic_mass = elements_list[element]["atomic_mass"]

        mol = mass / atomic_mass

        if composition.get(element, 0) == None:
            raise HTTPException(
                status_code = 422,
                detail = ""
            )
        
        elements_mol[element] = mol
        moles.append(mol)
    
    lowest_mol = min(moles)

    for element, mol in elements_mol.items():
        mol = mol / lowest_mol

        elements_mol[element] = mol

    return elements_mol

        

def get_empirical(composition: dict, molar_mass: float = None):
    
    elements = []

    for element, mol in composition.items():
        elements.append(element)

        if elements.count(element) != 1:
            raise HTTPException(
                status_code = 422,
                detail = f"Element entered more than once: {element}"
            )


    reordered_elements = reorder_elements(elements)

    composition = composition_to_mol(composition)
    
    multiplier = 1
    empirical_composition = {}
    status = False

    while status == False:

        for element, mol in composition.items():
            mol *= multiplier
            empirical_composition[element] = mol

        status = verify_whole(empirical_composition)

        if not status:
            multiplier +=  1


    empirical_formula = composition_to_formula(empirical_composition, reordered_elements)

    empirical_molar_mass = get_molar_mass(empirical_composition)

    if molar_mass:
        molecular_composition = get_multiplied_composition(empirical_composition, molar_mass, empirical_molar_mass)
        molecular_formula = composition_to_formula(molecular_composition, reordered_elements)
        molecular_molar_mass = get_molar_mass(molecular_composition)

        return empirical_formula, empirical_molar_mass, molecular_formula, molecular_molar_mass
    
    return empirical_formula, empirical_molar_mass


