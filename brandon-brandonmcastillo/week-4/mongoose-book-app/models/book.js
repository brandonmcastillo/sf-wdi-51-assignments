// book.js
//jshint esversion:6

const mongoose = require('mongoose');
const Schema = mongoose.Schema;
// Constructor Schema
const BookSchema = new Schema({
    title: String,
    author: String,
    image: String,
    date: Number
});
// Creates book model 
const Book = mongoose.model('Book', BookSchema);

module.exports = Book;