console.log('script ok');

const searchForm = document.getElementById("search-form");
const searchInput = document.querySelector("#search-input");

//const productImage = document.querySelector("#product-image");
const productName = document.querySelector("#product-name");
const genericName = document.querySelector("#generic-name");
const origin = document.querySelector("#origin");
const quantity = document.querySelector("#quantity");

const imageContainer = document.querySelector("#image-container");
const image = document.createElement("img");

searchForm.addEventListener("submit", (event) => {
  console.log('eventlistener');
  event.preventDefault();
  const searchTerm = searchInput.value;
  getProduct(searchTerm);
  searchInput.value = "";
});

async function getProduct(searchTerm) {
  console.log("getproduct");

  const url = `https://world.openfoodfacts.org/api/v0/product/${searchTerm}.json`;

  try {
    const response = await fetch(url);
    const productData = await response.json();
    console.log(productData);
    showProduct(productData);
    //windows.location.href = 'product.html';
  } catch (error) {
    console.log(error);
  }
}

function showProduct(product) {
  console.log("showproduct");
  //productImage.innerText = product.product.image_url;
  console.log(product.product.product_name);
  image.setAttribute("src", product.product.image_url);
  imageContainer.appendChild(image);
  //productImage.innerHTML = product.product.image_url;
  productName.innerText = `Nom : ${product.product.product_name}`;
  genericName.innerText = `Nom generique : ${ product.product.generic_name}`;
  origin.innerText =`Origine : ${product.product.nutriscore_data.origins}`;
  quantity.innerText = `Quantité : ${product.product.product_quantity} g`;
  console.log('end');
}