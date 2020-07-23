'user stricts';

const mongoose = require('mongoose');
const Customer = require('../models/customers');

exports.list = () => {
    return Customer.find();
};

exports.save = (draftCustomer) => {
    return draftCustomer.save();
};