function updateInterfaces(interfaces){
    console.log("Interfaces updated");
    // Update the interface options
    let interface1Select = document.getElementById("interface1");
    let interface2Select = document.getElementById("interface2");
    interface1Select.innerHTML = "";
    interface2Select.innerHTML = "";
    interfaces.forEach(interface => {
        let option = document.createElement("option");
        option.value = interface;
        option.text = interface;
        interface1Select.add(option.cloneNode(true));
        interface2Select.add(option);
    });
}
function sendSignal(event) {
    let interface1Select = document.getElementById("interface1");
    let interface2Select = document.getElementById("interface2");
    let interface1Value = interface1Select.options[interface1Select.selectedIndex].value;
    let interface2Value = interface2Select.options[interface2Select.selectedIndex].value;
    fetch("/events", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "event": String(event),
            "interface1": interface1Value,
            "interface2": interface2Value
        })
    })
    .then(response => response.json())
    .then(data => {
       if (data.interfaces){
            updateInterfaces(data.interfaces);
        }
    })
    .catch(error => console.error(error));
}
function resetPortInfo(port) {
    let portElement = document.getElementsByClassName("packageAnalysis--content--" + port)[0];
    const textareas = portElement.querySelectorAll('.inOutInput:nth-child(2n-1)');
    const value1Textareas = textareas[0]
    const value2Textareas = textareas[1]
    value1Textareas.value = "";
    value2Textareas.value = "";
}
function clearMAC() {
    const macTableElement = document.getElementsByClassName("packageAnalysis--content--center")[0];
    const macTableTextareas = macTableElement.querySelectorAll('.inOutTextarea');
    const macTableTextarea = macTableTextareas[0];
    macTableTextarea.value = "";
}
function pushNewTimer() {
    const pushNumber = document.getElementById("pushNumber").value;
    console.log(pushNumber);
    fetch("/timer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "timer": pushNumber
        })
    })
    .then(response => response.json())
    .then(data => { console.log(data) })
    .catch(error => console.error(error));
}