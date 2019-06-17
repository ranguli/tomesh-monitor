async function update() {
    const updatedInterfaces = await (await fetch('interfaces')).json();
    const currentInterfaceElements = [...document.getElementById('adapters').childNodes[1].childNodes].filter((elm) => elm.tagName === 'TR');

    for (const interface of currentInterfaceElements) {
        const newInfo = updatedInterfaces.filter((inter) => inter.name === interface.id.split('_')[1])[0];
        for (const elem of interface.childNodes) {
            if (elem.tagName === 'TH') {
                elem.className = `status_${newInfo.status}`
            }
            else if (elem.tagName === 'TD') {
                elem.innerText = newInfo.ipv4;
            }
        }
    }
}


window.onload = function() {

    // Restart button
    document.getElementById("restart").onclick = function() {
        window.location.reload();
    };

    // Clock 
    clock();  
    function clock() {
        var now = new Date();
        var TwentyFourHour = now.getHours();
        var hour = now.getHours();
        var min = now.getMinutes();
        var mid = 'PM';
        if (min < 10) {
            min = "0" + min;
        }
        if (hour > 12) {
            hour = hour - 12;
        }    
        if(hour==0){ 
            hour=12;
        }
        if(TwentyFourHour < 12) {
            mid = 'AM';
        } 
        document.getElementById('time').innerHTML = hour+':'+min+''+mid;
        setTimeout(clock, 1000);
    }
}

setInterval(update, 3000);