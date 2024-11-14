// views.js

// Wait for the document to load before applying any styles
document.addEventListener("DOMContentLoaded", function() {
    // Check if there's a saved view preference in localStorage
    const viewPreference = localStorage.getItem("viewPreference");
    
    // Apply saved preference or default to grid view
    if (viewPreference === "list") {
        setListView();
    } else {
        setGridView();
    }
});

function setGridView() {
    const productContainer = document.querySelector(".product-container");
    productContainer.classList.remove("list");
    productContainer.classList.add("grid"); // Apply grid view

    // Update icon styles (optional)
    document.getElementById("gridViewIcon").classList.add("active");
    document.getElementById("listViewIcon").classList.remove("active");

    // Save preference
    localStorage.setItem("viewPreference", "grid");
}

function setListView() {
    const productContainer = document.querySelector(".product-container");
    productContainer.classList.remove("grid");
    productContainer.classList.add("list"); // Apply list view

    // Update icon styles (optional)
    document.getElementById("gridViewIcon").classList.remove("active");
    document.getElementById("listViewIcon").classList.add("active");

    // Save preference
    localStorage.setItem("viewPreference", "list");
}
