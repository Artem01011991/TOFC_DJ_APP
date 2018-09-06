function djangoControlCondition(enebling) {
    if(enebling){
        document.getElementById("dj_control").checked = true;
    }
    document.getElementById("dj_control").checked = false;
}

function djangoControlChangeCondition() {
    let elem = document.getElementById("dj_control");
    let xhttp = new XMLHttpRequest();

    xhttp.open("GET", window.location.hostname + ":8000/rest?"+ elem.id + "=" + elem.value, true);
    xhttp.send();
}
