document.addEventListener("DOMContentLoaded", () => {
    const names = [
        "John Doe, age 40"
    ];


    const namesList = document.getElementById("names");


    const appendNewName = function (name) {
        const newName = document.createElement("li");
        newName.innerHTML = name;
        namesList.appendChild(newName);
    };

    names.forEach(function (name) {
        appendNewName(name);
    })
    const dataForm = document.forms[0];
    dataForm.onsubmit = function (event) {

        event.preventDefault(); //ptevents page from loading

        const formData = {
            firstname: dataForm.elements["fname"].value,
            lastname: dataForm.elements["lname"].value,
            age: dataForm.elements["age"].value
        };

        fetch("https://quiet-diligent-seed.glitch.me/submissions", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })

            .then(response => response.json())
            .then(data => {
                console.log("Success:", data)
                dataForm.reset()
            })
            .catch(error => {
                console.error("Error:", error);
            });

        names.push(document.getElementById("fname").value + " " + ", age ");
        appendNewName(document.getElementById("fname").value);
    }

});