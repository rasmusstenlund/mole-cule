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
    `
}