'use strict'

const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();

// Conectar com o banco
const MongoClient = require('mongodb').MongoClient;

const uri = "";
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect(err => {
    const collection = client.db("test").collection("shopping");
    //console.log(collection);

    client.close();
});

// Carregar models
const Products = require('./models/products');

// Carregar routers
const route_index = require('./routes/index');
const route_products = require('./routes/products');

// Converter automaticamente em json
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// Definir rotas
app.use('/', route_index);
app.use('/products', route_products);

module.exports = app;