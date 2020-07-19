'use strict';

const express = require('express');
const router = express.Router();

router.get('/', (_req, res, _next) => {
    res.status(200).send({
        title: 'Shopping API',
        version: '0.0.3'
    });
});

module.exports = router;