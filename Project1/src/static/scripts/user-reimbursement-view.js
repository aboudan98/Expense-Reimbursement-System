home_button = document.getElementById('home-button')
home_button.onclick=() => {
    window.location.replace("user-home-view.html")
}

sign_out = document.getElementById('sign-out-button')
sign_out.onclick=() => {
    window.location.replace("login.html")
}