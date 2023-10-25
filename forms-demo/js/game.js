let fname = ""

function greet() {
    let greetParagraph = document.getElementById("greet");
    // get values from the form
    fname = document.getElementById("fname").value;
    let lname = document.getElementById("lname").value;
    let age = document.getElementById("age").value;
    //show the results
    greetParagraph.innerHTML = "Greetings, " + age + " year old " + fname + " " + lname + "!";

}

function trivia() {
    let triviaAnswer = document.getElementById("trivia-answer");

    let chocolateSelected = document.getElementById("chocolate").checked;
    let tunaSelected = document.getElementById("tuna").checked;
    let honeySelected = document.getElementById("honey").checked;

    if (chocolateSelected) {
        triviaAnswer.innerHTML = fname + ", that is not the correct answer. Try again."
    } else if (tunaSelected) {
        triviaAnswer.innerHTML = fname + ", that is not the correct answer. Try again."
    } else {
        triviaAnswer.innerHTML = fname + ", you are correct."
    }

}

function ttl() {
    let ttlAnswer = document.getElementById("ttl-answer");

    let truth1Selected = document.getElementById("truth1").checked;
    let truth2Selected = document.getElementById("truth2").checked;
    let lieSelected = document.getElementById("lie").checked;

    if (truth1Selected) {
        ttlAnswer.innerHTML = fname + ", I can roll my tongue. Try again."
    } else if (truth2Selected) {
        ttlAnswer.innerHTML = fname + ", it's a lot of boba, but it's true. Try again."
    } else {
        ttlAnswer.innerHTML = fname + ", you are correct. I don't have perfect pitch, but it would be neat if I did."
    }

}