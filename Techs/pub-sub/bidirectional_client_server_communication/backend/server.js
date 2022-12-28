const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
let services = require('./services.js');
let meta = require('./meta.js');



app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('a user connected');

  socket.on(meta.topics.button_clicked, (data) => {
    let received_topic = meta.topics.button_clicked;
    console.log(`Topic: ${received_topic}: Button Clicked Received with data: ${data}`);
    services.sendResult(io, meta.topics.finished_result, data);
  });

  socket.on('disconnect', () => {
    console.log('user disconnected');
  });
});


http.listen(3000, () => {
  console.log('listening on *:3000');
});




