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

            <div class = "data hidden" id = "balance-data">
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
        last_input.appendChild(plus);

        const container = document.createElement("div");
        container.classList.add("equation-part-container");
        const input = document.createElement("input");
        input.type = "text";
        input.classList.add("product-input");
        container.appendChild(input);

        products_list.appendChild(container);
    })

    const output = document.getElementById("balance-data")
    const submit_button = document.getElementById("balance-submit");
    const clear_button = document.getElementById("balance-clear");
    const entered = document.getElementById("balance-entered-equation");

    clear_button.addEventListener("click", function () {
        const reactant_input = document.createElement("input");
        reactant_input.type = "text";
        reactant_input.classList.add("reactant-input");

        const reactant_container = document.createElement("div");
        reactant_container.classList.add("equation-part-container");
        reactant_container.appendChild(reactant_input);

        reactants_list.innerHTML = "";
        reactants_list.appendChild(reactant_container);

        const product_input = document.createElement("input");
        product_input.type = "text";
        product_input.classList.add("product-input");

        const product_container = document.createElement("div");
        product_container.classList.add("equation-part-container");
        product_container.appendChild(product_input);

        products_list.innerHTML = "";
        products_list.appendChild(product_container);

        output.classList.add("hidden");
    })

    submit_button.addEventListener("click", function () {
        const reactants = reactants_list.getElementsByClassName("reactant-input");
        const products = products_list.getElementsByClassName("product-input");


        let reactant_side = ""

        for (let i = 0; i < reactants.length; i++) {
            let reactant = reactants[i].value;
            reactant = reactant.trim();

            if (!reactant) {
                continue
            }

            reactant_side += reactant;

            if (i < (reactants.length - 1)) {
                reactant_side += " + "
            }
        }

        let product_side = ""

        for (let i = 0; i < products.length; i++) {
            let product = products[i].value;
            product = product.trim();

            if (!product) {
                continue
            }

            product_side += product;

            if (i < (products.length - 1)) {
                product_side += " + "
            }
        }

        if (reactant_side && product_side) {
            entered.textContent = `${reactant_side} -> ${product_side}`;
            output.classList.remove("hidden");
        }
    })
}