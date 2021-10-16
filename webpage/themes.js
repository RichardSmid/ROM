function setTheme(themeID) {
    document.cookie = "theme=" + themeID + ";path=/;";
    loadTheme();
}

function loadTheme() {
    let currentTheme = document.cookie;
    let root = document.documentElement;
    console.log(currentTheme);
}