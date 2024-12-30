const express = require('express');
const mongoose = require('mongoose');

const app = express();
const PORT = process.env.DATABASE_PORT || 3000;

// CONNECT TO MONGODB

const mongoUri = process.env.MONGO_URI || 'mongodb://mongodb:27017/cookbook';

mongoose.connect(mongoUri, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch((err) => {
    console.error('Error connecting to MongoDB:', err);
});

app.use(express.json());

// ROUTES

app.get('/', (req, res) => {
    res.json({ message: 'Cookbook Database API' });
});

const userRouter = require('./routers/UserRouter');
app.use('/users', userRouter);

// START SERVER

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});