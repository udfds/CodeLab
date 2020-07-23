'use stricts';

const Product = require('../models/products');
const Validator = require('../validators/validator');
const Repository = require('../repositories/products');

exports.get = (_req, res, _next) => {
    Repository.list().then(products => {
        res.status(200).send(products);
    }).catch(error => {
        res.status(400).send(error);
    });
};

exports.post = (req, res, _next) => {
    let draftProduct = new Product(req.body);

    let validator = new Validator();
    validator.minLength(draftProduct.title, 3, 'title');
    validator.minLength(draftProduct.slug, 3, 'slug');
    validator.minLength(draftProduct.description, 3, 'description');
    validator.maxLength(draftProduct.title, 10, 'title');
    validator.maxLength(draftProduct.slug, 10, 'slug');
    validator.maxLength(draftProduct.description, 10, 'description');

    if (!validator.isValid()) {
        res.status(400).send(validator.errors()).end();
        return;
    }

    Repository.save(draftProduct).then(() => {
        res.status(201).send({
            message: 'Product cadastrado com sucesso!'
        });
    }).catch(error => {
        res.status(400).send({
            message: 'Erro ao cadastrar Product!',
            data: error
        });
    });
};

exports.put = (req, res, _next) => {
    let draftProduct = {
        title: req.body.title,
        description: req.body.description,
        price: req.body.price
    };

    Repository.update(req.params.id, draftProduct).then(() => {
        res.status(201).send({
            message: 'Product atualizado com sucesso!'
        });
    }).catch(error => {
        res.status(400).send({
            message: 'Erro ao atualizar Product!',
            data: error
        });
    });
};

exports.delete = (req, res, _next) => {
    Repository.delete(req.params.id).then(() => {
        res.status(201).send({
            message: 'Product removido com sucesso!'
        });
    }).catch(error => {
        res.status(400).send({
            message: 'Erro ao remover Product!',
            data: error
        });
    });
};

exports.getBySlug = (req, res, _next) => {
    Repository.getBySlug(req.params.slug).then(product => {
        res.status(200).send(product);
    }).catch(error => {
        res.status(400).send(error);
    });
};

exports.getById = (req, res, _next) => {
    Repository.getById(req.params.id).then(product => {
        res.status(200).send(product);
    }).catch(error => {
        res.status(400).send(error);
    });
};