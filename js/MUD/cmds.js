var dice = require('./dice').roller
var Cmd = {
  do: function(args, socket, clients) {
    socket.broadcast("<"+socket.name+"> "+args.join(" "), socket)
  },
  w: function(args, socket, clients) {
    socket.whisper(socket.name + ":w> " + args.slice(2).join(" "), tokens[1], socket)
  },
  l: function(args, socket, clients) {
    socket.write("Users: ")
    clients.forEach(function (client) {
      if(client.name === socket.name) return
      else socket.write(client.name+", ")
    })
    socket.write("\n\r")
  },
  roll: function(args, socket, clients) {
    if(args[0] === undefined) args[0]="1d6"

    var specs = args[0].split('d')
    if(isNaN(specs[0]) || isNaN(specs[1])) {
      socket.write("Invalid Roll.\n\r")
      return
    }
    if(isNaN(args[1])) args[1] = 0;

    var result = dice.roll(specs[0], specs[1], args[1])
    socket.broadcast("\r"+socket.name+" rolled "+args[0]+"+"+args[1]+" and got a "+result+"\n\r", socket)
    socket.write("\r"+socket.name+" rolled "+args[0]+" w/ "+args[1]+" mod and got a "+result+"\n\r")
  },
  h: function(args, socket, clients){
    socket.write("!l - list peers, !w [name] [message] - whisper [message] to [name], !h - help\n\r")
    socket.write("!do [message], !roll [#dies]d[#sides] (mod)\n\r")
    socket.write("CTRL+C Cancel message, CTRL+D Exit littleMUD\n\r")
  }
}

module.exports.cmd = Object.create(Cmd);
