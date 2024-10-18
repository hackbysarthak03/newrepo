const navBtn = document.querySelector('.navbar-mobile-btn')
const navHeader = document.querySelector('.header')
const body = document.body

function toggleNavbar() {
    navHeader.classList.toggle('active')
    body.classList.toggle('no-scroll')
}

navBtn.addEventListener('click', () => toggleNavbar());

function changeToLoading() {
    document.getElementById('saveBtn').style.display = 'none'
    document.getElementById('loadingBtn').style.display = 'flex'
}

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


const checkboxes = document.querySelectorAll('.checkbox-input')
const checkbox_text = document.querySelectorAll('.checkbox-label')

checkboxes.forEach((checkbox, index) => {
    checkbox.addEventListener('change', function() {
        if (checkbox.checked) {
            checkbox_text[index].style.color = '#1e85f0';  // Change this to the color you want
        } else {
            checkbox_text[index].style.color = '#535353';  // Change this back to default
        }
    });
});

const changeStatus = document.querySelector('#change-status')
changeStatus.addEventListener('click', function () {
    window.location.href = "/profile/updateStatus?status=200";
})

const manageBlogs = document.querySelector('#manage-blogs')
manageBlogs.addEventListener('click', function () {
    window.location.href = "/profile/updateStatus?status=100";
})

const liveCall = document.querySelector('#live-call')
liveCall.addEventListener('click', function () {
    window.location.href = "/profile/updateStatus?status=300";
})