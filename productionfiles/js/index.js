const navBtn = document.querySelector('.navbar-mobile-btn')
const navHeader = document.querySelector('.header')
const body = document.body

function toggleNavbar(){
    navHeader.classList.toggle('active')
    body.classList.toggle('no-scroll')
}

navBtn.addEventListener('click', () => toggleNavbar());

        

window.addEventListener("load", function () {
    let loadingScreen = document.getElementById("loading-screen");

    // Record the current time when the page finishes loading
    let startTime = new Date().getTime();

    // Ensure at least 3 seconds have passed before hiding the loading screen
    let delay = 3000; // Minimum 3 seconds

    // Calculate how much time has passed since the page loaded
    let timeElapsed = new Date().getTime() - startTime;

    // If the time elapsed is less than 3 seconds, delay hiding the loading screen
    if (timeElapsed < delay) {
        setTimeout(function () {
            loadingScreen.style.display = "none";
        }, delay - timeElapsed); // Wait for the remaining time
    } else {
        loadingScreen.style.display = "none"; // Hide immediately if 3 seconds have already passed
    }
});
    
