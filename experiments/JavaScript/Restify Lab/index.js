const restify = require('restify');
const port = 8080;

const server = restify.createServer();

server.get('/', (_request, response) => {
    response.send({ message: '-- App running fine!' });
});

server.get('/feature/:name', (request, response) => {
    let message = '-- Feature: ' + request.params.name + ' is fine!';
    response.send({ message: message });
});

server.listen(port, () => {
    console.log('-- App running on port: ' + port);
})