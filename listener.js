#!/usr/bin/env node

var net = require('net');

var onConnection = function (socket) {
  socket.pipe(process.stdout);
};

net.createServer(onConnection).listen(5280);
console.log('Server running at 127.0.0.1:5280');
