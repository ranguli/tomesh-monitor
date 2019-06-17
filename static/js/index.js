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
                elem.innerText = newInfo.ip;
            }
        }
    }
}


window.onload = function() {
    document.getElementById("restart").onclick = function() {
        window.location.reload();
    };
};

setInterval(update, 3000);
