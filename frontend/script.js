function get_home_page() {
    return `
        <h1>Welcome to Mole-Cule</h1>
        <p>This is a chemistry tool</p>
    `;
}   

function get_analyze_page() {
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
            
            <div class = "data">
                <div class = "formula">
                    <p>XY</p>
                    <p class = "molar_mass">Molar mass: 000.000 g/mol</p>
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
    `;
}

function get_convert_page() {
    return `
        <div class = "convert">
            <div class = "enter">
                <p>Formula</p>
                <input type = "text" id = "convert-formula" name = "formula" placeholder = "e.g H2O" required>

                <p>Value to convert</p>
                <div class = "unit">
                    <div class = "toggle-unit">
                        <input type = "radio" id = "convert-mol" name = "unit" value = "mol">
                        <label for = "convert-mol">Mol</label>

                        <input type = "radio" id = "convert-mass" name = "unit" value = "mass" checked>
                        <label for = "convert-mass">Mass</label>

                        <div class = "slider"></div>
                    </div>

                    <input class = "write-unit" type = "text" id = "convert-unit-count" name = "count" required>

                </div>

                <div class = "buttons">
                    <input type = "button" class = "submit-button" id = "convert-submit" value = "Convert">
                    <input type = "button" class = "clear-button" id = "convert-clear" value = "Clear">
                </div>
            </div>

            <div class = "data">
                <p class = "formula">XY</p>

                <div class = "count-data">
                    <div class = "mol-data">
                        <h4>Mol</h4>
                        <p class = "data-mol">00.00</p>
                    </div>

                    <div class = "mass-data">
                        <h4>Mass (g)</h4>
                        <p class = "data-mass">000.000</p>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function get_balance_page() {
    return `
        <div class = "balance">
            <div class = "enter">
                <div class = "equation-maker">
                    <p>Reactants</p>
                    <div class = "equation-side reactants-side">
                        <input type = "text" class = "reactant-input">
                        <input type = "button" id = "balance-add-reactant" class = "add-button" value = "+ Reactant">
                    </div>
                    <p class = "arrow">&#8594</p>
                    <p>Products</p>
                    <div class = "equation-side products-side">
                        <input type = "text" class = "product-input">
                        <input type = "button" id = "balance-add-product" class = "add-button" value = "+ Product">
                    </div>
                </div>
                <div class = "buttons">
                    <input type = "button" class = "submit-button" id = "balance-submit" value = "Balance">
                    <input type = "button" class = "clear-button" id = "balance-clear" value = "Clear">
                </div>
            </div>

            <div class = "data">
                <div class = "entered">
                    <h4 class = "balance-equation-header">Entered Equation</h4>
                    <p id = "balance-entered-equation" class = "balance-equation-text">X + Y -> X2Y</p>
                </div>

                <div class = "balanced">
                    <h4 class = "balance-equation-header">Balanced Equation</h4>
                    <p id = "balance-balanced-equation" class = "balance-equation-text">2X + Y -> X2Y</p>
                </div>
            </div>
        </div>
    `;
}

function get_empirical_page() {
    return `
        <div class = "empirical">
            <div class = "enter">
                <p>Composition</p>
                <div class = "composition-maker">
                    <div class = "empirical-part-list">
                        <div class = "empirical-part">
                            <input type = "text" class = "empirical-element" placeholder = "Element">
                            <span>:</span>
                            <input type = "text" class = "empirical-mass_percentage" placeholder = "Mass %">
                        </div>
                    </div>

                    <input type = "button" class = "add-button" id = "empirical-add-element" value = "+ Element">
                </div>

                <div class = "empirical-optional">
                    <div class = "optional-molar-mass">
                        <p>(Optional) Molar mass</p>
                        <input type = "text" id = "molar-mass">
                    </div>
                    <div class = "optional-hydrate">
                        <label class = "hydrate-container">Is Hydrate?
                            <input type = "checkbox" id = "empirical-hydrate-check">
                            <span class = "checkmark"></span>
                        </label>
                    
                        <div class = "optional-hydrate-data">
                            <div class = "hydrate-mass">
                                <p>Hydrate mass (Before burning)</p>
                                <input type = "text" id = "empirical-hydrate-mass" required>
                            </div>
                            <div class = "anhydrous-mass">
                                <p>Anhydrous mass (After burning)</p>
                                <input type = "text" id = "empirical-anhydrous-mass" required>
                            </div>
                        </div>
                    </div>
                </div>

                <div class = "buttons">
                    <input type = "button" class = "submit-button" id = "empirical-submit" value = "Get Empirical">
                    <input type = "button" class = "clear-button" id = "empirical-clear" value = "Clear">
                </div>
            </div>

            <div class = "data">
                <div class = "empirical-part">
                    <h4>Empirical</h4>
                    <div class = "empirical-data">
                        <p id = "empirical-empirical-formula">XY</p>
                        <p id = "empirical-empirical-mass">60 g/mol</p>
                    </div>
                </div>
                <div class = "molecular-part">
                    <h4>Molecular</h4   >
                    <div class = "molecular-data">
                        <p id = "empirical-molecular-formula">X2Y2</p>
                        <p id = "empirical-molecular-mass">120 g/mol</p>
                    </div>
                </div>
                <p id = "empirical-warning">Warning: Entered molar mass doesn't match calculated</p>
            </div>
        </div>
    `;
}

function get_limiting_page() {
    return `
        <div class = "limiting">
            <div class = "enter">
                <p>Composition</p>
                <div class = "equation-maker">
                    <p>Reactants</p>
                    <div class = "equation-side reactants-side">
                        <input type = "text" class = "reactant-input">
                        <input type = "button" id = "balance-add-reactant" class = "add-button" value = "+ Reactant">
                    </div>
                    <p class = "arrow">&#8594</p>
                    <p>Products</p>
                    <div class = "equation-side products-side">
                        <input type = "text" class = "product-input">
                        <input type = "button" id = "balance-add-product" class = "add-button" value = "+ Product">
                    </div>
                </div>

                <p>Reactants Mol</p>
                <div class = "reactants-mol-list">
                    <div class = "reactant-mol">
                        <span class = "reactant">X2</span>
                        <span>:</span>
                        <input type = "text" class = "mol" placeholder = "Mol">
                    </div>
                </div>

                <div class = "buttons">
                    <input type = "button" class = "submit-button" id = "limiting-submit" value = "Get Limiting">
                    <input type = "button" class = "clear-button" id = "limiting-clear" value = "Clear">
                </div>
            </div>
            <div class = "data">
                <div class = "equation">
                    <h4>Equation</h4>
                    <p id = "limiting-equation">X2 + 2Y -> 2XY</p>
                </div>
                
                <div class = "limiting-reactant">
                    <h4>Limiting Reactant</h4>
                    <p id = "limiting-limiting-reactant">X2</p>
                </div>

                <div class = "theoretical">
                    <h4>Theoretical Yields</h4>
                    <div class = "theo-yields-list">
                        <div class = "theo-yield">
                            <p class = "product">XY</p>
                            <span>:</span>
                            <p class = "count">3.5 Mol</p>
                        </div>
                    </div>
                </div>

                <div class = "excess">
                    <h4>Excess Remnants</h4>
                    <div class = "excess-remnants-list">
                        <div class = "excess-remnant">
                            <p class = "reactant">X2</p>
                            <span>:</span>
                            <p class = "count">0 Mol</p>
                        </div>

                        <div class = "excess-remnant">
                            <span class = "reactant">Y</span>
                            <span>:</span>
                            <span class = "count">0.4 Mol</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

const routes = {
    '#/': get_home_page,
    '#/analyze': get_analyze_page,
    '#/convert': get_convert_page,
    '#/balance': get_balance_page,
    '#/empirical': get_empirical_page,
    '#/limiting': get_limiting_page,


}

function router() {
    const current_hash = window.location.hash || '#/';

    const content_function = routes[current_hash];

    const app_container = document.getElementById('app');
    
    if (content_function) {
        app_container.innerHTML = content_function();
    } else {
        app_container.innerHTML = '<h1>404</h1><p>Page Not Found</p>'
    }
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router)