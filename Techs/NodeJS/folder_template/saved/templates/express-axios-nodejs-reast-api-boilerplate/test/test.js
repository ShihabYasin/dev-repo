let assert = require('assert');
let request = require('request');


function test_1() {}
    var options = {
        'method': 'GET',
        'url': 'http://localhost:3000/cat/myfact/',
        'headers': {
        }
    };
    
    request(options, function (error, response) {
        if (error) throw new Error(error);
        assert.equal(response.body, 'Hello API 2 id Here !!!!');
    });
    


function test_2() {}
    var options = {
        'method': 'GET',
        'url': 'http://localhost:3000/cat/facts/',
        'headers': {
        }
    };
    
    request(options, function (error, response) {
        if (error) throw new Error(error);
        assert.equal(response.body, response.body);
    });




test_1();
test_2();   