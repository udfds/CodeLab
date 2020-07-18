const router = require('express').Router();
let Task = require('../models/task.model');

router.route('/').get((_request, response) => {
    Task.find()
        .then(tasks => response.json(tasks))
        .catch(error => response.status(400).json('Error: ' + error));
});

router.route('/').post((request, response) => {
    const username = request.body.username;
    const description = request.body.description;
    const duration = Number(request.body.duration);
    const date = Date.parse(request.body.date);

    const newTask = new Task({ username, description, duration, date });

    newTask.save()
        .then(() => response.json('Task added!'))
        .catch(error => response.status(400).json('Error: ' + error));
});

router.route('/:id').get((request, response) => {
    Task.findById(request.params.id)
        .then(task => response.json(task))
        .catch(error => response.status(400).json('Error: ' + error));
});

router.route('/:id').delete((request, response) => {
    Task.findByIdAndDelete(request.params.id)
        .then(() => response.json('Task deleted!'))
        .catch(error => response.status(400).json('Error: ' + error));
});

router.route('/:id').put((request, response) => {
    Task.findById(request.params.id)
        .then(task => {
            task.username = request.body.username;
            task.description = request.body.description;
            task.duration = Number(request.body.duration);
            task.date = Date.parse(request.body.date);

            task.save()
                .then(() => response.json('Task updated!'))
                .catch(error => response.status(400).json('Error: ' + error));

        })
        .catch(error => response.status(400).json('Error: ' + error));
});

module.exports = router;