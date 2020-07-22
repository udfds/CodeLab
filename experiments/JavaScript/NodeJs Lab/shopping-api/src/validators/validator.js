'use stricts';

let errors = [];

function Validator() {
    errors = [];
}

Validator.prototype.isRequired = (value, property) => {
    if (!value || value.length <= 0) {
        errors.push({ message: property + ' is required' });
    }
}

Validator.prototype.minLength = (value, min, property) => {
    if (!value || value.length < min) {
        errors.push({ message: property + ' is invalid, the minimum number of characters is ' + min });
    }
}

Validator.prototype.maxLength = (value, max, property) => {
    if (!value || value.length > max) {
        errors.push({ message: property + ' is invalid, the maximum number of characters is ' + max });
    }
}

Validator.prototype.errors = () => {
    return errors;
}

Validator.prototype.clear = () => {
    errors = [];
}

Validator.prototype.isValid = () => {
    return errors.length == 0;
}

module.exports = Validator;