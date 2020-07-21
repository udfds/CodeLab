'use strict';

const express = require('express');
const router = express.Router();
const controller = require('../controllers/products');

router.get('/', controller.get);
router.post('/', controller.post);
router.put('/:id', controller.put);
router.delete('/:id', controller.delete);
router.get('/:slug', controller.getBySlug);
router.get('/:id', controller.getById);

module.exports = router;