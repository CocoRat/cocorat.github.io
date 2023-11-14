
function thank() {
    let thankParagraph = document.getElementById("thank");
    // get values from the form
    let firstName = document.getElementById("firstName").value;
    let lastName = document.getElementById("lastName").value;
    //show the results
    thankParagraph.innerHTML = "Thank you for your message, " + firstName + " " + lastName + "!";

}