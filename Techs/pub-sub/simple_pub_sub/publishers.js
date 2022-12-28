import { createRequire } from "module";
const require = createRequire(import.meta.url);

// import{ insert_doc, drop_collection , update_doc  } from "./writer-service.js";
import { producer , create_kafka_topic, topics } from "./kafka_base.js";


let topic  = topics[1]


create_kafka_topic(topic)

producer.on('ready', function() {
  console.log('Producer is ready');

  const payloads = [
    { topic: topic, messages: 'Hello, World ' }
  ];

  producer.send(payloads, function(error, data) {
    console.log(data);
    process.exit(0);
  });
});

producer.on('error', function(error) {
  console.error(error);
});
