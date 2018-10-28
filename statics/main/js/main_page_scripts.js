let xhttp = new XMLHttpRequest();

function setStateOfConfigElements(elem, state) {
    elem.checked = state;
    elem.parentElement.style.background = state?'#66ff99':'unset';
}

function setAccessabilityOfElements(elem_id, dj_dis) {
    let elems_ids = JSON.parse(document.getElementById('elems_ids').textContent);

    if(elem_id == elems_ids['django']){
        let elems = [document.getElementById(elems_ids['binance']), document.getElementById(elems_ids['index'])];
        dj_dis = true;

        for (i in elems){
            elems[i].parentElement.parentElement.style.opacity = '0.5';
            elems[i].parentElement.style.cursor = 'not-allowed';
            elems[i].parentElement.classList.remove('config-hover');
            elems[i].disabled = true;
        }
    }
    // else{
    //     let elem = document.getElementById(elem_id);
    //     elem.nextSibling.style.opacity = '0.5';
    // }

    return dj_dis
}

function requestConfigValue(url) {
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
            let elems_state = JSON.parse(this.responseText);
            let dj_disabled = false; // Prevent calling once more setAccessabilityOfElements if django control off

            for(i in elems_state) {
                setStateOfConfigElements(document.getElementById(i), elems_state[i] === 'true');

                if(elems_state[i] === 'false' && !dj_disabled){
                    dj_disabled = setAccessabilityOfElements(i, dj_disabled);
                }
            }
        }
    };

    xhttp.open('GET', window.location.protocol + url, true);
    xhttp.send();
}

function changeConfigValue(elem) {
    let answer = window.confirm('Change value to: "' + elem.checked + '"');

    if (answer) {
        xhttp.open('POST', window.location.protocol + '/rest/', true);
        xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhttp.send('id=' + elem.id + '&value=' + elem.checked);

        setStateOfConfigElements(elem, elem.checked);
    }
    else {
        setStateOfConfigElements(elem, elem.checked != true);
    }
}
