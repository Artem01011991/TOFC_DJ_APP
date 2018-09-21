let xhttp = new XMLHttpRequest();

function requestConfigValue(elems) {
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
            setConfigValue(JSON.parse(this.responseText), elems);
        }
    };

    xhttp.open('GET', window.location.protocol + '/rest/config-current-state', true);
    xhttp.send();
}

function setConfigValue(id_value_json, elems) {
    for(i = 0; i < elems.length; i++) {
        if(id_value_json[elems[i].id] == 'true') {
            elems[i].checked = true;
        }
        else {
            elems[i].checked = false;
        }
    }
}

function changeConfigValue(elem) {
    let answer = window.confirm('Change value to: "' + elem.checked + '"');

    if (answer) {
        xhttp.open("GET", window.location.protocol + "/rest?id=" + elem.id + "&value=" + elem.checked, true);
        xhttp.send();
    }
    else {
        requestConfigValue([elem]);
    }
}
