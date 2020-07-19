'use strict'

const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const router = express.Router();

// Converter automaticamente em json
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

const route_get = router.get('/', (_req, res, _next) => {
    res.status(200).send({
        title: 'Paradox API',
        version: '0.0.2'
    });
});

const route_post = router.post('/', (req, res, _next) => {
    res.status(201).send(req.body);
});

const route_put = router.put('/:id', (req, res, _next) => {
    const id = req.params.id;
    res.status(200).send({
        id: id,
        item: req.body
    });
});

const roude_delete = router.delete('/:id', (req, res, _next) => {
    res.status(200).send(req.body);
});

app.use('/', route_get);
app.use('/', route_post);
app.use('/', route_put);
app.use('/', roude_delete);

module.exports = app;