const jwt = require('jsonwebtoken');

function validateToken(request, response, next) {
    const token = request.header('auth-token');
    if (!token) {
        return response.status(400).send({error: 'Access denied.'});
    }

    try {
        const verified = jwt.verify(token, process.env.JWT_SECRET);
        request.user = verified;
        next();

    } catch (error) {
        response.status(400).send({error: 'Invalid token.'});
    }
}

module.exports = validateToken;