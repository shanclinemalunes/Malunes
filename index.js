// Pakage imports
const express = require('express');

// Server setup 
const server = express ()
let PORT = 4321
let HOSTNAME = '192.168.2.35'

server.listen(PORT,HOSTNAME, () => {
        conlose.log('server is running: ${ HOSTNAME}:${PORT}');
}) 



