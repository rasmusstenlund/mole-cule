export function page() {
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
    `
}