export function page() {
    return `
        <div class = "balance">
            <div class = "enter">
                <div class = "equation-maker">
                    <p>Reactants</p>
                    <div class = "equation-side" id = "balance-reactants-side">
                        <div class = "equation-part-container">
                            <input type = "text" class = "reactant-input">
                        </div>
                    </div>
                    <input type = "button" id = "balance-add-reactant" class = "add-button" value = "+ Reactant">
                    <p class = "arrow">&#8594</p>
                    <p>Products</p>
                    <div class = "equation-side" id = "balance-products-side">
                        <div class = "equation-part-container">
                            <input type = "text" class = "product-input">
                        </div>
                    </div>
                    <input type = "button" id = "balance-add-product" class = "add-button" value = "+ Product">
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

export function setup() {
    const add_reactant = document.getElementById("balance-add-reactant");
    const add_product = document.getElementById("balance-add-product");
    const reactants_list = document.getElementById("balance-reactants-side");
    const products_list = document.getElementById("balance-products-side");


    add_reactant.addEventListener("click", function () {
        const last_input = reactants_list.lastElementChild;
        const plus = document.createElement("p");
        plus.textContent = "+";

        last_input.appendChild(plus)

        const div = document.createElement("div");
        div.classList.add("equation-part-container");

        const input = document.createElement("input");
        input.type = "text";
        input.classList.add("reactant-input");

        div.appendChild(input)
    
        reactants_list.append(div)
    })

    add_product.addEventListener("click", function () {
        const last_input = products_list.lastElementChild;
        const plus = document.createElement("p");
        plus.textContent = "+";
        last_input.appendChild(plus)

        const container = document.createElement("div");
        container.classList.add("equation-part-container");
        const input = document.createElement("input");
        input.type = "text";
        input.classList.add("product-input");
        container.appendChild(input);

        products_list.appendChild(container);
    })
}