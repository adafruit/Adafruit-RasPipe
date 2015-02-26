#!/usr/bin/env node

var net = require('net'),
    sys = require('sys');

net.createServer(onConnection).listen(5280);

function onConnection(socket) {
  socket.setNoDelay(true);

  socket.addListener("connect", function () {
    // sys.puts('client connected: ' + this.remoteAddress);
  });

  socket.addListener("data", function (data) {
    sys.puts(data);
  });

  socket.addListener("end", function () {
    // sys.puts('end of connection');
    this.end();
  });
}

sys.puts('Server running at 127.0.0.1:8124');
