document.addEventListener("DOMContentLoaded", function() {
    const showText = document.querySelectorAll("#showText"); // Select all elements with the class "showText"
    const hiddenDiv = document.getElementById("hiddenDiv");
    let isVisible = false;

    showText.forEach(function(showText) {
        showText.addEventListener("click", function() {
            if (isVisible) {
                hiddenDiv.style.display = "none"; // Hide the div if it's currently visible
            } else {
                hiddenDiv.style.display = "block"; // Show the div if it's currently hidden
            }
            isVisible = !isVisible; // Toggle the visibility flag
        });
    });
});
