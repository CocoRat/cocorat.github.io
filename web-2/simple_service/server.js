// server.js
// where your node app starts

// init project
const express = require("express");
const app = express();

//n-memory data store
let submissions = [];

// we've started you off with Express,
// but feel free to use whatever libs or frameworks you'd like through `package.json`.

// http://expressjs.com/en/starter/static-files.html
app.use(express.static("public"));
app.use(express.json())

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (request, response) {
    response.sendFile(__dirname + "/index.html");
});

app.get("/display", function (request, response) {
    response.sendFile(__dirname + "/display.html")
});

app.put('/submissions', (req, res) => {
    const newData = req.body; //assuming the client sends an object with a "text" field

    if (newData) {
        submissions.push(newData);
        res.status(201).json({ success: true })
    }
    else {
        res.status(400).json({ success: false, error: "No text provided" })
    }
});

// get request comes to the path messages
app.get("/submissions", (req, res) => {
    res.json(submissions);
})

// listen for requests :)
const listener = app.listen(process.env.PORT, function () {
    console.log("Your app is listening on port " + listener.address().port);
});


