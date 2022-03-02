
var count = 1;
var countElement = document.querySelector("#count");
console.log(countElement);

function likeCounter(){
    count++;
    countElement.innerText = count + " likes";

}