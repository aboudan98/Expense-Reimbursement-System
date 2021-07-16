statistics = document.getElementById('view-statistics-button')
statistics.onclick=() => {
    window.location.replace("statistics.html")
}

view_all = document.getElementById('view-reimbursements-button')
view_all.onclick=() => {
    window.location.replace("manager-reimbursement-view.html")
}

async function get_user(){
    let url = 'http://localhost:5000/login-user-info'
    let response = await fetch(url)
    // Remember fetch returns a response object, not the direct response body
    let data = await response.json()
    console.log(data['_manager_username'])
    field = document.getElementById('welcome-manager')
    field.value = 'Welcome, ' + data['_manager_username'] + '!'
}


sign_out = document.getElementById('sign-out-button')
sign_out.onclick=() => {
    window.location.replace("login.html")
}

window.onload = function () {
    this.get_user()
}