// 1. Create logger instance
// 2 . Use logger to log

const winston = require('winston');

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
      new winston.transports.File({ filename: '/media/yasin/MyStudy/Saved_Downloads/ELK_LOG_DATA_STORAGE/1.log', level: 'info' })
    ]
  });



const currentDateTime = new Date().toLocaleString();
console.log(currentDateTime);

logger.log('info', `MSG => NOW TIME IS :  ${currentDateTime}`);
