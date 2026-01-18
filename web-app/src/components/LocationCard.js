import * as React from 'react';
import { styled } from '@mui/material/styles';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Collapse from '@mui/material/Collapse';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { red } from '@mui/material/colors';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShareIcon from '@mui/icons-material/Share';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import Stack from '@mui/material/Stack';
import { useState } from 'react';
import DeviceCard from './DeviceCard';



export default function LocationCard({ location, devices }) {
  const [id] = useState(location.id);
  const [name] = useState(location.name);


  return (
    <Card sx={{ maxWidth: '100%' }}>
      <CardHeader
        action={
          <IconButton aria-label="settings">
            <MoreVertIcon />
          </IconButton>
        }
        title={ name }
      />
      <CardContent>
        <Stack direction="row" spacing={2}>
          {devices.map((device, index) => (
            <DeviceCard key={device.id} device={device} />
          ))}
        </Stack>
      </CardContent>
      <CardActions disableSpacing>
      </CardActions>
    </Card>
  );
}