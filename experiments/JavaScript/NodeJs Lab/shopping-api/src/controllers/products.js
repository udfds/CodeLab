'use stricts';

exports.post = (req, res, _next) => {
    res.status(201).send(req.body);
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


