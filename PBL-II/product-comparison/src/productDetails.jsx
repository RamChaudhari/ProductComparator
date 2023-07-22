import { Flex, Box, Image, Text, Heading, Link } from '@chakra-ui/react';
import { Card, CardBody } from '@chakra-ui/react'
import {ArrowForwardIcon} from "@chakra-ui/icons"

const color = "#ff0000"

function ItemCard({ itemDetails, bcolor }) {
  // console.log(bcolor);

  return (
    <Card margin={2} padding="1vw" width={{base: "50vw", md: "300px"}} className="product-card" color={'gray.100'} >
      <CardBody>
        <Image src={itemDetails.productImage} borderRadius={13} maxHeight="300px" objectFit="cover" margin="auto"/>
        <Text className="item-name" fontSize={25}>{itemDetails.productName}</Text>
        {/* <Text><Image display="inline" src='/star.png' width="1em"/></Text> */}
        <Text className="item-Rating" fontSize={20} color="lightgreen" fontWeight={600}>{itemDetails.productRating ? "⭐" + itemDetails.productRating : ""}</Text>
        <Text className="item-price" fontSize={24} fontWeight={500} color="cornsilk">{itemDetails.productPrice}</Text>
        <Link display="flex" target='_blank' href={itemDetails.productURL} justifyContent="end" fontSize={30}><ArrowForwardIcon /></Link>
      </CardBody>

    </Card>
  )
}

function Store({ name, items, bcolor }) {
  console.log(items)

  return (
    <Box className="storeEntry">
      <Heading as="h3" fontSize="2rem" fontWeight={500} textAlign="center" marginY={30} width="100">{name}</Heading>
      <Flex className="store-items" flexDirection={{sm: "row", md: "column"}} gap="30px" width="fit-content">
        {items.map(item => <ItemCard itemDetails={item} key={item.productName} bcolor={bcolor}/>)}
      </Flex>
    </Box>
  )
}

function DetailsView({ searchResult }) {

  const storeNames = searchResult.storeNames;
  const storeItems = searchResult.storeItems;
  const colors = searchResult.colors

  const lenStores = storeNames.length
  // console.log(storeNames)

  return (
      <Flex flexDirection={{base: 'column', md: 'row'}} justifyContent={{md: 'space-evenly'}} width="100%" overflow={{base: "scroll", md: "hidden"}}> 
      {
        storeNames.map(sName => <Store key={sName} name={sName} items={storeItems[sName]} />)
      }
    </Flex>
  )
}

export default DetailsView