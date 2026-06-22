export function page() {
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
    `
}