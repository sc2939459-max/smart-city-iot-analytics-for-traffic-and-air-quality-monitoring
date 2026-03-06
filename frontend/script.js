async function fetchData(){

const res = await fetch("http://127.0.0.1:5001/predict");
const data = await res.json();

document.getElementById("speed").innerText = data.speed + " km/h";
document.getElementById("density").innerText = data.density;
document.getElementById("congestion").innerText = data.congestion;
document.getElementById("aqi").innerText = data.aqi;

}

fetchData();
setInterval(fetchData,5000);



const trafficChart = new Chart(
document.getElementById('trafficChart'),
{
type:'bar',
data:{
labels:['A','B','C','D','E'],
datasets:[{
label:'Traffic Density',
data:[150,200,90,70,195],
backgroundColor:'orange'
}]
}
});


const aqiChart = new Chart(
document.getElementById('aqiChart'),
{
type:'line',
data:{
labels:['10AM','11AM','12PM','1PM','2PM'],
datasets:[{
label:'AQI',
data:[160,150,100,180,140],
borderColor:'red'
}]
}
});


const pieChart = new Chart(
document.getElementById('pieChart'),
{
type:'pie',
data:{
labels:['Good','Moderate','Poor'],
datasets:[{
data:[40,35,25],
backgroundColor:['green','yellow','red']
}]
}
});