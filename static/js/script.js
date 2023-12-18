/**
 * Detect when user scrolls past 400px and shrink the logo
 */
window.addEventListener('scroll', function () {
    let scrollPos = window.scrollY;
    let logo = document.getElementById("logo");
    if (scrollPos > 400) {        
        logo.src = "https://res.cloudinary.com/dkxdppkpe/image/upload/v1702568243/logo-sml_osf1ph_zcoipv.webp";
    } else {
        logo.src = "https://res.cloudinary.com/dkxdppkpe/image/upload/v1702568243/logo_sqdz3b_tv5b3l.webp";
    }
});

/** 
 * Set timeout function to close alert after 3 seconds
 * Credit: Code Insitute course content
 */
setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    if (messages) {
        alert.close();
    }
}, 3000);

