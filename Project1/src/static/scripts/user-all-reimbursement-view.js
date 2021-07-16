var arrHead = new Array();
arrHead = ['ID', 'Amount', 'Reason', 'Status', 'User ID']; // table headers.

home_button = document.getElementById('home-button')
home_button.onclick=() => {
    window.location.replace("user-home-view.html")
}

sign_out = document.getElementById('sign-out-button')
sign_out.onclick=() => {
    window.location.replace("login.html")
}

let reimbursementTable
// first create a TABLE structure by adding few headers.
function createTable() {
    reimbursementTable = document.createElement('table');
    reimbursementTable.setAttribute('id', 'reimbursementTable');  // table id.

    var tr = reimbursementTable.insertRow(-1);

    for (var h = 0; h < arrHead.length; h++) {
        var th = document.createElement('th'); // the header object.
        th.innerHTML = arrHead[h];
        tr.appendChild(th);
    }

    var div = document.getElementById('cont');
    div.appendChild(reimbursementTable);    // add table to a container.
}

async function addItem(){
    let url = 'http://localhost:5000/users/reimbursements'
    let response = await fetch(url)
    // Remember fetch returns a response object, not the direct response body
    let data = await response.json()

    var reimbursementTable = document.getElementById('reimbursementTable');

    var rowCnt = reimbursementTable.rows.length;
    var tr = reimbursementTable.insertRow(rowCnt);
    tr = reimbursementTable.insertRow(rowCnt);


    let count = 0
    let count2 = 0
    for(let item in data){
        console.log("item: " + item)
        count=0;
        console.log(data[item])
        for(let element in data[item]){
            console.log('element: ' + element)
            var td = document.createElement('td');
            td.setAttribute('id', 'td')
            td = tr.insertCell(count);
            let item_to_add = data[item]
            let ol = document.createElement("text");
            ol.setAttribute('id',(data[item])[element]);
            ol.appendChild(document.createTextNode((data[item])[element]));
            td.appendChild(ol);
            count+=1
        }
        count2+=1
        tr = reimbursementTable.insertRow(count2);
    }

    console.log('hello')
}



window.onload = function () {
    this.createTable()
    this.addItem()
}