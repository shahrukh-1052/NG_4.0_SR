function conv() {
    let km = document.getElementById("km").value;

    if (km === "") {
        document.getElementById("res").innerText = "Please enter a value";
        return;
    }

    let miles = parseFloat(km) * 0.621371;

    document.getElementById("res").innerText = miles.toFixed(2) + " Miles";
}