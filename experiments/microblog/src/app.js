const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const mongoose = require('mongoose');
const BodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

require('dotenv').config();

const app = express();
const PORT = 3333;
const Users = require('./models/user.js');
const Posts = require('./models/post.js');
const authentication = require('./auth.js');

mongoose.connect(process.env.DB_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}, () => console.log('Connected to the database!'));

app.use(morgan('common'));
app.use(cors({ origin: "http://localhost:3000" }));
app.use(BodyParser.json());
app.use(BodyParser.urlencoded({ extended: true }));

app.listen(PORT, () => {
    console.log(`Server running in the port: ${PORT}`);
});

app.get('/', (req, res) => {
    res.send('CodeLab - Microblog');
});

app.post('/users', authentication, async (request, response) => {
    try {
        const { username, password } = request.body

        const draftUser = await Users.findOne({username});

        if (!!draftUser) {
            return response.status(400).send({ error: 'Username in use.'}); 
        }

        let salt = bcrypt.genSaltSync(10);
        let passwordCrypt = bcrypt.hashSync(password, salt);
        
        let user = new Users({ username: username, password: passwordCrypt });
        let result = await user.save();
        response.send(result);

    } catch (error) {
        response.status(500).send(error);
    }
});

app.get('/users', authentication, async (_request, response) => {
    try {
        let users = await Users.find().exec();
        response.send(users);

    } catch (error) {
        response.status(500).send(error);
    }
});

app.get('/users/:id', authentication, async (request, response) => {
    try {
        let user = await Users.findById(request.params.id).exec();
        response.send(user);

    } catch (error) {
        response.status(500).send(error);
    }
});

app.post('/login', async (request, response) => {
    try {
        const { username, password } = request.body;
        const user = await Users.findOne({username});

        if (!user) {
            return response.status(400).send({ error: 'Username not found.'});
        }

        const validPassword = bcrypt.compareSync(password, user.password);
        if (!validPassword) {
            return response.status(400).send({ error: 'Invalid password' });
        }

        const token = jwt.sign({_id: user.id}, process.env.JWT_SECRET);    
        
        response.header('auth-token', token).send(token);

    } catch (error) {
        response.status(500).send(error);
    }
});

app.post('/posts', authentication, async (request, response) => {
    try {
        const { content } = request.body;
        console.log(request.user);

        let post = new Posts({owner: request.user, content});
        let result = await post.save();

        if (!post) {
            response.status(400).send({error: 'Unable to create post.'});
        } else {
            response.send(result);
        }

    } catch (error) {
        response.status(500).send(error);
    }

});

app.delete('/posts/:id', authentication, async (request, response) => {
    try {
        const { id } = request.params;
        await Posts.deleteOne(id);

        response.status(200).send({message: 'Post deleted.'});

    } catch (error) {
        response.status(500).send(error);
    }

});

app.put('/posts/:id/like', authentication, async (request, response) => {
    try {
        const { id } = request.params;
        const post = await Posts.findOne(id);

        if  (!post) {
            return response.status(400).send({error: 'Post not found.'});
        }

        if (post.owner === request.user._id) {
            return response.status(400).send({error: 'Invalid owner.'});
        }

        const likes = Posts.likes.some(like => like == req.user._id);
        
        if (likes) {
            post.likes = post.likes.filter(like => like != req.user._id);
        } else {
            post.likes.push(req.user._id);
        }    

        await post.save();

        response.status(200).send(post);

    } catch (error) {
        response.status(500).send(error);
    }
});