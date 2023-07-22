import { Box, Button } from "@chakra-ui/react";
import { Input, InputGroup, InputLeftElement, InputRightAddon } from '@chakra-ui/react'
import { Tabs, TabList, Tab, TabPanels, TabPanel } from "@chakra-ui/react";
import { Search2Icon } from "@chakra-ui/icons"

function SearchBar({ searchFunc, searchType }) {
    function keyevent(e){
        if(e.code === "Enter")
            searchFunc();
    }

    return (
        <InputGroup fontSize={30} display="flex" justifyContent="center">
            <Button fontSize="inherit" paddingX="20px" pointerEvents="none" children={<Search2Icon />} borderRightRadius={0} height="100%" />
            <Input id="searchInput" fontSize="inherit" padding="5px" type="text" placeholder="Search" borderRadius={0} outline="none" maxWidth={500} height="100%" onKeyPress={keyevent}/>
            <Input id="searchType" type="hidden" value={searchType} />
            <Button fontSize="inherit" borderLeftRadius={0} borderRightRadius="10px" paddingX="15px" paddingY="15px" onClick={searchFunc} height="100%">Search</Button>
        </InputGroup>
    )
}

function SearchView({ searchFunc, searchType }) {
    const selectedTabStyle = {
        color: 'white',
        'border-bottom': '1px solid lightgreen',
        // margin: '0 25px',
        // 'border-radius': '100px'
    }

    return (
        <>
            <Tabs marginTop="25px" display="none">
                <TabList display="flex" fontSize={30} justifyContent="space-around">
                    {/* <TabList> */}
                    {/* <TabList fontSize={30}> */}
                    <Tab fontSize={30} width="50%" color="slategray" _selected={selectedTabStyle}>Fashion</Tab>
                    <Tab fontSize={30} width="50%" color="slategray" _selected={selectedTabStyle}>Electronics</Tab>
                </TabList>
            </Tabs>
            <Box display="flex" justifyContent="center" margin={20}>
                <SearchBar searchFunc={searchFunc} searchType={searchType} />
            </Box>
        </>
    )
}

export default SearchView;