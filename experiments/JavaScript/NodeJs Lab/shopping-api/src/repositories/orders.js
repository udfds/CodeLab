'user stricts';

const mongoose = require('mongoose');
const Order = require('../models/orders');

exports.list = () => {
    return Order.find().populate('customer');
};

exports.save = (draftOrder) => {
    return draftOrder.save();
};