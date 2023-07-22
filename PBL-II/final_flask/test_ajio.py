import requests
from icecream import ic
import json
def get_details(product):
    details={}
    details['productName']= product.get('name', "")
    details['productPrice'] = product.get('price').get('formattedValue', "")
    details['productImage'] = product.get('images')[0].get('url', "")
    details['productURL'] = "https://ajio.com" + product.get('url', "")
    return details

def search(query):
    

    headers = {
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'Referer': 'https://www.ajio.com/search/?text=satin%20dress',
        'ai': 'www.ajio.com',
        'os': '4',
        'vr': 'WEB-1.15.0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = [
        ('fields', 'SITE'),
        ('currentPage', '0'),
        ('pageSize', '45'),
        ('format', 'json'),
        ('query', query),
        ('sortBy', 'relevance'),
        ('text', 'satin dress'),
        ('gridColumns', '3'),
        ('facets', 'genderfilter:Girls'),
        ('segmentIds', ''),
        ('advfilter', 'true'),
        ('platform', 'Desktop'),
        ('is_ads_enable_plp', 'false'),
        ('is_ads_enable_slp', 'false'),
        ('showAdsOnNextPage', 'false'),
        ('displayRatings', 'true'),
        ('segmentIds', ''),
        ('segmentIds', 'false'),
    ]

    response = requests.get('https://www.ajio.com/api/search', params=params, headers=headers)
    

    
    products = response.json().get('products')
    product_info = [get_details(product) for product in products[:5]]
    return product_info
