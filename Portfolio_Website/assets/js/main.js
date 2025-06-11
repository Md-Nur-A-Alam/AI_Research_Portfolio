// Main JS for Navbar Toggle (Mobile)

document.addEventListener('DOMContentLoaded', () => {
  const navbar = document.querySelector('.navbar');
  const toggleBtn = document.querySelector('.menu-toggle');
  toggleBtn?.addEventListener('click', () => {
    navbar.classList.toggle('active');
  });
});