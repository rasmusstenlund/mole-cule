from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services.molecule_info import get_composition, get_molar_mass, convert_mass_mole, get_elements_data

from services.equation_info import equation_to_dicts, get_limiting_ratios, get_limiting_reactant, get_theoretical_yields, get_excess_remnants

from services.validation import validate_equation, validate_quantity_dict, validate_compound_str

from services.balance import balance_equation

app = FastAPI(title="Mole-Cule API", description = "This is the API used for the tool Mole-Cule.")

class LimitingFactor(BaseModel):
    equation: str
    reactants_mol: dict



@app.get("/")
def Home():
    return {"message": "Welcome to Mole-Cule API!"}

@app.get("/analyze")
def analyze(formula: str):
    validate_compound_str(formula)
    composition = get_composition(formula)

    elements_data = get_elements_data(composition)

    molar_mass = get_molar_mass(composition) 
    
    return {
        "formula": formula,
        "molar_mass":molar_mass,
        "elements_data": elements_data,
        "note": "Percentages may not add up to exactly 100% due to rounding"
    }

@app.get("/balance")
def balance(equation:str):
    validate_equation(equation)

    balanced_equation, coefficients = balance_equation(equation)

    return {
        "entered_equation": equation,
        "data": {
            "balanced_equation":balanced_equation,
            "coefficients": coefficients
        }
    }
 
@app.get("/convert")
def convert(formula: str, mass: float = None, mol: float = None):

    validate_compound_str(formula)

    composition = get_composition(formula)

    molar_mass = get_molar_mass(composition)
    


    if mass and formula and not mol:
        mol = convert_mass_mole(molar_mass, mass, "to_mol")

        mol = round(mol, 3)

        return {
            "mol": mol
        }
    
    elif mol and formula and not mass:
        mass = convert_mass_mole(molar_mass, mol, "to_mass")

        mass = round(mass, 3)

        return {
            "mass": mass
        }

    else:
        raise HTTPException(status_code = 422, detail = "Provide formula and either mass or mol")
    

@app.post("/limiting")
def limiting(data: LimitingFactor):

    equation = data.equation
    reactants_mol = data.reactants_mol

    validate_equation(equation)
    validate_quantity_dict(reactants_mol)

    reactants, products = equation_to_dicts(equation)

    limiting_ratios = get_limiting_ratios(reactants, reactants_mol)

    limiting_reactant = get_limiting_reactant(limiting_ratios)

    theoretical_yields = get_theoretical_yields(limiting_reactant, reactants, products, reactants_mol)

    for compound, theo_yield in theoretical_yields.items():

        theoretical_yields[compound] = theo_yield

    excess_remnants = get_excess_remnants(limiting_reactant, reactants, reactants_mol)

    return {
        "limiting_reactant": limiting_reactant,
        "theoretical_yields": theoretical_yields,
        "excess_remnants": excess_remnants
        
    }



    