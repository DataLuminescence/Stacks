
function pizzaOven(crust, sauce, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crust;
    pizza.sauceType = sauce;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;

    return pizza;
}

function randomPizza(){
    var randCrust = ["deep dish", "hand tossed", "thin"];
    var randSauce = ["traditional", "white", "beans"];
    var randCheeses = ["mozzarella", "cheddar", "feta", "monterrey jack" ];
    var randToppings = ["pepperoni", "sausage", "ham", "bacon", "soyrizo", "green pepper", "jalapeno", "mushroom"];

    var randPizza = {};
    randPizza.crustType = randCrust[Math.floor(Math.random() * (3 - 0) + 0)];
    randPizza.sauceType = randSauce[Math.floor(Math.random() * (3 - 0) + 0)];
    randPizza.cheeses = randCheeses[Math.floor(Math.random() * (4 - 0) + 0)];
    randPizza.toppings = randToppings[Math.floor(Math.random() * (8 - 0) + 0)];

    return randPizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni","sausage"]);
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
var angryPizza = pizzaOven("thin", "traditional", ["mozzarella"], ["pineapple", "jalapeno"]);
var abominationpizza = pizzaOven("deep dish", "white", ["mozzarella", "chedar"], ["pepperoni", "bacon", "hotcheetos"]);
var randPizza = randomPizza();

console.log(pizza1);
console.log(pizza2);
console.log(angryPizza);
console.log(abominationpizza);
console.log(randPizza);