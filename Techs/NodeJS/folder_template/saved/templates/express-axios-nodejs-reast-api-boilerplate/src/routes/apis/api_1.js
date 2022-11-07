const axios = require('axios');

// Write Your internal API Implementation here.
const getFacts = async () => {
  const response = await axios.get(`https://catfact.ninja/fact`);
  return response.data.fact;
};

// return response data to router
module.exports = async (req, res) => {  
  res.send(await getFacts());
};
