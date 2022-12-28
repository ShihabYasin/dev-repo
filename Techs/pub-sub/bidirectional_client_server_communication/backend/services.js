let result_data_dummy_1 = { message: 'NO 1  => result is here !!' };


async function sendResult(io_obj, topic, data) {
    let result_data = { result_data: result_data_dummy_1, request_data: JSON.parse(data) };
    await io_obj.emit(topic, JSON.stringify(result_data));
  }

module.exports = {
    sendResult
};