const mongoose = require('mongoose');

const UserModel = new mongoose.Schema({
    username: { type: String, required: true },
    password: { type: String, required: true, max: 1024 },
    posts: [{ type: mongoose.Schema.Types.ObjectId, type: mongoose.Schema.Types.ObjectId, ref: 'post' }]
}, {
    timestamps: true
});

module.exports = mongoose.model('user', UserModel);