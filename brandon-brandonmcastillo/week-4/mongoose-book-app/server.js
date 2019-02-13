// server.js
// SERVER-SIDE JAVASCRIPT
// jshint esversion:6

/////////////////////////////
//  SETUP and CONFIGURATION
/////////////////////////////

//require express in our app
const express = require('express'),
    bodyParser = require('body-parser');
const db = require('./models');
// generate a new express app and call it 'app'
const app = express();

// serve static files in public
app.use(express.static('public'));

// body parser config to accept our datatypes
app.use(bodyParser.urlencoded({ extended: true }));

// var newBookUUID = 18;


////////////////////
//  ROUTES
///////////////////


// define a root route: localhost:3000/
app.get('/', function(req, res) {
    res.sendFile('views/index.html', { root: __dirname });
});

// get all books
app.get('/api/books', (req, res) => {
    db.Book.find((err, foundBooks) => {
        if (err) {
            console.log('Index Error: ${err}');
            res.sendStatus(500);

        }
    });

});

// get one book
app.get('/api/books/:id', function(req, res) {
    // find one book by its id
    console.log('books show', req.params);
    for (var i = 0; i < books.length; i++) {
        if (books[i]._id === req.params.id) {
            res.json(books[i]);
            break; // we found the right book, we can stop searching
        }
    }
});

// create new book
app.post('/api/books', function(req, res) {
    // create new book with form data (`req.body`)
    console.log('books create', req.body);
    var newBook = req.body;
    newBook._id = newBookUUID++;
    books.push(newBook);
    res.json(newBook);
});

// update book
app.put('/api/books/:id', function(req, res) {
    // get book id from url params (`req.params`)
    console.log('books update', req.params);
    var bookId = req.params.id;
    // find the index of the book we want to remove
    var updateBookIndex = books.findIndex(function(element, index) {
        return (element._id === parseInt(req.params.id)); //params are strings
    });
    console.log('updating book with index', deleteBookIndex);
    var bookToUpdate = books[deleteBookIndex];
    books.splice(updateBookIndex, 1, req.params);
    res.json(req.params);
});

// delete book
app.delete('/api/books/:id', function(req, res) {
    // get book id from url params (`req.params`)
    console.log('books delete', req.params);
    var bookId = req.params.id;
    // find the index of the book we want to remove
    var deleteBookIndex = books.findIndex(function(element, index) {
        return (element._id === parseInt(req.params.id)); //params are strings
    });
    console.log('deleting book with index', deleteBookIndex);
    var bookToDelete = books[deleteBookIndex];
    books.splice(deleteBookIndex, 1);
    res.json(bookToDelete);
});





app.listen(process.env.PORT || 3000, function() {
    console.log('Book app listening at http://localhost:3000/');
});