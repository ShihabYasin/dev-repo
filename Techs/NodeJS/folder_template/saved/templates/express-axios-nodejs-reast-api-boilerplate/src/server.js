require('dotenv').config();


const app = require('./app');


const config = require('./config/config.json');
const env = process.env.NODE_ENV;
const configuration = config[env];

app.listen(configuration.port, () => {
  console.log(`${env} server running at port ${configuration.port}`);
});
