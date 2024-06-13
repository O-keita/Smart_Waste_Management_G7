document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.getElementById("menu"); // Replace with the actual ID or class of your menu icon
  const sidebar = document.getElementById("user-sidebar");

  menuIcon.addEventListener("click", function () {
    sidebar.classList.toggle("sidebar-hidden"); // Toggle the CSS class to hide/show the sidebar
  });
});
