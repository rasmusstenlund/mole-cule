from fastapi.testclient import TestClient

from app.main import app

app.state.testing = True

client = TestClient(app)



#Test the analyze endpoint
def test_analyze_standard():
    response = client.post("/analyze", json = {
        "formula": "H2O" 
    })

    data = response.json()

    assert response.status_code == 200
    assert data["formula"] == "H2O"
    assert "H" in data["elements_data"]
    assert data["elements_data"]["H"]["count"] == 2
    assert "O" in data["elements_data"]
    assert data["elements_data"]["O"]["count"] == 1
    assert len(data["elements_data"]) == 2
    assert data["molar_mass"] == 18.015


def test_analyze_round_brackets():
    response = client.post("/analyze", json = {
        "formula": "Cu(OH)2"
    })
    
    data = response.json()

    assert response.status_code == 200
    assert "Cu" in data["elements_data"]
    assert data["elements_data"]["Cu"]["count"] == 1
    assert "O" in data["elements_data"]
    assert data["elements_data"]["O"]["count"] == 2
    assert "H" in data["elements_data"]
    assert data["elements_data"]["H"]["count"] == 2


def test_analyze_square_brackets():
    response = client.post("/analyze", json = {
        "formula": "Cu[OH]2"
    })
    
    data = response.json()

    assert response.status_code == 200
    assert "Cu" in data["elements_data"]
    assert data["elements_data"]["Cu"]["count"] == 1
    assert "O" in data["elements_data"]
    assert data["elements_data"]["O"]["count"] == 2
    assert "H" in data["elements_data"]
    assert data["elements_data"]["H"]["count"] == 2


def test_analyze_hydrate():
    response = client.post("/analyze", json = {
        "formula": "CuSO4*5H2O"
    })

    data = response.json()

    assert response.status_code == 200
    assert "Cu" in data["elements_data"]
    assert data["elements_data"]["Cu"]["count"] == 1
    assert "S" in data["elements_data"]
    assert data["elements_data"]["S"]["count"] == 1
    assert "O" in data["elements_data"]
    assert data["elements_data"]["O"]["count"] == 9
    assert "H" in data["elements_data"]
    assert data["elements_data"]["H"]["count"] == 10


