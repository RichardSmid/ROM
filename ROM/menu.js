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
const tag = document.getElementsByClassName("menu")[0];

function makeContent(item, parent) {
    console.log(item);
    if (Array.isArray(item)) {
        // tag.innerHTML += "<ul>";
        let ul = document.createElement("ul");
        ul.innerHTML += "<li><h2>" + item[0] + "</h2></li>";   
        for (let i = 0; i < item.length; i++) {
            makeContent(item[i], ul);
        }
        parent.appendChild(ul);
        // tag.innerHTML += "</ul>";
    } else {
        parent.innerHTML += "<li>" + item + "</li>";
    }
}

makeContent(content, tag);
// document.getElementsByClassName("menu")[0].appendChild(tag);