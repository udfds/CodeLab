'use strict'

const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();

// Carregar routers
const route_index = require('./routes/index');
const route_products = require('./routes/products');

// Converter automaticamente em json
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// Conectar com o banco
const MongoClient = require('mongodb').MongoClient;
const uri = "";
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect(err => {
    const collection = client.db("test").collection("tasks");
    //console.log(collection);
    client.close();
});



app.use('/', route_index);
app.use('/products', route_products);

module.exports = app;