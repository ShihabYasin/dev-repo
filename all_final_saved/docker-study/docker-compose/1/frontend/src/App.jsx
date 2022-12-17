import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button'
import { FormControl } from '@mui/material';
import { InputLabel } from '@mui/material';
import { Input } from '@mui/material';
import './App.css';


function App() {
  const [selectedFiles, setSelectedFiles] = useState(null);
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [filename, setFilename] = useState('');

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
    axios.get(`http://localhost:5000/download/${filename}`, { responseType: 'blob' }).then((response) => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
    });
  };

  return (
    <div className="container">
      <input type="file" multiple onChange={handleFileSelect} />

      <Button variant="contained" color="primary" onClick={handleUpload}>
        Upload
      </Button>

      <FormControl>
        <InputLabel htmlFor="filename">Filename</InputLabel>
        <Input id="filename" value={filename} onChange={(event) => setFilename(event.target.value)} />
      </FormControl>
      <Button type="button" variant="contained" color="primary" onClick={handleDownload}>
        Download
      </Button>


    </div>
  );
}

export default App;
