const productImage = document.querySelector("#product-image");
const productName = document.querySelector("#product_name");
const genericName = document.querySelector("#generic-name");
const origin = document.querySelector("#origin");
const quantity = document.querySelector("#quantity");

searchForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const searchTerm = searchInput.value;
  getWeather(searchTerm);
  searchInput.value = "";
});

async function getWeather(searchTerm) {
  const url = 'https://world.openfoodfacts.org/api/v0/product/${searchTerm}.json';
  try {
    const response = await fetch(url);
    const weatherData = await response.json();
    showWeather(weatherData);
  } catch (error) {
    console.log(error);
  }
}

function showWeather(product) {
  productImage.innerText = product.name;
  productName.innerText = product.weather[0].description;
  genericName.innerText = `${weatherData.main.temp}°C`;
  origin.innerText = `Humidité : ${weatherData.main.humidity}%`;
  quantity.innerText = `Pression : ${weatherData.main.pressure} hPa`;
}