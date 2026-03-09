const express = require("express");
const app = express();

app.get("/multiply", (req, res) => {

const a = parseFloat(req.query.a);
const b = parseFloat(req.query.b);

if (isNaN(a) || isNaN(b)) {
return res.send("Please provide numbers like ?a=5&b=6");
}

const result = a * b;

res.send(`Result: ${result}`);

});

const PORT = 3000;

app.listen(PORT, () => {
console.log(`Server listening on port ${PORT}`);
console.log("http://localhost:3000/multiply?a=5&b=6");
});
