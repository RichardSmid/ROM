console.log(document.cookie);

function setTheme(themeID) {
    document.cookie = "username=DOG;path=/;";
    console.log(document.cookie);
    loadTheme();
}

function loadTheme() {
    let currentTheme = document.cookie;
    let root = document.documentElement;
    console.log(currentTheme);
}