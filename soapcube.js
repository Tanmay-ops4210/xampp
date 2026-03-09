const express = require("express");

var app = express();


app.get("/cube/:num", function (req, res) {

    const num = req.params.num;

    const result = parseInt(num) * parseInt(num) * parseInt(num);

    res.json({ result: result });
});

app.listen(3300, function () {
    console.log("Server running on port 3300");
    console.log("http://localhost:3300/cube/3");
});