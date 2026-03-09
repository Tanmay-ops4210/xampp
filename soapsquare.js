const express = require("express");

var app = express();


app.get("/square/:num", function (req, res) {

    const num = req.params.num;

    const result = parseInt(num) * parseInt(num);

    res.json({ result: result });
});

// Run server
app.listen(3300, function () {
    console.log("Server running on port 3300");
    console.log("http://localhost:3300/square/5");
});