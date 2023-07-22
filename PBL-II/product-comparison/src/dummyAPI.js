const APIResponse = {
  'storeNames': [["Amazon", "#33beff"], 
    ["Flipkart", "#33ff49"], 
    ["Croma", "linear-gradient(135deg, rgba(255,255,255, 0.8), rgba(255,255,255, 0.15))"]],

  'storeItems': {
    'Amazon': [
      {
        productName: 'AName1',
        productPrice: 'APrice1',
        productRating: 'ARating1',
        productImage: 'https://m.media-amazon.com/images/I/71AvQd3VzqL._AC_UY218_.jpg'
      },
      {
        productName: 'AName2',
        productPrice: 'APrice2',
        productRating: 'ARating2',
        productImage: 'https://m.media-amazon.com/images/I/71AvQd3VzqL._AC_UY218_.jpg'
      }
    ],
    'Flipkart': [
      {
        productImage: 'https://m.media-amazon.com/images/I/71AvQd3VzqL._AC_UY218_.jpg',
        productName: 'FName1',
        productPrice: 'FPrice1',
        productRating: 'FRating1'
      }
    ],
    'Croma':  [
      {
        productImage: 'https://media.croma.com/image/upload/v1662443638/Croma%20Assets/Communication/Mobiles/Images/251802_on6al4.png',
        productName: 'OnePlus Nord CE2 Lite 5G (6GB RAM, 128GB, Blue Tide)',
        productPrice: '₹18,999.00',
        productRating: 4.7,
        productURL: 'https://chroma.com/oneplus-nord-ce2-lite-5g-6gb-ram-128gb-blue-tide-/p/251802'
      },
      {
        productImage: 'https://media.croma.com/image/upload/v1662443649/Croma%20Assets/Communication/Mobiles/Images/251803_pwadqy.png',
        productName: 'OnePlus Nord CE2 Lite 5G (6GB RAM, 128GB, Black Dusk)',
        productPrice: '₹18,999.00',
        productRating: 4.6,
        productURL: 'https://chroma.com/oneplus-nord-ce2-lite-5g-6gb-ram-128gb-black-dusk-/p/251803'
      },
      {
        productImage: 'https://media.croma.com/image/upload/v1681109083/Croma%20Assets/Communication/Mobiles/Images/270656_k5mn33.png',
        productName: 'OnePlus Nord CE 3 Lite 5G (8GB RAM, 256GB, Chromatic Gray)',
        productPrice: '₹21,999.00',
        productRating: 5.0,
        productURL: 'https://chroma.com/oneplus-nord-ce-3-lite-5g-8gb-ram-256gb-chromatic-gray-/p/270656'
      }
    ]
  },
  'colors': [
    "#ff0000",
    "#00ff00",
    "#ff0000",
]
}

export default APIResponse;