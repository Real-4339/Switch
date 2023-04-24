var socket = new WebSocket("ws://" + window.location.host + "/ws");

socket.onopen = function(event) {
    socket.send(JSON.stringify({type: "hello", message: "Hello, server!"}));
};

socket.onmessage = function(event) {
    let data = JSON.parse(event.data);
    if (data.type === "updatePort") {
        updatePort(data.port, data.list);
    } else if (data.type === "updateMacTable") {
        updateMacTable(data.macTable);
    } else if (data.type === "addToMacTable") {
        addToMacTable(data.macTable);
    } else if (data.type === "log") {
        pushLog(data.log);
    }
};

function pushLog(log) {
    const logTextarea = document.getElementById("postResponse");
    logTextarea.value += log + "\n";
}

function addToMacTable(macTable) {
    const macTableElement = document.getElementsByClassName("packageAnalysis--content--center")[0];
    const macTableTextareas = macTableElement.querySelectorAll('.inOutTextarea');
    const macTableTextarea = macTableTextareas[0];
    let value = macTableTextarea.value;
    value += JSON.stringify(macTable) + "\n";
}

function updateMacTable(macTable) {
    const macTableElement = document.getElementsByClassName("packageAnalysis--content--center")[0];
    const macTableTextareas = macTableElement.querySelectorAll('.inOutTextarea');
    const macTableTextarea = macTableTextareas[0];
    macTableTextarea.value = JSON.stringify(macTable);
    
}

function updatePort(port, dict) {
    let portElement;
    let value1Text = "";
    let value2Text = "";
    
    if (port === "port1") {
        portElement = document.getElementsByClassName("packageAnalysis--content--left")[0];
    } else if (port === "port2") {
        portElement = document.getElementsByClassName("packageAnalysis--content--right")[0];
    }
    
    for (const obj of dict[0].value1) {
    value1Text += JSON.stringify(obj) + "\n";
    }

    for (const obj of dict[0].value2) {
    value2Text += JSON.stringify(obj) + "\n";
    }
    

    const textareas = portElement.querySelectorAll('.inOutInput:nth-child(2n-1)');
    const value1Textareas = textareas[0]
    const value2Textareas = textareas[1]

    // Update the textareas
    value1Textareas.value = value1Text;
    value2Textareas.value = value2Text;
}