def test_analyze_invalid_hydrate():
    response = client.post("/analyze", json = {
        "formula": "CuSO4**5H2O"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid use of '*'"}


def test_analyze_empty():
    response = client.post("/analyze", json = {
        "formula": ""
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid input: Must contain formula"}


def test_analyze_space():
    response  = client.post("/analyze", json = {
        "formula": "   H2O    "
    })

    data = response.json()

    assert response.status_code == 200
    assert "H" in data["elements_data"]
    assert data["elements_data"]["H"]["count"] == 2
    assert "O" in data["elements_data"]
    assert data["elements_data"]["O"]["count"] == 1


def test_analyze_invalid_character():
    response = client.post("/analyze", json = {
        "formula": "H$O"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Unknown character(s): '$'"}


def test_analyze_invalid_element():
    response = client.post("/analyze", json = {
        "formula": "XxO"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Unknown Element: 'Xx'"}


def test_analyze_zero():
    response = client.post("/analyze", json = {
        "formula": "H0O"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid count for 'H': Element cannot be 0"}


def test_analyze_mismatched_brackets():
    response = client.post("/analyze", json = {
        "formula": "Fe2(OH]3"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Mismatched brackets: '(' and ']'"}


#Test the balance endpoint 

def test_balance_standard():
    response = client.post("/balance", json = {
        "equation": "H2 + O2 -> H2O"
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["balanced_equation"] == "2H2 + O2 -> 2H2O"
    assert data["data"]["coefficients"]["reactants"] == {"H2": 2, "O2": 1}
    assert data["data"]["coefficients"]["products"] == {"H2O": 2}


def test_balance_balanced():
    response = client.post("/balance", json = {
        "equation": "2H2 + O2 -> 2H2O"
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["balanced_equation"] == "2H2 + O2 -> 2H2O"


def test_balance_state():
    response = client.post("/balance", json = {
        "equation": "H2(g) + O2(g) -> H2O(l)"
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["balanced_equation"] == "2H2(g) + O2(g) -> 2H2O(l)"


def test_balance_unmatched_elements():
    response = client.post("/balance", json = {
        "equation": "Fe + O -> H2O"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid equation: Mismatched elements on sides of equation"}


def test_balance_missing_reactant():
    response = client.post("/balance", json = {
        "equation": "-> H2O"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid structure: Reactant(s) missing"}

def test_balance_missing_product():
    response = client.post("/balance", json = {
        "equation": "H2 + O2 ->"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid structure: Product(s) missing"}


def test_balance_empty_equation():
    response = client.post("/balance", json = {
        "equation": "+ ->"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid structure: Empty equation"}


def test_balance_multiple_arrows():
    response = client.post("/balance", json = {
        "equation": "H2 -> O2 -> H2O"
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid structure: Only use 1 '->'"}


#Test the convert endpoint

def test_convert_mass_to_mol():
    response = client.post("/convert", json = {
        "formula": "H2O",
        "mass": 9.008
    })

    data = response.json()

    assert response.status_code == 200
    assert data["entered_mass"] == 9.008
    assert data["data"]["mol"] == 0.5


def test_convert_mol_to_mass():
    response = client.post("/convert", json = {
        "formula": "H2O",
        "mol": 0.5
    })

    data = response.json()

    assert response.status_code == 200
    assert data["entered_mol"] == 0.5
    assert data["data"]["mass"] == 9.008


def test_convert_missing_formula():
    response = client.post("/convert", json = {
        "mass": 18.015
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid input: Must contain formula"}


def test_convert_missing_input():
    response = client.post("/convert", json = {
        "formula": "H2O"
    })

    assert response.status_code ==  422
    assert response.json() == {"detail": "Invalid input: Must contain either mass or mol"}

def test_convert_both_inputs():
    response = client.post("/convert", json = {
        "formula": "H2O",
        "mass": 18.015,
        "mol": 1
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid input: Must contain either mass or mol"}


def test_convert_negative():
    response = client.post("/convert", json = {
        "formula": "H2O",
        "mol": -1
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid value: Must be greater than 0"}

def test_convert_zero():
    response = client.post("/convert", json = {
        "formula": "H2O",
        "mol": 0
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid value: Must be greater than 0"}


#Test empirical endpoint

def test_empirical_standard_anhydrous():
    response = client.post("/empirical", json = {
        "composition": {"C": 40, "H": 6.71, "O": 53.28}
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["empirical"]["formula"] == "CH2O"
    assert data["data"]["empirical"]["molar_mass"] == 30.026


def test_empirical_standard_molarmass():
    response = client.post("/empirical", json = {
        "composition": {"C": 40, "H": 6.71, "O": 53.28},
        "molar_mass": 180.156
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["molecular"]["formula"] == "C6H12O6"
    assert data["data"]["molecular"]["molar_mass"] == 180.156


def test_empirical_wrong_order():
    response = client.post("/empirical", json = {
        "composition": {"O": 40.10, "Cu": 39.82, "S": 20.09}
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["empirical"]["formula"] == "CuSO4"


def test_empirical_standard_hydrate():
    response = client.post("/empirical", json = {
        "composition": {"Cu": 39.81, "S": 20.09, "O": 40.10},
        "is_hydrate": True,
        "hydrate_mass": 100,
        "anhydrous_mass": 63.92
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["empirical"]["formula"] == "CuSO4*5H2O"
    assert data["data"]["empirical"]["molar_mass"] == 249.677


def test_empirical_standard_hydrate_molarmass():
    response = client.post("/empirical", json = {
        "composition": {"C": 26.68, "H": 2.24, "O": 71.08},
        "is_hydrate": True,
        "hydrate_mass": 100,
        "anhydrous_mass": 71.42,
        "molar_mass": 126.07
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["empirical"]["formula"] == "CHO2*H2O"
    assert data["data"]["molecular"]["formula"] == "C2H2O4*2H2O"

def test_empirical_mismatched_molarmass():
    response = client.post("/empirical", json = {
        "composition": {"C": 40, "H": 6.71, "O": 53.28},
        "molar_mass": 179
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["molecular"]["molar_mass"] == 180.156
    assert data["data"]["molecular"]["warning"] == "Entered molar mass doesn't match calculated molar mass"


def test_empirical_negative():
    response = client.post("/empirical", json = {
        "composition": {"C": -40, "H": 6.71, "O": 53.28}
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid count for 'C': Amount must be greater than 0"}

def test_empirical_zero():
    response = client.post("/empirical", json = {
        "composition": {"C": 40, "H": 0, "O": 53.28}
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid count for 'H': Amount must be greater than 0"}

def test_empirical_larger_anhydrous():
    response = client.post("/empirical", json = {
        "composition": {"H": 11.19, "O": 88.81},
        "is_hydrate": True,
        "hydrate_mass": 90,
        "anhydrous_mass": 100
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid input: Anhydrous mass cannot be greater than hydrate mass"}

def test_empirical_no_mass_lost():
    response = client.post("/empirical", json = {
        "composition": {"H": 11.19, "O": 88.81},
        "is_hydrate": True,
        "hydrate_mass": 100,
        "anhydrous_mass": 100
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid input: Cannot be hydrate due to no mass lost after evaporating"}

def test_empirical_unknown_element():
    response = client.post("/empirical", json = {
        "composition": {"Xx": 40, "C": 60}
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Unknown Element: 'Xx'"}


def test_empirical_invalid_total():
    response = client.post("/empirical", json = {
        "composition": {"C": 70, "H": 40, "O": 50}
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Mass percentages do not add up to ~100%"}


#Test limiting factor

def test_limiting_standard():
    response = client.post("/limiting", json = {
        "equation": "2H2 + O2 -> 2H2O",
        "reactants_mol": {"H2": 1, "O2": 1}
    })

    data = response.json()

    assert response.status_code == 200
    assert data["data"]["limiting_reactant"] == "H2"
    assert data["data"]["theoretical_yields"]["H2O"] == {"mol": 1, "grams": 18.015}
    assert data["data"]["excess_remnants"]["H2"] == {"mol": 0, "grams": 0}
    assert data["data"]["excess_remnants"]["O2"] == {"mol": 0.5, "grams": 15.999}

def test_limiting_reactant_missing():
    response = client.post("/limiting", json = {
        "equation": "2H2 + O2 -> 2H2O",
        "reactants_mol": {"H2": 1}
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Reactant(s) missing from list: 'O2'"}

def test_limiting_extra_element_reactants():
    response = client.post("/limiting", json = {
        "equation": "2H2 + O2 -> 2H2O",
        "reactants_mol": {"H2": 1, "O2": 1, "Fe": 1}
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Unexpected reactant(s) in list: 'Fe'"}

def test_limiting_negative():
    response = client.post("/limiting", json = {
        "equation": "2H2 + O2 -> 2H2O",
        "reactants_mol": {"H2": 1, "O2": -1}
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid count for 'O2': Amount must be greater than 0"}

def test_limiting_zero():
    response = client.post("/limiting", json = {
        "equation": "2H2 + O2 -> 2H2O",
        "reactants_mol": {"H2": 0, "O2": 1}
    })

    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid count for 'H2': Amount must be greater than 0"}