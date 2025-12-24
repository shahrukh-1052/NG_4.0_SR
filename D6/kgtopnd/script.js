function pound(){
    let kgs = document.getElementById("kg").value;
    if (kgs ===""){
        document.getElementById("res").innerHTML = "Please Enter Numericals Only";
        return

    }
    let pound = parseFloat("km") * 2.20462262;
    document.getElementById("res").innerHTML= pound.toFixed(2) + "Pounds" ;
}