import './App.css';
import Header from './components/HeaderBar' 
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import { apiService } from './api/locations_service';
import LocationCard from './components/LocationCard'
import { useState, useEffect } from 'react';
import Stack from '@mui/material/Stack';


function App() {
  const [locations, setLocations] = useState([]);

  async function getLocations(){
    try {
      const response = await apiService.get();
      setLocations(response.data.response);
      return response.data;
    } catch(error) {
      console.log(error);
    }
  }

  useEffect(() => {
    const response = {
      data: {
        response: [
          { id: 1, name: 'Location 1', address: 'Address 1' },
          { id: 2, name: 'Location 2', address: 'Address 2' },
          { id: 3, name: 'Location 3', address: 'Address 3' }
        ]
      }
    };
    
    setLocations(response.data.response); // Установите данные в state
  }, []); // Пустой массив - выполнится один раз при монтировании

  return (
    <div className="App"> 
      <div>
        <Header />
      </div>
      {locations.length > 0 ? (
        <Container maxWidth={false} sx={{ m: 10, mx: 'auto' }}>
          <Stack spacing={2}>
          {locations.map((location, index) => (
            <LocationCard key={index} location={location} />
          ))}
          </Stack>
        </Container>
      ) : (
        <Container sx={{ m: 40, mx: 'auto' }}>
          <h3>
            No locations so far
          </h3>
          <Button sx={{ justifyContent: "center", alignItems: "center" }}>
            add location
          </Button>
        </Container>
      )}
    </div>
  );
}

export default App;