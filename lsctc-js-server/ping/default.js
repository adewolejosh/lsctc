
// This file is supposed to act as a default url address
// Reason: Clients(web or mobile) can ping this address at anytime to see if it is on/keep-alive

const express = require('express');

const route = express.Router();


route.get('', function(req, res){
    return res.status(200).json({"Success": "Successfully pinged lsctc-js-server"})
})


module.exports = route
