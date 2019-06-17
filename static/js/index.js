async function updateInterfaces() {
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

function clock() {
    document.getElementById('time').innerHTML = new Date().toLocaleString('en-US', {hour: 'numeric', minute: 'numeric', hour12: true});
}

window.onload = () => {
    document.getElementById("restart").onclick = () => window.location.reload();

    setInterval(clock, 1000);
    setInterval(updateInterfaces, 3000);
    clock();
}
