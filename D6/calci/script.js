// function changename(){
//     document.getElementById("sr").innerHTML = "SUMATHI REDDY";
// }

function add(){
    let a = document.getElementById("num1").value;
    let b = document.getElementById("num2").value;

    let result = parseFloat(a) + parseFloat(b);
    document.getElementById("result").innerHTML = result;
}


function sub(){
    let a = document.getElementById("num1").value;
    let b = document.getElementById("num2").value;
    
    let result = parseFloat(a) - parseFloat(b);
    document.getElementById("result").innerHTML = result;
}


function mul(){
    let a = document.getElementById("num1").value;
    let b = document.getElementById("num2").value;
    
    let result = parseFloat(a) * parseFloat(b);
    document.getElementById("result").innerHTML = result;
}

function div(){
    let a = document.getElementById("num1").value;
    let b = document.getElementById("num2").value;
    
    let result = parseFloat(a) / parseFloat(b);
    document.getElementById("result").innerHTML = result;
}