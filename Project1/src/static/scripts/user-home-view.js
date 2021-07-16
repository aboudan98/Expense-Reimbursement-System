new_request = document.getElementById('new-reimbursement-button')
new_request.onclick=() => {
    window.location.replace("user-reimbursement-view.html")
}

view_all = document.getElementById('view-reimbursements-button')
view_all.onclick=() => {
    window.location.replace("user-all-reimbursement-requests.html")
}

async function get_user(){
    let url = 'http://localhost:5000/login-user-info'
    let response = await fetch(url)
    // Remember fetch returns a response object, not the direct response body
    let data = await response.json()
    field = document.getElementById('welcome-user')
    field.value = 'Welcome, ' + data['_user_username'] + '!'
}


sign_out = document.getElementById('sign-out-button')
sign_out.onclick=() => {
    window.location.replace("login.html")
}

window.onload = function () {
    this.get_user()
}