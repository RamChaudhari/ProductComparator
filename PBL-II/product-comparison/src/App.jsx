import {useState} from "react";
import { Heading, Box, Input } from '@chakra-ui/react'
import DetailsView from './productDetails'
import SearchView from './SearchView'
import dummyResponse from './dummyAPI'
import { Routes, Route, Outlet, Link } from "react-router-dom";
import Home from "./screens/Home";

function Title() {
    return (
        <Box>
            <Heading margin="auto" fontSize={40} textAlign={'center'} padding={5}>
                Product Comparision
            </Heading>
        </Box>

    )
}


function App_Old() {
    const [contentPanel, useContentPanel] = useState(<SearchView searchFunc={useSearch}/>);
    const url = "http://127.0.0.1:5000/search";

    async function useSearch(){
        //do some magik
        const query = document.getElementById("searchInput").value;
        const body = new FormData();
        body.append('query', query);

        const response = await fetch(url, {
            mode: 'no-cors',
            'headers':{
                'Access-Control-Allow-Origin': 'no-cors'
            },
            'method': 'post',
            'body': body
        })
        const searchResults = await response.json();
        console.log(query);
        // const detailsElement = <DetailsView searchResult={searchResults} />
        // useContentPanel(detailsElement);
    }

    // const ContentPanel = <DetailsView searchResult={searchResults} />;

    return (
        <Box height="100%" display="flex" flexDirection="column">
            <Title />
            <hr />
            <Box flexGrow="1" position="relative">
                { contentPanel }
            </Box>
        </Box>
    )
}

function App(){
    return(
        <Routes>
            <Route path="/" > 
                <Route index element={<Home />} />
            </Route>
        </Routes>
    )
}

export default App
