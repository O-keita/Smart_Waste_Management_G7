document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.getElementById("menu"); // Replace with the actual ID or class of your menu icon
  const sidebar = document.getElementById("user-sidebar");
  const messageContainer = document.getElementById("flash-message");

  menuIcon.addEventListener("click", function () {
    sidebar.classList.toggle("sidebar-hidden");
  });

  setTimeout(function () {
    messageContainer.style.display = "none";
  }, 3000);
});
