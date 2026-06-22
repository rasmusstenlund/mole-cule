export function page() {
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
    `
}