const speedEl = document.getElementById("speed");
const densityEl = document.getElementById("density");
const congestionEl = document.getElementById("congestion");
const aqiEl = document.getElementById("aqi");

const labels = [];
const speedData = [];

const trafficChart = new Chart(
    document.getElementById("trafficChart"),
    {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Average Speed (km/h)",
                data: speedData,
                borderWidth: 2
            }]
        }
    }
);

async function fetchData() {
    try {
        const response = await fetch("http://127.0.0.1:5001/api/latest");
        const data = await response.json();

        console.log("LIVE DATA:", data);

        speedEl.textContent = data.avg_speed;
        densityEl.textContent = data.traffic_density;
        congestionEl.textContent = data.congestion;
        aqiEl.textContent = data.aqi;

        labels.push(data.timestamp);
        speedData.push(data.avg_speed);

        if (labels.length > 10) {
            labels.shift();
            speedData.shift();
        }

        trafficChart.update();

    } catch (error) {
        console.error("API ERROR:", error);
    }
}

setInterval(fetchData, 5000);
fetchData();
