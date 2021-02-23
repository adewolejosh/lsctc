const express = require('express');
const {Pool} = require('pg')
const db_config = require('./db/config.js')

const app = express()
const port = process.env.PORT

const client = new Pool(db_config)
client.connect(function(){
    console.log("Connected!")
})


app.listen(port, function(){
    console.log(`You're listening on port! ${port}`);
})
