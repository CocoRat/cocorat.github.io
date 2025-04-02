// server.js
// where your node app starts

// init project
const express = require("express");
const app = express();
const messages = [{ "name": "John Doe", "age": 20 }];

// we've started you off with Express,
// but feel free to use whatever libs or frameworks you'd like through `package.json`.

// http://expressjs.com/en/starter/static-files.html
app.use(express.static("public"));
app.use(express.json())

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (request, response) {
    response.sendFile(__dirname + "/index.html");
});

app.post('/messages', (req, res) => {
    const newMessage = req.body.text; //assuming the client sends an object with a "text" field

    if (newMessage) {
        messages.push(newMessage);
        res.status(201).json({ success: true })
    }
    else {
        res.status(400).json({ success: false, error: "No text provided" })
    }
})

// get request comes to the path messages
app.get("/messages", (req, res) => {
    res.json(messages);
})

// listen for requests :)
const listener = app.listen(process.env.PORT, function () {
    console.log("Your app is listening on port " + listener.address().port);
});


