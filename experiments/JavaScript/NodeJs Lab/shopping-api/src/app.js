'use strict'

const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Converter automaticamente em json
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));


// -----------------------------------------------------------------------------------------
// DataBase
// -----------------------------------------------------------------------------------------
const uri = "mongodb+srv://<login>:<password>@cluster0-hq1oy.gcp.mongodb.net/shopping?retryWrites=true&w=majority";
mongoose.connect(uri, { useNewUrlParser: true, useCreateIndex: true });
const connection = mongoose.connection;
connection.once('open', () => {
    console.log("MongoDB database connection established successfully");
});


// -----------------------------------------------------------------------------------------
// Routes
// -----------------------------------------------------------------------------------------
const route_index = require('./routes/index');
const route_products = require('./routes/products');

// Definir rotas
app.use('/', route_index);
app.use('/products', route_products);

module.exports = app;