
const {Pool} = require('pg')
const express = require('express');
const db_config = require('./db/config.js');

const ping_router = require('./ping/default.js');

const app = express()
const port = process.env.PORT


const client = new Pool(db_config)
client.connect(function(){
    console.log("Connected!")
})

app.use('/', ping_router);


app.listen(port, function(){
    console.log(`You're listening on port! ${port}`);
})
