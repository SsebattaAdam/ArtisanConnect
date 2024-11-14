// Utility function to update the cart summary in the UI
function updateCartSummary() {
    let cartItems = JSON.parse(sessionStorage.getItem('cart')) || [];
    let subTotal = 0;
    let shippingCost = 0;
    let discount = 0;

    // Calculate the subtotal, shipping, and discount
    cartItems.forEach(item => {
        subTotal += item.price * item.quantity;
    });

    // Example shipping and discount calculations
    shippingCost = 500; // Flat rate shipping
    discount = 0; // For now, no discount applied

    // Total Price
    let total = subTotal + shippingCost - discount;

    // Update cart display
    document.getElementById("sub-total").innerText = `UGX ${subTotal}`;
    document.getElementById("shipping-cost").innerText = `UGX ${shippingCost}`;
    document.getElementById("discount").innerText = `-UGX ${discount}`;
    document.getElementById("total").innerText = `UGX ${total}`;
}

// Function to update the cart items in the UI
function updateCartItems() {
    let cartItems = JSON.parse(sessionStorage.getItem('cart')) || [];
    let cartTableBody = document.getElementById('cart-items');
    cartTableBody.innerHTML = ''; // Clear the current cart table

    if (cartItems.length === 0) {
        cartTableBody.innerHTML = `<tr><td colspan="5">Your cart is empty.</td></tr>`;
        return;
    }

    cartItems.forEach((item, index) => {
        let totalPrice = item.price * item.quantity;
        let row = document.createElement('tr');

        row.innerHTML = `
            <td><img src="${item.image}" alt="${item.name}"><div>${item.name}</div></td>
            <td>UGX ${item.price}</td>
            <td class="quantity">
                <div class="quantity-controls">
                    <button type="button" class="quantity-btn" onclick="updateQuantity(${index}, -1)">-</button>
                    <input type="number" step="1" min="1" max="100" name="quantity" value="${item.quantity}" class="quantity-input" onchange="changeQuantity(${index}, this.value)">
                    <button type="button" class="quantity-btn" onclick="updateQuantity(${index}, 1)">+</button>
                </div>
            </td>
            <td>UGX ${totalPrice}</td>
            <td><a href="javascript:void(0);" onclick="removeItem(${index})">Remove</a></td>
        `;

        cartTableBody.appendChild(row);
    });

    updateCartSummary(); // Update the summary after adding/removing items
}

// Function to add item to the cart
function addToCart(item) {
    let cartItems = JSON.parse(sessionStorage.getItem('cart')) || [];
    let existingItemIndex = cartItems.findIndex(cartItem => cartItem.id === item.id);

    if (existingItemIndex >= 0) {
        // If item already in cart, increase quantity
        cartItems[existingItemIndex].quantity += item.quantity;
    } else {
        // If item is not in cart, add it
        cartItems.push(item);
    }

    // Save updated cart to sessionStorage
    sessionStorage.setItem('cart', JSON.stringify(cartItems));

    // Update the cart display
    updateCartItems();
}

// Function to remove item from cart
function removeItem(index) {
    let cartItems = JSON.parse(sessionStorage.getItem('cart')) || [];
    cartItems.splice(index, 1); // Remove the item from the array

    // Save updated cart to sessionStorage
    sessionStorage.setItem('cart', JSON.stringify(cartItems));

    // Update the cart display
    updateCartItems();
}

// Function to update item quantity
function updateQuantity(index, delta) {
    let cartItems = JSON.parse(sessionStorage.getItem('cart')) || [];
    if (cartItems[index].quantity + delta > 0) {
        cartItems[index].quantity += delta;
        sessionStorage.setItem('cart', JSON.stringify(cartItems));
        updateCartItems();
    }
}

// Function to change item quantity directly
function changeQuantity(index, value) {
    let cartItems = JSON.parse(sessionStorage.getItem('cart')) || [];
    let newQuantity = parseInt(value);

    if (newQuantity > 0) {
        cartItems[index].quantity = newQuantity;
        sessionStorage.setItem('cart', JSON.stringify(cartItems));
        updateCartItems();
    }
}

// Initialize the cart display when the page loads
document.addEventListener('DOMContentLoaded', function () {
    updateCartItems();
});
