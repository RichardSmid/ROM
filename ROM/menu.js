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