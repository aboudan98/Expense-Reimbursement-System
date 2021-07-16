async function send_user_info(){
//    let url = 'http://localhost:5000/login'
//    let response = await fetch(url)
//    // Remember fetch returns a response object, not the direct response body
//    let data = await response.json()
    let field = document.getElementById('username').value
    console.log(field)

    console.log("after")
}

submit_button = document.getElementById('submit-button')
submit_button.onclick=() => {
    this.send_user_info()
}

