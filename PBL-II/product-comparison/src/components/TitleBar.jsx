import { Box, Heading } from "@chakra-ui/react";

function heading({ text }) {
    return (
        <>
            <Heading margin="auto" fontSize="2.25rem" padding={5}>
                {text}
            </Heading>

            <hr />
        </>
    )
}


export default heading;