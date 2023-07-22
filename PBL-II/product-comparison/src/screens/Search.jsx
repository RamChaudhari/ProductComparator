import SearchView from '../SearchView';
import TitleBar from '../components/TitleBar'
import { Flex, Box } from '@chakra-ui/react'
import { useState } from 'react';
import DetailsView from '../productDetails';
import APIResponse from '../dummyAPI';

function Search({ searchType }) {
    const [bottomPanel, useBottomPanel] = useState(<SearchView searchType={searchType} searchFunc={search}/>);

    const URL = "http://127.0.0.1:5500/login?"
    const [title, useTitle] = useState(<TitleBar text="Product Comparision" />)

    async function search(){
        const query = document.getElementById("searchInput").value;
        const type = document.getElementById("searchType").value;
        // console.log(query, type);
        const searchParams = new URLSearchParams({
            'query': query,
            'type': type
        });

        // var result
        useBottomPanel(<div></div>)

        const results = await fetch( URL + searchParams, ).then((response) => response.json())
        // const results = APIResponse;
        // console.log()
        
        useTitle(<TitleBar text={query.toUpperCase()} />)
        useBottomPanel(<DetailsView searchResult={results}/>)
    }

    return (
        <Flex height="100%" flexDirection="column">
            {title}
            <Box flexGrow="1">
                {bottomPanel}
            </Box>
        </Flex>

    )
}

export default Search;