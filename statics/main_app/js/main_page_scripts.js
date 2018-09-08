function djangoControlCondition(enebling) {
    let elem = document.getElementById("dj_control");

    if(enebling){
        elem.checked = true;
    }
    else if(!enebling){
        elem.checked = false;
    }
}

function djangoControlChangeCondition() {
    let elem = document.getElementById("dj_control");
    let answer = window.confirm('Change value to: "' + elem.checked + '"');

    if (answer) {
        let xhttp = new XMLHttpRequest();
        xhttp.open("GET", window.location.protocol + "/rest?" + elem.id + "=" + elem.checked, true);
        xhttp.send();
    }
    else {
        location.reload()
    }
}
