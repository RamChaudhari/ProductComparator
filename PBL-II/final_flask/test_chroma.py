import requests
from icecream import ic


def get_details(product):
    details = {}

    details['productName'] = product.get('name')
    # details['mrp'] = product.get('mrp').get('formattedValue')
    details['productPrice'] = product.get('price').get('formattedValue')
    # details['discount'] = product.get('discountValue')
    # details['availability'] = product.get("stock").get('stockLevelStatus')
    details['productRating'] = product.get("finalReviewRating")
    details['productURL'] = "https://croma.com" + product.get('url')
    details['productImage'] = product.get('plpImage')

    return details
    # print(product)


def print_details(product_details):
    print(product_details)
    exit()
    print(f"Name: {product_details.get('name')}")
    print(f"Availability: {product_details.get('availability')}")
    print(f"Rating: {product_details.get('rating')}")
    print(f"MRP: {product_details.get('mrp')}")
    print(f"Selling Price: {product_details.get('price')}")
    print(f"Discount: {product_details.get('discount')}")
    print(f"URL: {product_details.get('url')}")


def search(query):
    headers = {
        'Host': 'api.croma.com',
        'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://www.croma.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.croma.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = {
        'currentPage': '0',
        'query': query,
        'fields': 'FULL',
    }

    response = requests.get(
        'https://api.croma.com/product/allchannels/v1/search', params=params, headers=headers)

    products = response.json().get('products')
    product_info = [get_details(product) for product in products[:5]]

    # ic(product_info)
    return product_info

# ic(search("one plus nord ce"))
