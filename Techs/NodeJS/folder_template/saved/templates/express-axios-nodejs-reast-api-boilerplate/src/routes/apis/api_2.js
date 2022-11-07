

const api_function = (params) => {
  return 'Hello API 2 id Here !!!!'
}

module.exports = (req, res) => {
  res.send(api_function());
};