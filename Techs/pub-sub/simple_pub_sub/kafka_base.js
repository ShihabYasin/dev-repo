import { createRequire } from "module";
const require = createRequire(import.meta.url);

const Kafka = require('kafka-node');
const client = new Kafka.KafkaClient({ kafkaHost: 'localhost:9092' });
const producer = new Kafka.Producer(client);



let topics = ['new_request', 'process_request'];


function create_kafka_topic(topic_name) {
    client.createTopics([topic_name], function (error, result) {
        if (error) {
            console.error(error);
        } else {
            console.log(result);
        }
    });
}


export { client, producer , create_kafka_topic, topics }