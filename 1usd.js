const express = require("express");

const app = express();

app.get("/convert", (req, res) => {

    const rupees = parseFloat(req.query.inr);

    if (!rupees) {
        return res.status(400).json({ error: "Invalid amount" });
    }

    const usd = rupees / 75;

    res.json({
        rupees: rupees,
        dollars: usd.toFixed(2)
    });

});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});