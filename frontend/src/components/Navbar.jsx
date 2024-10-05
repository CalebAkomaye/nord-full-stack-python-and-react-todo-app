import {
  Box,
  Button,
  Container,
  Flex,
  Stack,
  useColorMode,
  useColorModeValue,
} from '@chakra-ui/react';
import { IoMoon } from 'react-icons/io5';
import { Input } from '@chakra-ui/react';
import { LuSun } from 'react-icons/lu';

function Navbar() {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Container maxW={'900px'} paddingY={'1.5'}>
      <Box
        px={'4'}
        py={'1'}
        my={'4'}
        bg={useColorModeValue('gray.200', 'gray.700')}
      >
        <Stack direction={'row'}>
          <Flex alignItems={'center'} justifyContent={'space-between'}>
            {/* Left*/}
            <Flex
              alignItems={'center'}
              justifyContent={'center'}
              gap={3}
              display={{ base: 'none', sm: 'flex' }}
            >
              <Button onClick={toggleColorMode}>
                {colorMode === 'light' ? <IoMoon /> : <LuSun size={20} />}
              </Button>
            </Flex>
            {/* Right*/}
            <Flex ml={'10'}>
              <Input placeholder='Search' border={'.5px solid grey'} />
            </Flex>
            <Flex></Flex>
          </Flex>
        </Stack>
      </Box>
    </Container>
  );
}

export default Navbar;
