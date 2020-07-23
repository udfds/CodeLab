'use stricts';

const Customer = require('../models/customers');
const Validator = require('../validators/validator');
const Repository = require('../repositories/customers');

exports.get = (_req, res, _next) => {
    Repository.list().then(customers => {
        res.status(200).send(customers);
    }).catch(error => {
        res.status(400).send(error);
    });
};

exports.post = (req, res, _next) => {
    let draftCustomer = new Customer(req.body);

    let validator = new Validator();
    validator.minLength(draftCustomer.name, 3, 'name');
    validator.minLength(draftCustomer.email, 3, 'email');
    validator.minLength(draftCustomer.password, 6, 'password');

    if (!validator.isValid()) {
        res.status(400).send(validator.errors()).end();
        return;
    }

    Repository.save(draftCustomer).then(() => {
        res.status(201).send({
            message: 'Customer cadastrado com sucesso!'
        });
    }).catch(error => {
        res.status(400).send({
            message: 'Erro ao cadastrar customer!',
            data: error
        });
    });
};