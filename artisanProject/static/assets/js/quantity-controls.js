document.addEventListener('DOMContentLoaded', function () {
    const quantityControls = document.querySelectorAll('.quantity-controls');

    quantityControls.forEach(quantityControl => {
        const minusButton = quantityControl.querySelector('.quantity-btn:first-child');
        const plusButton = quantityControl.querySelector('.quantity-btn:last-child');
        const inputField = quantityControl.querySelector('.quantity-input');

        // Check if elements are found
        console.log("Minus Button:", minusButton);
        console.log("Plus Button:", plusButton);
        console.log("Input Field:", inputField);

        minusButton.addEventListener('click', () => {
            let value = parseInt(inputField.value, 10);
            if (value > 1) {
                inputField.value = value - 1;
            }
            console.log("Minus clicked, new value:", inputField.value);
        });

        plusButton.addEventListener('click', () => {
            let value = parseInt(inputField.value, 10);
            inputField.value = value + 1;
            console.log("Plus clicked, new value:", inputField.value);
        });
    });
});
