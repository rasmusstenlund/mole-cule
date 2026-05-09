from fastapi import HTTPException

from data.elements import elements_list

from molecule_info import get_composition

def validate_element(element: str):
    if not element:
        raise HTTPException(
            status_code = 422,
            detail = "Element missing"
        )
    if element not in elements_list:
        raise HTTPException(
            status_code = 422, 
            detail = f"Unknown Element: {element}"
            )
     
    if elements_list[element]["atomic_mass"] is None:
        raise HTTPException(
            status_code = 422, 
            detail = f"Atomic mass for {element} missing"
            )
    
    if elements_list[element]["atomic_number"] is None:
        raise HTTPException(
            status_code = 422,
            detail = f"Atomic number for {element} missing"
        )
    

def validate_composition(compound:dict):
    if not compound:
        raise HTTPException(
            status_code = 422,
            detail = "Compound missing"
        )

    for element, count in compound.items():
        validate_element(element)

        if count <= 0:
            raise HTTPException(
                status_code = 422, 
                detail = f"Invalid count for {element}"
                )
        
def validate_compound_str(compound: str):
    if not compound:
        raise HTTPException(
            status_code = 422,
            detail = "Compound missing"
        )


    composition = get_composition(compound)

    validate_composition(composition)


def validate_quantity_dict(compound_dict: dict):

    if not compound_dict:
        raise HTTPException(
            status_code = 422,
            detail = "Compound dictionary missing"
        )



    for compound, count in compound_dict.items():
        validate_compound_str(compound)

        if count <= 0:
            raise HTTPException(
                status_code = 422, 
                detail = f"Invalid count for {compound}"
                )
        

        

def validate_reaction(reactants: dict, products:dict):
    if not reactants or not products:
        raise HTTPException(
            status_code = 422,
            detail = "Empty equation"
        )
    
    validate_quantity_dict(reactants)
    validate_quantity_dict(products)


def validate_equation_structure(equation: str):

    arrow_count = equation.count("->")

    if arrow_count != 1:
        raise HTTPException(
            status_code = 422,
            detail = "Arrow count invalid: Use 1 '->'"
        )
    
    reactants, products = equation.split("->")

    if not reactants or not products:
        raise HTTPException(
            status_code = 422,
            detail = "Empty equation"
        )