import { Container, Stack } from '@chakra-ui/react';
import Navbar from './components/Navbar';

function App() {
  return (
    <>
      <Stack minH={'100vh'}>
        <Navbar />
        <Container></Container>
      </Stack>
    </>
  );
}

export default App;
