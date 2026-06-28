export function page() {
    return `
        <div class = "empirical">
            <div class = "enter">
                <p>Composition</p>
                <div class = "composition-maker">
                    <div id = "empirical-part-list">
                        <div class = "empirical-part show">
                            <input type = "text" class = "empirical-element" placeholder = "Element">
                            <p>:</p>
                            <input type = "text" class = "empirical-mass-percentage" placeholder = "Mass %">
                        </div>
                    </div>

                    <input type = "button" class = "add-button" id = "empirical-add-element" value = "+ Element">
                </div>

                <div class = "empirical-optional">
                    <div class = "optional-molar-mass">
                        <p>(Optional) Molar mass</p>
                        <input type = "text" id = "empirical-molar-mass">
                    </div>
                    <div class = "optional-hydrate">
                        <label class = "hydrate-container">Is Hydrate?
                            <input type = "checkbox" id = "empirical-hydrate-check">
                            <span class = "checkmark"></span>
                        </label>
                    
                        <div class = "optional-hydrate-data">
                            <div class = "hydrate-mass">
                                <p>Hydrate mass (Before burning)</p>
                                <input type = "text" id = "empirical-hydrate-mass" placeholder = "(g)">
                            </div>
                            <div class = "anhydrous-mass">
                                <p>Anhydrous mass (After burning)</p>
                                <input type = "text" id = "empirical-anhydrous-mass" placeholder = "(g)">
                            </div>
                        </div>
                    </div>
                </div>

                <div class = "buttons">
                    <input type = "button" class = "submit-button" id = "empirical-submit" value = "Get Empirical">
                    <input type = "button" class = "clear-button" id = "empirical-clear" value = "Clear">
                </div>
            </div>

            <div class = "data hidden" id = "empirical-data">
                <div class = "empirical-part">
                    <h4>Empirical</h4>
                    <div class = "empirical-data">
                        <p id = "empirical-empirical-formula">XY</p>
                        <p id = "empirical-empirical-mass">60 g/mol</p>
                    </div>
                </div>
                <div class = "molecular-part hidden" id = "empirical-molecular">
                    <h4>Molecular</h4>
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

function create_empirical_part(empirical_list) {
    const element_input = document.createElement("input");
    element_input.type = "text";
    element_input.classList.add("empirical-element");
    element_input.placeholder = "Element";

    const colon = document.createElement("p");
    colon.textContent = ":"

    const percent_input = document.createElement("input");
    percent_input.type = "text";
    percent_input.classList.add("empirical-mass-percentage");
    percent_input.placeholder = "Mass %";

    const element_part = document.createElement("div");
    element_part.classList.add("empirical-part");
    element_part.appendChild(element_input);
    element_part.appendChild(colon);
    element_part.appendChild(percent_input);

    empirical_list.appendChild(element_part)

    setTimeout(function () {
        element_part.classList.add("show")
    }, 10)
}

function make_composition(empirical_list) {
    var composition = {}
    for (const empirical_part of empirical_list) {
        const element = empirical_part.querySelector(".empirical-element").value.trim();
        const percent = empirical_part.querySelector(".empirical-mass-percentage").value.trim();

        if (element && isFinite(percent)) {
            composition[element] = percent
        } else if (!(element) && !(percent)) {
            continue
        } else {
            return false;
        }
    }

    if (composition) {
        return composition;
    } else {
        return false;
    }
}

export function setup() {
    const empirical_list = document.getElementById("empirical-part-list");
    const add_element = document.getElementById("empirical-add-element");

    add_element.addEventListener("click", function () {
        create_empirical_part(empirical_list);
    })

    empirical_list.addEventListener("input", function () {
    })

    const submit_button = document.getElementById("empirical-submit");
    const clear_button = document.getElementById("empirical-clear");
    const output = document.getElementById("empirical-data");
    const check = document.getElementById("empirical-hydrate-check");
    const molar_mass_input = document.getElementById("empirical-molar-mass");
    const empirical_output = document.getElementById("empirical-empirical");
    const molecular_output = document.getElementById("empirical-molecular")

    clear_button.addEventListener("click", function () {
        empirical_list.innerHTML = "";
        create_empirical_part(empirical_list);
        output.classList.add("hidden");
        check.checked = false;
    })

    submit_button.addEventListener("click", function () {
        const molar_mass = molar_mass_input.value;

        const composition = make_composition(empirical_list);
        if (composition) {
            molecular_output.classList.add("hidden")
            if (molar_mass) {
                if (isFinite(molar_mass)) {
                    molecular_output.classList.remove("hidden");
                }
            }

            output.classList.remove("hidden");
        }
    })

}