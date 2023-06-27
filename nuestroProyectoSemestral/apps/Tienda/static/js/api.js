function consumoApi(){
    fetch("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=48400e5536d5a487887b115773f72aa5")
    .then(response => response.json())
    .then(data => {
        let wheater = document.getElementById("wheater");
        wheater.innerHTML = "id clima: "
        wheater.innerHTML += data.wheater.id;
    })
}