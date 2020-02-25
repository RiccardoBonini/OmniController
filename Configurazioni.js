var port=256;
var IP= 'ws://192.168.43.209:';
var url = IP + port.toString();
const MySocket = new WebSocket(url);//alternative socket 'ws://172.18.82.53:255'

function driveModeCar() {

    var msg = {
        M:"1"
    };
    if(MySocket.readyState == 1) {

        MySocket.send(JSON.stringify(msg));
        port ++;
    }

}

function driveModeSteam() {

    var msg = {
        M:"2"
    };
    if(MySocket.readyState == 1) {

        MySocket.send(JSON.stringify(msg));
        port ++;
    }

}

function cookingModeCar(){

    var msg = {
        M: "3"
    };
    if(MySocket.readyState == 1) {
        MySocket.send(JSON.stringify(msg));
    }

}

function cookingModeSteam(){

    var msg = {
        M: "4"
    };
    if(MySocket.readyState == 1) {
        MySocket.send(JSON.stringify(msg));
    }

}

function reverseDriveModeCar(){

    var msg = {
        M: "5"
    };
    if(MySocket.readyState == 1) {
        MySocket.send(JSON.stringify(msg));
    }

}

function reverseDriveModeSteam(){

    var msg = {
        M: "6"
    };
    if(MySocket.readyState == 1) {
        MySocket.send(JSON.stringify(msg));
    }

}

function openMode(evt, Mode) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(Mode).style.display = "block";
    evt.currentTarget.className += " active";
}