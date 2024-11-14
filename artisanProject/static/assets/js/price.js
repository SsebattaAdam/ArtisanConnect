document.addEventListener("DOMContentLoaded", function () {
  const quantityInputs = document.querySelectorAll(".quantity-input");
  const priceElements = document.querySelectorAll(".product-price"); // Ensure each price element has a unique class or ID

  quantityInputs.forEach((input, index) => {
      input.addEventListener("input", function () {
          let quantity = parseInt(input.value) || 1; // Parse the quantity as an integer, default to 1 if invalid
          let price = parseInt(priceElements[index].dataset.basePrice); // Get the base price from a data attribute
          
          if (!isNaN(price)) {
              let totalPrice = quantity * price;
              priceElements[index].textContent = `${totalPrice.toLocaleString()} USh`; // Update the price display
          }
      });
  });
});
