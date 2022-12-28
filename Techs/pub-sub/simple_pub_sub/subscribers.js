import { createRequire } from "module";
const require = createRequire(import.meta.url);

// import{ insert_doc, drop_collection , update_doc  } from "./writer-service.js";
import { client , topics } from "./kafka_base.js";
const Kafka = require('kafka-node');


let topic  = topics[1]

const consumer = new Kafka.Consumer(client, [{ topic: topic }], {
  autoCommit: true
});

consumer.on('message', function(message) {
  console.log(message);
});

consumer.on('error', function(error) {
  console.error(error);
});