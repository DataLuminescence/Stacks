function buttonRename(element){
    if(element.innerHTML == "Logout"){
        element.innerHTML = "Login";
    }else{
        element.innerHTML = "Logout";
    }
}

function likeCounter(element){
    element.innerHTML =  parseInt(element.innerHTML) + 1 + " Likes";
    alert("Ninja was liked " + element.innerHTML + " times!");
}

function buttonDelete(element){
    element.style = "display: none;"
}

