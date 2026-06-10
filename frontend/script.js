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
                <form class = "write">
                    <input class = "compound" type = "text" id = "formula" name = "formula" placeholder = "e.g H2O">
                    <input class = "clear" type = "button" value = "Clear">
                </form>
                <form class = "submit">
                    <input type = "button" value = "Analyze">
                </form>
            </div>
            <div class = "elements">
                <div>
                    <p>Formula</p>
                    <p>Molar mass</p>
                </div>
                <div class = "element">
                    <p class = "symbol">Symbol</p>
                    <p>Count</p>
                    <p>Atomic_num</p>
                    <p>Atomic_mass</p>
                    <p></p>
                    <p>Mass_contr</p>
                    <p>Mass_percent</p>
                </div>
                <div class = "element">
                    <p class = "symbol">Symbol</p>
                    <p>Count</p>
                    <p>Atomic_num</p>
                    <p>Atomic_mass</p>
                    <p></p>
                    <p>Mass_contr</p>
                    <p>Mass_percent</p>
                </div>
                <div class = "element">
                    <p class = "symbol">Symbol</p>
                    <p>Count</p>
                    <p>Atomic_num</p>
                    <p>Atomic_mass</p>
                    <p></p>
                    <p>Mass_contr</p>
                    <p>Mass_percent</p>
                </div>
            </div>
        </div>
    `;
}

function get_convert_page() {
    return `
        <h1>Convert between mass and mol</h1>
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