// JavaScript code
document.addEventListener("DOMContentLoaded", function () {
    // Get the popup element and the buttons for opening and closing it
    const popup = document.getElementById("popup");
    const openButton = document.getElementById("openPopup");
    const closeButton = document.getElementById("closePopup");
  
    // Function to open the popup
    function openPopup() {
      popup.style.display = "block";
    }
  
    // Function to close the popup
    function closePopup() {
      popup.style.display = "none";
    }
  
    // Event listener to open the popup when the button is clicked
    openButton.addEventListener("click", openPopup);
  
    // Event listener to close the popup when the close button is clicked
    closeButton.addEventListener("click", closePopup);
  });

  // Event listener to open the popup when the form is submitted
document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent the default form submission behavior
    openPopup(); // Open the popup
  });
  
  <script src="../static/js/popup.js"></script>