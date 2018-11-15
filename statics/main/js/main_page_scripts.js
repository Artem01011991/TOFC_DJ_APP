let xhttp = new XMLHttpRequest();

function setAccessabilityOfElements(elem_id, state) {
    if(elem_id === 'dj'){
        let elems = [document.getElementById('bin'), document.getElementById('ind')],
            dj_elem = document.getElementById(elem_id);

        dj_elem.checked = state;
        dj_elem.parentElement.style.background = state?'#66ff99':'unset';

        for (i in elems){
            elems[i].parentElement.style.opacity = state?'unset':'0.5';
            elems[i].parentElement.style.cursor = state?'pointer':'not-allowed';

            // The hover class removing
            if(!state){
                elems[i].parentElement.classList.remove('config-hover');
            }
            else {
                elems[i].parentElement.classList.add('config-hover');
            }

            elems[i].disabled = !state;
        }
    }
    else{
        let elem = document.getElementById(elem_id);
        elem.parentElement.style.background = state?'#66ff99':'unset';
        elem.parentElement.nextElementSibling.style.opacity = state?'unset':'0.5';
    }
}

function requestConfigValue(url) {
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
            let elems_state = JSON.parse(this.responseText);

            // Elements state changing
            for(i in elems_state) {
                setAccessabilityOfElements(i, elems_state[i] === 'true');
            }
        }
    };

    xhttp.open('GET', window.location.protocol + url, true);
    xhttp.send();
}

function changeConfigValue(elem) {
    let answer = window.confirm('Change value to: "' + elem.checked + '"');

    // Changing configuration
    if (answer) {
        xhttp.open('POST', window.location.protocol + '/rest/', true);
        xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhttp.send('id=' + elem.id + '&value=' + elem.checked);

        setAccessabilityOfElements(elem.id, elem.checked);
    }
    else {
        setAccessabilityOfElements(elem.id, elem.checked != true);
    }
}
