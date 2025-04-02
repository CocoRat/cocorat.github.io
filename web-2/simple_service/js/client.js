const names = [
    "John Doe, age 40"
];

const namesList = document.getElementById("names");
const dataForm = document.forms[0];
const formInputFname = dataForm.elements["fname"];
const formInputLname = dataForm.elements["lname"];
const formInputAge = dataForm.elements["age"];

const appendNewName = function (name) {
    const newName = document.createElement("li");
    newName.innerHTML = name;
    namesList.appendChild(newName);
};

names.forEach(function (name) {
    appendNewName(name);
})

dataForm.onsubmit = function (event) {
    event.preventDefault();
    names.push(formInputFname.value + " " + formInputLname.value + ", age " + formInputAge.value);
    appendNewName(formInputFname.value + " " + formInputLname.value + ", age " + formInputAge.value);
}
