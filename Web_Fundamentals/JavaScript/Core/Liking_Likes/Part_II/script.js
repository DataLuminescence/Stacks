
//Can I get the values of the first 2 characters of 
//string and parce into count1-3?

var count1 = 9;
var count2 = 12;
var count3 = 9;

function likeCounter(id){

var countElement = document.querySelector("#"+id);
console.log(countElement);

    if(id == 'count1'){
        count1++;
        countElement.innerText = count1 + " likes";
    }else if(id == 'count2'){
        count2++;
        countElement.innerText = count2 + " likes";
    }else if(id == 'count3'){
        count3++;
        countElement.innerText = count3 + " likes";
    }
}