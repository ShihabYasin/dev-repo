const express = require('express');
const router = express.Router();


// list possible apis 
const api_1 = require('./apis/api_1');
const api_2 = require('./apis/api_2');  

// connect api end points & associated apis with router
router.get('/facts', api_1);
router.get('/myfact', api_2);

// export router filled with apis 
module.exports = router;


