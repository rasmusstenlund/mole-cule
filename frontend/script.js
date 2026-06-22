import * as home from "./pages/home.js"
import * as analyze from "./pages/analyze.js"
import * as convert from "./pages/convert.js"
import * as balance from "./pages/balance.js"
import * as empirical from "./pages/empirical.js"
import * as limiting from "./pages/limiting.js"

const routes = {
    '#/': home,
    '#/analyze': analyze,
    '#/convert': convert,
    '#/balance': balance,
    '#/empirical': empirical,
    '#/limiting': limiting,
}

function router() {
    const current_hash = window.location.hash || '#/';

    const content_function = routes[current_hash];

    const app_container = document.getElementById('app');
    
    if (content_function) {
        app_container.innerHTML = content_function.page();
        
        
    } else {
        app_container.innerHTML = '<h1>404</h1><p>Page Not Found</p>'
    }
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router);