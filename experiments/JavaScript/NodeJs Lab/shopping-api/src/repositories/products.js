'user stricts';

const mongoose = require('mongoose');
const Product = require('../models/products');

exports.list = () => {
    return Product.find();
};

exports.getBySlug = (slug) => {
    return Product.findOne({
        active: true,
        slug: slug
    });
};

exports.getById = (id) => {
    return Product.findById(id);
};

exports.save = (draftProduct) => {
    return draftProduct.save();
};

exports.update = (id, draftProduct) => {
    return Product.findByIdAndUpdate(id, {
        $set: {
            title: draftProduct.title,
            description: draftProduct.description,
            price: draftProduct.price
        }
    });
};

exports.delete = (id) => {
    return Product.findByIdAndRemove(id);
}