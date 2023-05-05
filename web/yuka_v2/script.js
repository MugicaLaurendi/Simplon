console.log('script ok');

const searchForm = document.querySelector("#search-form");
const searchInput = document.querySelector("#search-input");

const productImage = document.querySelector("#product-image");
const productName = document.querySelector("#product-name");
const genericName = document.querySelector("#generic-name");
const origin = document.querySelector("#origin");
const quantity = document.querySelector("#quantity");

searchForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const searchTerm = searchInput.value;
  getProduct(searchTerm);
  searchInput.value = "";
});

async function getProduct(searchTerm) {
  console.log("getproduct");

  const url = 'https://world.openfoodfacts.org/api/v0/product/${searchTerm}.json';

  try {
    const response = await fetch(url);
    const productData = await response.json();
    showProduct(productData);
    windows.location.href = 'product.html';
  } catch (error) {
    console.log(error);
  }
}

function showProduct(product) {
  console.log("showproduct");
  productImage.innerText = product.product.image_url;
  productName.innerText = product.weather[0].description;
  genericName.innerText = `${weatherData.main.temp}°C`;
  origin.innerText = `Humidité : ${weatherData.main.humidity}%`;
  quantity.innerText = `Pression : ${weatherData.main.pressure} hPa`;
}