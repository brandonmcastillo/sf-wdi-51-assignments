// Front end side / connect mongoose and acquire it
var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/book-app", { useNewUrlParser: true });

// models/index.js
module.exports.Book = require("./book.js");