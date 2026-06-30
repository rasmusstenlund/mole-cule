export function page() {
    return `
        <div class = "analyze">
            <div class = "enter">
            <p>Formula</p>
                <div class = "write">
                    <input type = "text" id = "analyze-formula" name = "formula" placeholder = "e.g H2O" required>
                </div>
                <div class = "buttons">
                        <input type = "button" class = "submit-button" id = "analyze-submit" value = "Analyze">
                        <input type = "button" class = "clear-button" id = "analyze-clear" value = "Clear">
                </div>
            </div>
            
            <div class = "data hidden" id = "analyze-data">
                <div class = "formula">
                    <p id = "analyze-data-formula">XY</p>
                    <p class = "molar_mass" id = "analyze-molar-mass">Molar mass: 000.000 g/mol</p>
                </div>

                <div class = "desktop">
                    <p>Element</p>
                    <p>Count</p>
                    <p>Unit mass (u)</p>
                    <p>Total mass (u)</p>
                    <p>Mass %</p>
                </div>

                <div class = "element_card">
                    <p class = "value">X</p> <p class = "mobile"></p>
                    <p class = "mobile">Count:</p> <p class = "value">0</p>
                    <p class = "mobile">Unit mass (u):</p> <p class = "value">000.000</p>
                    <p class = "mobile">Total mass (u):</p> <p class = "value">000.000</p>
                    <p class = "mobile">Mass %:</p> <p class = "value">00.00</p>
                </div>

                <div class = "element_card">
                    <p class = "value">Y</p> <p class = "mobile"></p>
                    <p class = "mobile">Count:</p> <p class = "value">0</p>
                    <p class = "mobile">Unit mass (u):</p> <p class = "value">000.000</p>
                    <p class = "mobile">Total mass (u):</p> <p class = "value">000.000</p>
                    <p class = "mobile">Mass %:</p> <p class = "value">00.00</p>
                </div>
            </div>
        </div>
    `
}

import {call_api} from "../extra-functions.js"

export function setup() {
    const submit_button = document.getElementById("analyze-submit");
    const clear_button = document.getElementById("analyze-clear");
    const formula_input = document.getElementById("analyze-formula");

    const output = document.getElementById("analyze-data");
    const formula_output = document.getElementById("analyze-data-formula");
    const mol_mass = document.getElementById("analyze-molar-mass")



    submit_button.addEventListener("click", async function () {
        var formula = formula_input.value;
        formula = formula.trim()

        if (formula) {
            var dict = {};
            dict["formula"] = formula;
            const response = await call_api(dict, "/analyze");

            mol_mass.textContent = response["molar_mass"];

            output.classList.remove("hidden")

            formula_output.textContent = formula;
        }
    })

    clear_button.addEventListener("click", function () {
        formula_input.value = ""
        
        output.classList.add("hidden")
    })

}
