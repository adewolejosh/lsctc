const express = require('express');
const {pool} = require('./config')

const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: true}))
