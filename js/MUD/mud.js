// Load the TCP Library
var net = require('net');
var Cmds = require('./cmds').cmd;
// Keep track of the chat clients
var clients = [];
var SERVER_BANNER = "Welcome to littleMUD. To exit press CTRL+D\n\r"

function setname(name) { // Uses recursion to create unique names
  fname = name
  clients.forEach(function (client) {
    if(client.name === name) {
      fname = setname(name+".")
    }
  })
  if(name !== fname) console.log(fname)
  return fname
}

// Start a TCP Server
net.createServer(function (socket) {

  socket.authed=false
  // Identify this client
  socket.name = socket.remoteAddress + ":" + socket.remotePort;
  socket.data = ""

  // Readline from user
  socket.readline = function (incoming, callback) {
      incoming = incoming.toString()
      if(incoming.charCodeAt(0) === 13) {
        callback(this.data)
        this.data = ""
        socket.write(this.prompt+this.data)
      } else if(incoming.charCodeAt(0) === 3) {
        this.data = ""
        socket.write("\n\r"+this.prompt+this.data)
      } else if(incoming.charCodeAt(0) === 4) {
        socket.end()
      } else if(incoming.charCodeAt(0) === 8) {
        if(this.data === "") return
        this.data = this.data.substring(0,this.data.length-1)
        socket.write(String.fromCharCode(13))
        socket.write(this.prompt+this.data+" ")
        socket.write(String.fromCharCode(8))
      } else {
        this.data += incoming
        socket.write(String.fromCharCode(13))
        socket.write(this.prompt+this.data)
      }
  }

  // Send a message to all clients
  socket.broadcast = function (message, sender) {
    clients.forEach(function (client) {
      // Don't want to send it to sender
      if (client === sender) return;
      client.write('\r'+message+'\n\r')
      client.write(client.prompt+client.data)
    });
    // Log it to the server output too
    console.log(message)

  }

  // Send a message to a client
  socket.whisper = function (message, recipient, sender) {
    clients.forEach(function (client) {
      // Don't want to send it to sender
      if (client === sender) return;
      if (client.name === recipient) {
        client.write('\r'+message+'\n\r')
        client.write(client.prompt+client.data)
      }
    });
    // Log it to the server output too
    console.log(message)

  }

  // Put this new client in the list
  clients.push(socket);
  // Send a nice welcome message and announce
  socket.write(SERVER_BANNER)
  socket.prompt = "Name>"
  socket.write(socket.prompt);

  // Handle incoming messages from clients.
  socket.on('data', function (data) {
    if(socket.authed) { // if user is authenticated
      socket.readline(data, function(line) {
        if(line.charAt(0) === "!") {
          var tokens = line.split(" ")
          var cmd = tokens[0].substring(1).toLowerCase()
          if (cmd in Cmds) {
             Cmds[cmd](tokens.slice(1), socket, clients)
          } else {
            socket.write("Command not found.\n\r")
          }
        } else {
          socket.broadcast(socket.name + "> " + line, socket)
        }
      })
    } else { // authenticate user
      socket.readline(data, function(line) {
        socket.name = setname(line); // set users name and authenticate user
        socket.authed=true;
        socket.write('\r'+socket.name + " joined the chat\n\r") // announce the users presence
        socket.broadcast(socket.name + " joined the chat", socket);
        socket.prompt = "You>"
      })
    }
  });

  // Remove the client from the list when it leaves
  socket.on('end', function () {
    clients.splice(clients.indexOf(socket), 1);
    socket.broadcast(socket.name + " left the chat.");
  });

}).listen(5000);

// Put a friendly message on the terminal of the server.
console.log("Chat server running at port 5000\n\r");
