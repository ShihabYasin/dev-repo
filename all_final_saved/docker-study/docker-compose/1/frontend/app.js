import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button'



function App() {
  const [selectedFiles, setSelectedFiles] = useState(null);
  const [uploadedFiles, setUploadedFiles] = useState([]);

  const handleFileSelect = (event) => {
    setSelectedFiles(event.target.files);
  };

  const handleUpload = () => {
    const formData = new FormData();

    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append('file', selectedFiles[i]);
    }

    axios.post('http://localhost:5000/upload', formData)
      .then((response) => {
        setUploadedFiles(uploadedFiles.concat(response.data));
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleDownload = () => {
    axios.get('http://localhost:5000/download')
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div>
      <input type="file" multiple onChange={handleFileSelect} />

      <Button variant="contained" color="primary" onClick={handleUpload}>
        Upload
      </Button>
      <Button variant="contained" color="primary" onClick={handleDownload}>
        Download
      </Button>
    </div>
  );
}

export default App;
