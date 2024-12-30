const mongoose = require('mongoose');

const recipeSchema = new mongoose.Schema({
    id: { type: String, required: true, unique: true },
    name: { type: String, required: true },
    category: { type: String },
    area: { type: String },
    instructions: { type: String },
    thumbnail: { type: String },
    ingredients: { type: Map, of: String },
});

module.exports = mongoose.model('Recipe', recipeSchema);