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
                <form>
                    <div class = "write">
                        <input type = "text" id = "analyze-formula" name = "formula" placeholder = "e.g H2O" required>
                    </div>
                    <div class = "buttons">
                        <input type = "submit" class = "submit" value = "Analyze">
                        <input type = "button" class = "clear" value = "Clear">
                    </div>
                </form>
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
                <form>
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
                        <input class = "submit" type = "submit" value = "Convert">
                        <input class = "clear" type = "button" value = "Clear">
                    </div>
                </form>
            </div>
            <div class = "data">
                <p class = "formula">XY</p>

                <div class = "count-data">
                    <div class = "mol-data">
                        <p>Mol</p>
                        <p class = "data-mol">00.00</p>
                    </div>

                    <div class = "mass-data">
                        <p>Mass (g)</p>
                        <p class = "data-mass">000.000</p>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function get_balance_page() {
    return `
        <h1>Balance reaction</h1>
    `;
}

function get_empirical_page() {
    return `
        <h1>Get empirical formula from mass percents</h1>
    `;
}

function get_limiting_page() {
    return `
        <h1>Get limiting reactants and theoretical yields</h1>
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