const express = require("express");

const app = express();

// Prime number API
app.get("/prime", (req, res) => {

    const num = parseInt(req.query.n);

    if (isNaN(num) || num < 1) {
        return res.status(400).json({
            error: "Please provide a valid positive number"
        });
    }

    let isPrime = true;

    if (num === 1) {
        isPrime = false;
    } else {
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                isPrime = false;
                break;
            }
        }
    }

    res.json({
        number: num,
        prime: isPrime
    });

});

const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`Test URL: http://localhost:3000/prime?n=2`);
});