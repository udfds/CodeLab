'use stricts';

const Order = require('../models/orders');
const Repository = require('../repositories/orders');
const guid = require('guid');

exports.get = (_req, res, _next) => {
    Repository.list().then(orders => {
        res.status(200).send(orders);
    }).catch(error => {
        res.status(400).send(error);
    });
};

exports.post = (req, res, _next) => {
    let draftOrder = new Order(req.body);

    draftOrder.number = guid.raw().substring(0, 6);

    Repository.save(draftOrder).then(() => {
        res.status(201).send({
            message: 'Order cadastrado com sucesso!'
        });
    }).catch(error => {
        res.status(400).send({
            message: 'Erro ao cadastrar Order!',
            data: error
        });
    });
};