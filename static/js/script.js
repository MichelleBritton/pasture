/**
 * Detect when user scrolls past 400px and shrink the logo
 */
window.addEventListener('scroll', function () {
    let scrollPos = window.scrollY;
    let logo = document.getElementById("logo");
    if (scrollPos > 400) {        
        logo.src = "https://res.cloudinary.com/dkxdppkpe/image/upload/v1701105881/logo-sml_osf1ph.webp";
    } else {
        logo.src = "https://res.cloudinary.com/dkxdppkpe/image/upload/v1701084882/logo_sqdz3b.webp";
    }
});