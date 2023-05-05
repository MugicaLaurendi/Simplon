const apiKey = "847caf80e14695a9f6cb3cc9bbc35065";

const searchForm = document.querySelector("#search-form");
const searchInput = document.querySelector("#search-input");
const locationEl = document.querySelector("#location");
const weatherEl = document.querySelector("#weather");
const temperatureEl = document.querySelector("#temperature");
const humidityEl = document.querySelector("#humidity");
const pressureEl = document.querySelector("#pressure");
const windEl = document.querySelector("#wind");

searchForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const searchTerm = searchInput.value;
  getWeather(searchTerm);
  searchInput.value = "";
});

async function getWeather(searchTerm) {
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${searchTerm}&appid=${apiKey}&units=metric`;
  try {
    const response = await fetch(url);
    const weatherData = await response.json();
    console.log(weatherData);
    showWeather(weatherData);
  } catch (error) {
    console.log(error);
  }
}

function showWeather(weatherData) {
  locationEl.innerText = weatherData.name;
  weatherEl.innerText = weatherData.weather[0].description;
  temperatureEl.innerText = `${weatherData.main.temp}°C`;
  humidityEl.innerText = `Humidité : ${weatherData.main.humidity}%`;
  pressureEl.innerText = `Pression : ${weatherData.main.pressure} hPa`;
  windEl.innerText = `Vent : ${weatherData.wind.speed} km/h`;
  document.querySelector("#weather-info").style.display = "block";
}