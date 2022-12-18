import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import BasicGrid from './BasicGrid';
import { Box } from '@mui/system';
import CottageIcon from '@mui/icons-material/Cottage';
import { Typography } from '@mui/material';
import { Autocomplete } from '@mui/material';
import { TextField } from '@mui/material';


const top100Films = [
  { label: 'The Shawshank Redemption', year: 1994 },
  { label: 'The Godfather', year: 1972 },
  { label: 'The Godfather: Part II', year: 1974 },
  { label: 'The Dark Knight', year: 2008 },
  { label: '12 Angry Men', year: 1957 },
  { label: "Schindler's List", year: 1993 },
  { label: 'Pulp Fiction', year: 1994 }
]
function App() {
  const defaultProps = {
    options: top100Films,
    getOptionLabel: (option) => option.title,
  };
  const flatProps = {
    options: top100Films.map((option) => option.title),
  };
  const [value, setValue] = React.useState(null)

  return (

    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100px',
      }}
    >
       <Autocomplete
      disablePortal
      id="combo-box-demo"
      options={top100Films}
      sx={{ width: 300 }}
      renderInput={(params) => <TextField {...params} label="Movie" />}
      
    />

    

    </div >
  );
}

export default App;
