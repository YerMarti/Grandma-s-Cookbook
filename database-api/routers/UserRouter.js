const express = require('express');
const router = express.Router();

const User = require('../models/User');
const Recipe = require('../models/Recipe');

// Create a new user
router.post('/register', async (req, res) => {    
    try {
        const newUser = new User({
            username: req.body.username,
            password: req.body.password
        });
        await newUser.save();
        res.status(201).json(newUser);
    } catch (err) {
        console.error("Error in /register:", err);
        res.status(500).json({ error: err.message });
    }
});

// Check login credentials
router.post('/login', async (req, res) => {
    try {
        const user = await User.findOne({ username: req.body.username, password: req.body.password });
        
        if (!user) {
            return res.status(401).json({ error: 'Invalid credentials' });
        }

        res.json(user);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Add a recipe to a user's favorites
router.post('/:username/favorites', async (req, res) => {
    try {
        const user = await User.findOne({ username: req.params.username });

        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }

        const recipeData = req.body;

        user.favoriteRecipes.push(recipeData.id);
        await user.save();

        res.status(200).json(user);
    } catch (err) {
        console.error(err)
        res.status(500).json({ error: err.message });
    }
});

// Get a user's favorite recipes
router.get('/:username/favorites', async (req, res) => {
    try {
        const user = await User.findOne({ username: req.params.username });

        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        
        res.json(user.favoriteRecipes);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

module.exports = router;