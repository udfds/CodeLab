const mongoose = require('mongoose');

const PostModel = new mongoose.Schema({
    owner: { type: mongoose.Schema.Types.ObjectId, ref: 'user' },
    content: { type: String, required: true, min: 1 },
    likes: [{ type: mongoose.Schema.Types.ObjectId, ref: 'user'}]
}, {
    timestamps: true
});

module.exports = mongoose.model('post', PostModel);