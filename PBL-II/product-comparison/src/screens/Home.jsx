import Heading from '../components/TitleBar'
import { Flex, Button, Link } from '@chakra-ui/react'

function Btn({ text, redirTo }) {
    return (
        <Button as={'a'} href={redirTo} height={200} width={400} fontSize={30}>
            {text}
        </Button>
    )
}

function Home() {
    return (
        <Flex height="100vh" flexDirection="column">
            <Heading/>
            <Flex justifyContent="space-evenly" alignItems="center" flexGrow="1">
                <Btn text="Fashion" redirTo="/fashion" />
                <Btn text="Electronics" redirTo="/electronics" />
            </Flex>
        </Flex>
    )
}

export default Home;