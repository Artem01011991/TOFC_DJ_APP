let xhttp = new XMLHttpRequest();

function configControlCondition() {
    xhttp.onreadystatechange = function f(){
        if (this.readyState == 4 && this.status == 200){
            let elems = [].slice.call(document.querySelectorAll('[id$=_control]'));
            let response = JSON.parse(xhttp.responseText);
            document.write(response.index_act_mode);
        }
    };

    xhttp.open('GET', window.location.protocol + '/rest/config-current-state', true);
    xhttp.send();

    // if(enebling){
    //     elem.checked = true;
    // }
    // else if(!enebling){
    //     elem.checked = false;
    // }
}

function djangoControlChangeCondition() {
    let elem = document.getElementById("dj_control");
    let answer = window.confirm('Change value to: "' + elem.checked + '"');

    if (answer) {
        xhttp.open("GET", window.location.protocol + "/rest?" + elem.id + "=" + elem.checked, true);
        xhttp.send();
    }
    else {
        location.reload()
    }
}
