'use strict'

const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const config = require('./config');

// Converter automaticamente em json
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));


// -----------------------------------------------------------------------------------------
// DataBase
// -----------------------------------------------------------------------------------------
mongoose.connect(config.connectionString, { useNewUrlParser: true, useCreateIndex: true });
const connection = mongoose.connection;
connection.once('open', () => {
    console.log("MongoDB database connection established successfully");
});


// -----------------------------------------------------------------------------------------
// Models
// -----------------------------------------------------------------------------------------
const Product = require('./models/products');
const Customer = require('./models/customers');
const Order = require('./models/orders');


// -----------------------------------------------------------------------------------------
// Routes
// -----------------------------------------------------------------------------------------
const route_index = require('./routes/index');
const route_products = require('./routes/products');
const route_customers = require('./routes/customers');
const route_orders = require('./routes/orders');

app.use('/', route_index);
app.use('/products', route_products);
app.use('/customers', route_customers);
app.use('/orders', route_orders);

module.exports = app;