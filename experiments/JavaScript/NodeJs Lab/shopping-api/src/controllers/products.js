'use stricts';

const mongoose = require('mongoose');
const Product = mongoose.model('Product');

exports.get = (req, res, _next) => {
    Product.find({}).then(data => {
        res.status(200).send(data);
    }).catch(error => {
        res.status(400).send(error);
    });
};

exports.post = (req, res, _next) => {
    let product = new Product(req.body);
    product.save().then(x => {
        res.status(201).send({
            message: 'Produto cadastrado com sucesso!'
        });
    }).catch(error => {
        res.status(400).send({
            message: 'Erro ao cadastrar produto!',
            data: error
        });
    }).finally(() => {
        console.log('F---');
    });

};

exports.put = (req, res, _next) => {
    const id = req.params.id;
    res.status(200).send({
        id: id,
        item: req.body
    });
};

exports.delete = (req, res, _next) => {
    res.status(200).send(req.body);
};

exports.getBySlug = (req, res, _next) => {
    Product.findOne({
        active: true,
        slug: req.params.slug
    }).then(data => {
        res.status(200).send(data);
    }).catch(error => {
        res.status(400).send(error);
    });
};

exports.getById = (req, res, _next) => {
    Product.findById(req.params).then(data => {
        res.status(200).send(data);
    }).catch(error => {
        res.status(400).send(error);
    });
};