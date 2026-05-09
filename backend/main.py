from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services.molecule_info import get_composition, get_molar_mass, get_mass_percent, convert_mass_mole

from services.equation_info import equation_to_dicts, get_limiting_ratios, get_limiting_reactant, get_theoretical_yields

from services.validation import validate_equation_structure, validate_reaction, validate_quantity_dict, validate_compound_str

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

    molar_mass = get_molar_mass(composition)
    mass_percent_float = get_mass_percent(molar_mass, composition)
    
    mass_percent = {}
    for element, value in mass_percent_float.items():
        value = value *100
        value = round(value, 2)
        mass_percent[element] = value

    return {
        "formula": formula,
        "composition": composition,
        "molar_mass": molar_mass,
        "mass_percent": mass_percent
    }

@app.get("/convert")
def convert(formula: str, mass: float = 0.0, mol: float = 0.0):

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

    validate_equation_structure(equation)
    validate_quantity_dict(reactants_mol)

    reactants, products = equation_to_dicts(equation)

    validate_reaction(reactants, products)

    limiting_ratios = get_limiting_ratios(reactants, reactants_mol)

    limiting_reactant = get_limiting_reactant(limiting_ratios)

    theoretical_yields = get_theoretical_yields(limiting_reactant, reactants, products, reactants_mol)

    for compound, theo_yield in theoretical_yields.items():
        theo_yield = round(theo_yield, 3)

        theoretical_yields[compound] = theo_yield

    return {
        "limiting_reactant": limiting_reactant,
        "theoretical_yields": theoretical_yields
    }



    