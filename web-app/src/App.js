import './App.css';
import Header from './components/HeaderBar' 
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import { locationService } from './api/locationService';
import { deviceService } from './api/deviceService';
import LocationCard from './components/LocationCard';
import DeviceCard from './components/DeviceCard';
import { useState, useEffect } from 'react';
import Stack from '@mui/material/Stack';


function App() {
  const [locations, setLocations] = useState([]);
  const [devices, setDevices] = useState([]);

  async function getLocations(){
    try {
      const locations_response = await locationService.get();
      setLocations(locations_response.data.response);
      return locations_response.data;
    } catch(error) {
      console.log(error);
    }
  }

  async function getDevices(locations){
    try {
      const devices_response = await deviceService.get(locations);
      setDevices(devices_response.data.response);
      return devices_response.data;
    }
    catch(error) {
      console.log(error);
    }
  }

  useEffect(() => {
    const response = {
      data: {
        response: [
          { id: 1, name: 'Location 1' },
          { id: 2, name: 'Location 2' },
          { id: 3, name: 'Location 3' }
        ]
      }
    };
    
    setLocations(response.data.response); // Установите данные в state
  }, []); // Пустой массив - выполнится один раз при монтировании

  useEffect(() => {
    const response = {
      data: {
        response: [
          { id: 1, name: 'Device 1', location_id: 1 },
          { id: 2, name: 'Device 2', location_id: 1 },
          { id: 3, name: 'Device 3', location_id: 2 }
        ]
      }
    };
    
    setDevices(response.data.response); // Установите данные в state
  }, []);

  const getDevicesForLocation = (locationId) => {
    return devices.filter(device => device.location_id === locationId);
  };

  return (
    <div className="App"> 
      <div>
        <Header />
      </div>
      {locations.length > 0 ? (
        <Container maxWidth={false} sx={{ m: 10, mx: 'auto' }}>
          <Stack spacing={2}>
          {locations.map((location, index) => (
            <LocationCard key={index} location={location} devices = { devices }>
              <h1>some text</h1>
                {/* {getDevicesForLocation(location.id).map((device) => (
                  <DeviceCard key={device.id} device={device} />
                ))} */}
            </LocationCard>
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