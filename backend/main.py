from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services.molecule_info import get_composition, get_molar_mass, get_mass_percent, convert_mass_mole

from services.reaction_info import get_lim_compound

app = FastAPI(title="Mole-Cule API", description = "This is the API used for the tool Mole-Cule.")

class LimitingFactor(BaseModel):
    equation: str
    reactants: dict



@app.get("/")
def Home():
    return {"message": "Welcome to Mole-Cule API!"}

@app.get("/analyze")
def analyze(formula: str):
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
def convert(formula: str = "", mass: float = 0.0, mol: float = 0.0):
    composition = get_composition(formula)
    molar_mass = get_molar_mass(composition)
    
    if mass and formula and not mol:
        mol = convert_mass_mole(molar_mass, mass, "to_mol")

        return {
            "mol": mol
        }
    
    elif mol and formula and not mass:
        mass = convert_mass_mole(molar_mass, mol, "to_mass")

        return {
            "mass": mass
        }

    else:
        raise HTTPException(status_code = 422, detail = "Provide formula and either mass or moles")
    

@app.post("/limiting")
def limiting(data: LimitingFactor):
    equation = data.equation.replace(" ", "")
    reactants = data.reactants
    limiting_reactant = get_lim_compound(equation, reactants)

    return{
        "limiting_reactant": limiting_reactant
    }



    