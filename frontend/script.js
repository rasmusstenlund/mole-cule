function get_home_page() {
    return `
        <h1>Welcome to Mole-Cule</h1>
        <p>This is a chemistry tool</p>
    `;
}   

function get_analyze_page() {
    return `
        <h1>Analyze compound</h1>
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