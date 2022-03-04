function odds(){
    for(var i=1; i < 21; i+=2){
        console.log(i);
    }
}
// odds();

function divisible3(){
    for(var i=100; i > 0; i--){
        if(i%3 == 0){
            console.log(i);
        }
    }
}
// divisible3();

function sequence(){
    for(var i=4; i > 0-5; i -= 1.5){
        console.log(i);
    }
}
//sequence();

function sigma(){
    var sum = 0;
    for(var i=1; i < 101; i++){
        sum += i;
    }
    console.log(sum);
}
// sigma();

function factorial(){
    var product = 1;
    for(var i=1; i < 13; i++){
        product *= i;
    }
    console.log(product);
}
factorial();