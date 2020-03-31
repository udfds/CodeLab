const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const mongoose = require('mongoose');
const BodyParser = require('body-parser');
const router = require("./routes");

require('dotenv').config();

const app = express();
const PORT = 3333;

mongoose.connect(process.env.DB_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}, () => console.log('Connected to the database!'));

app.use(morgan('common'));
app.use(cors({ origin: "http://localhost:3000" }));
app.use(BodyParser.json());
app.use(BodyParser.urlencoded({ extended: true }));
app.use(router);

app.listen(PORT, () => {
    console.log(`Server running in the port: ${PORT}`);
});

