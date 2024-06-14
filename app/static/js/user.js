document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.getElementById("menu"); // Replace with the actual ID or class of your menu icon
  const sidebar = document.getElementById("user-sidebar");
  const messageContainer = document.getElementById("message");

  menuIcon.addEventListener("click", function () {
    sidebar.classList.toggle("sidebar-hidden"); // Toggle the CSS class to hide/show the sidebar
  });

  function showMessage(message) {
    messageContainer.innerText = message;
    messageContainer.style.display = "block";

    setTimeout(function () {
      messageContainer.style.display = "none";
    }, 5000); // Hide the message after 5 seconds
  }
});
