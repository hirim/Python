function led1_on(){
    fetch("/led1/on")
        .then(response=> response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result");
            if (data == "ok") {
                result.innerHTML = "<h1> LED 1 is running </h1>";
            }
            else {
                result.innerHTML = "<h1> error </h1>";
            }
        });
}

function led1_off(){
    fetch("/led1/off")
        .then(response=> response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result");
            if (data == "ok") {
                result.innerHTML = "<h1> LED 1 is stopping </h1>";
            }
            else {
                result.innerHTML = "<h1> error </h1>";
            }
        });
}

function led2_on(){
    fetch("/led2/on")
        .then(response=> response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result");
            if (data == "ok") {
                result.innerHTML = "<h1> LED 2 is running </h1>";
            }
            else {
                result.innerHTML = "<h1> error </h1>";
            }
        });
}
function led2_off(){
    fetch("/led2/off")
        .then(response=> response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result");
            if (data == "ok") {
                result.innerHTML = "<h1> LED 2 is stopping </h1>";
            }
            else {
                result.innerHTML = "<h1> error </h1>";
            }
        });
}