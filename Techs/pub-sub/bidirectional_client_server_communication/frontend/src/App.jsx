import React, { useEffect, useState } from 'react';
import socketIOClient from 'socket.io-client';
import Divider from '@mui/material/Divider'

let meta = require('./meta.js');

let data1 = { message: 'Button  1 was clicked' };

function App() {
  const [buttonClicked, setButtonClicked] = useState(false);
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const newSocket = socketIOClient('http://localhost:3000');
    setSocket(newSocket);

    newSocket.on(meta.topics.finished_result, (data) => {
      setButtonClicked(true);
      console.log('====================================');
      console.log(`DONE: ${data}`);
      console.log('====================================');
    });

    return () => {
      newSocket.disconnect();
    };
  }, []);

  const handleButtonClick = () => {
    socket.emit(meta.topics.button_clicked, JSON.stringify(data1));
  };

  return (
    <div>
      {buttonClicked ? 'Button was clicked' : 'Button was not clicked'}
      <Divider />
      <button onClick={handleButtonClick}>BUTTON 1</button>

    </div>
  );
}

export default App;
