
function addToKeepItem() {
    let item = document.getElementById("to-keep-entry");
    if (item.value !== "") {
        addElementToList(item.value, "to-keep-elements");
        item.value = "";
    }
}

function addToImproveItem() {
    let item = document.getElementById("to-improve-entry");
    if (item.value !== "") {
        addElementToList(item.value, "to-improve-elements");
        item.value = "";
    }
}

function addElementToList(item, listId) {
    let list = document.getElementById(listId);

    let div = document.createElement("div");
    div.className = "item";

    let p = document.createElement("p");
    p.innerText = `${item}`;

    let button = document.createElement("button");
    button.innerText = "Delete";
    button.addEventListener("click", deleteItem);

    div.appendChild(p);
    div.appendChild(button);

    list.appendChild(div);
}

function deleteItem(e) {
    let toDelete = e.target.parentElement;
    let deleteFrom = toDelete.parentElement;
    deleteFrom.removeChild(toDelete);
}

function sendBoard() {
    let boardData = getRetroJSON();
    let request = new XMLHttpRequest();
    request.onload = function() {
        console.log(this.responseURL);
        window.location = this.responseURL;
    };
    request.open("POST", "/add");
    request.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    request.send(boardData);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getRetroJSON() {
    let toKeep = document.getElementById("to-keep-elements");
    let toKeepList = getListOfItems(toKeep);
    let toImprove = document.getElementById("to-improve-elements");
    let toImproveList = getListOfItems(toImprove);
    let boardId = document.getElementsByClassName("retro-board")[0].getAttribute("id");

    let boardData = {"toKeep": toKeepList, "toImprove": toImproveList, "boardId": boardId};
    return JSON.stringify(boardData);
}

function getListOfItems(boardPart) {
    let items = [];
    for (let item of boardPart.getElementsByClassName("item")) {
        items.push(item.getElementsByTagName("p")[0].innerText);
    }
    return items;
}