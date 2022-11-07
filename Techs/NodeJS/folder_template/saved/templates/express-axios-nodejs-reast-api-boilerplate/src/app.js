const express = require('express');
const app = express();

// get a router middleware
const middleware = require('./routes/router');
app.use('/cat', middleware); // use this router middleware with /cat link prefixed

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

module.exports = app;
