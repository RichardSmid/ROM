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
const tag = document.createElement("ul");

function makeContent(item) {
    console.log(item);
    if (Array.isArray(item)) {
        tag.innerHTML += "<ul>";
        tag.innerHTML += "<li><h2>" + item[0] + "</h2></li>";   
        for (let i = 1; i < item.length; i++) {
            makeContent(item[i])
            if (i == item.length -1) {
                
            }
            tag.innerHTML += "</ul>";
        }
    } else {
        tag.innerHTML += "<li>" + item + "</li>";
    }
}

makeContent(content);