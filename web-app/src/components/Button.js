import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

export default function ContainedButtons({ buttonName }) {
  return (
    <Stack direction="row" spacing={2}>
      <Button variant="contained">{buttonName}</Button>
    </Stack>
  );
}
