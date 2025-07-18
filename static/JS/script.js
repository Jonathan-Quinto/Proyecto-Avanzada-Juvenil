document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll("nav ul li a");

    window.addEventListener("scroll", function () {
        let fromTop = window.scrollY;

        navLinks.forEach(link => {
            let section = document.querySelector(link.getAttribute("href"));
            if (
                section.offsetTop <= fromTop &&
                section.offsetTop + section.offsetHeight > fromTop
            ) {
                link.style.color = "#151922";
            } else {
                link.style.color = "white";
            }
        });
    });
});
