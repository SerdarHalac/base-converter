const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

const app = express();

// bring in routers

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

// router modules

module.exports = app;
