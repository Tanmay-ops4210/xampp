const express = require("express");

const app = express();

// Web Service Endpoint
app.get("/factorial", (req, res) => {

    const num = parseInt(req.query.n);

    if (isNaN(num) || num < 0) {
        return res.status(400).json({
            error: "Please provide a valid positive number"
        });
    }

    let factorial = 1;

    for (let i = 1; i <= num; i++) {
        factorial *= i;
    }

    res.json({
        number: num,
        factorial: factorial
    });

});

const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`Test URL: http://localhost:3000/factorial?n=5`);
});