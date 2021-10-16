const content = [
    "Lorem",
    "Ipsum",
    [
        "Big",
        "Item",
        "Lorem",
        "Ipsum",
    ],
    "Bed",
    "Document",
    "~10"
] 

function makeContent(item, parent) {
    if (Array.isArray(item)) {
        let ul = document.createElement("ul");
        ul.innerHTML += "<li><h2>" + item[0] + "</h2></li>";   
        for (let i = 1; i < item.length; i++) {
            makeContent(item[i], ul);
        }
        parent.appendChild(ul);
    } else {
        parent.innerHTML += "<li>" + item + "</li>";
    }
}

makeContent(content, document.getElementsByClassName("menu")[0]);

//          THEMES

const themes = {
Blueish: ['rgb(46, 132, 166)', 'rgb(10, 166, 122)', 'rgb(147, 191, 175)', 'rgb(217, 197, 173)', 'rgb(64, 64, 64)'],
Redish: ['rgb(3, 140, 101)', 'rgb(242, 235, 223)', 'rgb(242, 129, 29)', 'rgb(242, 5, 5)', 'rgb(140, 3, 3)'],
Yellowish: ['rgb(17, 33, 64)', 'rgb(50, 61, 64)', 'rgb(242, 229, 48)', 'rgb(166, 159, 65)', 'rgb(242, 211, 53)'],
}

for (const iterator of object) {
    
}
function addTheme() {
    
}