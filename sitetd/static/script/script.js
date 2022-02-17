console.log('privet')
let xhr = new XMLHttpRequest();
let countCon = 0;
function checkPassword() {
    console.log(123);
    const val = document.getElementById('id_password').value;
    const confimval = document.getElementById('id_password2').value;
    if ( val&&confimval&& val!=confimval) {
        if (!document.getElementById("textPassword")) {
            const div = document.createElement("div");
            div.innerText = "Password mismatch";
            div.classList.add("text-center","text-danger");
            div.setAttribute('id','textPassword')
            document.getElementById("id_passwordText").appendChild(div);
        }
    } else if ( val&&confimval&& val==confimval && document.getElementById("textPassword")) {
        document.getElementById("textPassword").remove();
    }
    }


function createObject() {
    let status = JSON.parse(xhr.responseText)['status'];
    console.log(status);
    console.log(countCon);

    if ( status ) {
         if (document.getElementById('textCheckUser')) {
            document.getElementById('textCheckUser').remove();
        }
        const div = document.createElement("div");
        div.innerText = "username free";
        div.classList.add("text-center","text-danger");
        div.setAttribute('id','textCheckUser')
        document.querySelector(".form-outline").appendChild(div);
    } else if (status === false ) {
        if (document.getElementById('textCheckUser')) {
            document.getElementById('textCheckUser').remove();
        }
        const div = document.createElement("div");
        div.innerText = "username not free";
        div.classList.add("text-center","text-danger");
        div.setAttribute('id','textCheckUser')
        document.querySelector(".form-outline").appendChild(div);
    } else if ( countCon < 3 ) {
        countCon +=1;
        console.log('count');
        setTimeout(createObject, 400);
    } else {
        count = 0;
    }
}


function checkUserName() {

    username = document.getElementById("id_username").value;
    console.log(username);
    let csrfname = document.querySelector('.form-horizontal>input').value;
    if (username) {
        xhr.open("POST",'/register/checkuser', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({'username':username}, null, '\t'));
        setTimeout(createObject, 400);
    }
}
