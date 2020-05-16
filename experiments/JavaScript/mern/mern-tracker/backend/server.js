const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

require('dotenv').config();

const app = express();
const port = process.env.port || 5000;
const uri = process.env.MONGO_URI;

app.use(cors());
app.use(express.json());

// -----------------------------------------------------------------------------------------
// DataBase
// -----------------------------------------------------------------------------------------
mongoose.connect(uri, { useNewUrlParser: true, useCreateIndex: true });
const connection = mongoose.connection;

connection.once('open', () => {
    console.log("MongoDB database connection established successfully");
});

// -----------------------------------------------------------------------------------------
// Routes
// -----------------------------------------------------------------------------------------
const taskRouter = require('./routes/task');
const userRouter = require('./routes/user');

app.use('/task', taskRouter);
app.use('/user', userRouter);

// -----------------------------------------------------------------------------------------
// App
// -----------------------------------------------------------------------------------------
app.listen(port, () => {
    console.log('-- Running on port:' + port);
});
