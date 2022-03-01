console.log("Hello World");

// function print255(){
//     for(var i=1; i<2; i++){
//         console.log(i);
//     }
// }

// function dostuff(e){
//     console.log(e);
// //element.remove();
// //element.innerText = "This has changed!";

//     element.innerText = "<h1 class='important'><h1>";
//     element.innerHTML = "<button onclick='console.log(`more stuff`)'>Dynamic Button</button>";
// }


function d6() {
    var roll = (Math.random()* (6 - 1 + 1) + 1);
    return roll;
}
const element = document.getElementById("randomhelp");
element.innerHTML = "" +roll;

parseInt(element.innerHTML

var playerRoll = d6();
console.log("The player rolled: " + playerRoll);