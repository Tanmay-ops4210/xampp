const express = require("express");
const app = express();

app.get("/temperature", (req, res) => {

    const f = parseFloat(req.query.f);

    if (isNaN(f)) {
        return res.status(400).json({ error: "Invalid input" });
    }

    const c = (f - 32) * 5 / 9;

    res.json({
        fahrenheit: f,
        celsius: c.toFixed(2)
    });

});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});