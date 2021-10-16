function setTheme(themeID) {
    document.cookie = "theme:" + themeID;
    
}

function loadTheme() {
    let currentTheme = parseInt(document.cookie.substring(5, document.cookie - 1));
    let root = document.documentElement;
    
}