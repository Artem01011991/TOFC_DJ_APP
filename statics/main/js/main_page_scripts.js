let xhttp = new XMLHttpRequest();

function setStateOfConfigElements(elem, state) {
    elem.checked = state;
    elem.parentElement.style.background = state?'#66ff99':undefined;
}

function requestConfigValue(url) {
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
            let elems_state = JSON.parse(this.responseText);

            for(i in elems_state) {
                setStateOfConfigElements(document.getElementById(i), elems_state[i] === 'true');
            }
        }
    };

    xhttp.open('GET', window.location.protocol + url, true);
    xhttp.send();
}

function changeConfigValue(elem) {
    let answer = window.confirm('Change value to: "' + elem.checked + '"');

    if (answer) {
        xhttp.open("GET", window.location.protocol + "/rest?id=" + elem.id + "&value=" + elem.checked, true);
        xhttp.send();

        setStateOfConfigElements(elem, elem.checked)
    }
    else {
        setStateOfConfigElements(elem, elem.checked != true);
    }
}
