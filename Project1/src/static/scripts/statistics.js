
home_button = document.getElementById('home-button')
home_button.onclick=() => {
    window.location.replace("manager-home-view.html")
}

sign_out = document.getElementById('sign-out-button')
sign_out.onclick=() => {
    window.location.replace("login.html")
}

async function get_most_requests(){
    let url = 'http://localhost:5000/most-requests'
    let response = await fetch(url)
    // Remember fetch returns a response object, not the direct response body
    let data = await response.json()
    field = document.getElementById('most-requests')
    field.style.width="400px"
    field.value = 'Most requests were made by ' + data['max_user'] + ' at ' + data['max_requests'] + ' requests'
}

async function get_most_spent(){
    let url = 'http://localhost:5000/most-spent'
    let response = await fetch(url)
    // Remember fetch returns a response object, not the direct response body
    let data = await response.json()
    field = document.getElementById('most-spent')
    field.style.width="400px"
    field.value = 'Most reimbursement amount was made from ' + data['max_user'] + ' at ' + data['max_spent']
}

window.onload = function () {
    this.get_most_requests()
    this.get_most_spent()
}