"use strict";

const citiesUnparsed = JSON.parse(
  document.getElementById("cities-list-json").textContent
);

const nameCity = document.location.pathname.slice(
  8,
  document.location.pathname.length - 1
);

function findCity() {
  for (let i = 0; i < citiesUnparsed.length; i++) {
    const cityUnparsed = citiesUnparsed[i];
    const city = JSON.parse(cityUnparsed);
    if (city["name"] === nameCity) {
      return city;
    }
  }
}
const cityObj = findCity();

function generateDatas(objectField, start, end) {
  let data = [];
  for (let i = start; i < end; i++) {
    data.push(objectField[i]);
  }
  return data;
}

function createNewChart(start, end) {
  const data = {
    labels: generateDatas(Object.keys(cityObj), start, end),
    datasets: [
      {
        label: "Dataset 1",
        data: generateDatas(Object.values(cityObj), start, end),
        backgroundColor: [
          "rgba(255, 99, 132,1)",
          "rgba(54, 162, 235,1)",
          "rgba(255, 206, 86,1)",
          "rgba(75, 192, 192,1)",
          "rgba(153, 102, 255,1)",
        ],
      },
    ],
  };

  const config = {
    type: "polarArea",
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
        },
        title: {
          display: true,
          text: "Chart.js Polar Area Chart",
        },
      },
    },
  };
  return config;
}

new Chart(document.getElementById("myChart"), createNewChart(3, 8));
new Chart(document.getElementById("myChart-2"), createNewChart(8, 13));
new Chart(document.getElementById("myChart-3"), createNewChart(13, 18));
new Chart(document.getElementById("myChart-4"), createNewChart(18, 23));
new Chart(document.getElementById("myChart-5"), createNewChart(23, 28));
new Chart(document.getElementById("myChart-6"), createNewChart(28, 33));
new Chart(document.getElementById("myChart-7"), createNewChart(33, 38));