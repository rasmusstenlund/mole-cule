export function page() {
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
    `
}