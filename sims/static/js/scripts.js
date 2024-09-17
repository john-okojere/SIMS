// Mobile Menu Toggle
document.addEventListener("DOMContentLoaded", function () {
    const nav = document.querySelector('nav ul');
    const menuToggle = document.createElement('button');
    menuToggle.textContent = "Menu";
    menuToggle.classList.add("menu-toggle");
    
    menuToggle.addEventListener('click', function () {
        nav.classList.toggle('active');
    });

    document.querySelector('nav').appendChild(menuToggle);
});

// Smooth Scrolling for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
