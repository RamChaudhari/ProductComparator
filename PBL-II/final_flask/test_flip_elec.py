from json import dumps, loads
from bs4 import BeautifulSoup
import requests
import pandas as pd

def flipElect(product):
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=TI168258682630600001348045028741262154980030966209289738676196919980; K-ACTION=null; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19475%7CMCMID%7C72675547173909686763485602278663433223%7CMCAAMLH-1683191630%7C12%7CMCAAMB-1683191630%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1682594030s%7CNONE%7CMCAID%7CNONE; _pxvid=d1356a83-e4db-11ed-a208-794d4b766e76; pxcts=d1357a65-e4db-11ed-a208-794d4b766e76; Network-Type=4g; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE2ODQzMTQ4MzAsImlhdCI6MTY4MjU4NjgzMCwiaXNzIjoia2V2bGFyIiwianRpIjoiZmY1NjRmMGQtMGY2OC00OGViLWIwYWItNzVmNDQxMjY3YjlmIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjgyNTg2ODI2MzA2MDAwMDEzNDgwNDUwMjg3NDEyNjIxNTQ5ODAwMzA5NjYyMDkyODk3Mzg2NzYxOTY5MTk5ODAiLCJrZXZJZCI6IlZJNzUwQzJGOThCQUY3NDg0MEJCNjQ5MzE3NUZGNkQwNUUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.pmsplw0Jyxf-aLkYiMThvqZxDGp0MJhq93MuHSqSVUQ; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fsearch%25253Fq%25253Done%25252Bplus%25252Bnord%25252B2t%252526as%25253Don%252526as-show%25253Don%252526otracker%25253DAS_Query_HistoryAutoSug%2526ot%253DA; qH=e5c23c36adf1b0de; __pxvid=ae0156fb-e4de-11ed-abfa-0242ac120002; SN=VI750C2F98BAF74840BB6493175FF6D05E.TOK031395F6E3F646F78EDACC6E3E324475.1682588062.LO; S=d1t14TT8/AhE/PyBjP20/Pz8/P5nhMstJMH9rgG+B62qGv42USq5OFNxGQx4B4wS77MmfnrFQEmfgAsVRyLjZ1NmY0w==; _px3=68f01d3d88d333cd422bf0c748124faa05e872f2c634bb1effc0d422450b7c45:9RomqLxwGW/4EuOSUUtOgegQvP/TD2gS7OIXbtI0+OjlFGcIhXMNdMPTkjGkp9imOJqpZamzrsYPFV6DIh37zw==:1000:7XKe2T4TN7AlYVxalRmOKfDTTYhpTc4EZadCI3HOr2HIy/Ac3hcZvIGDp+sTG+QZukfsUuZeNNUIPEIR4XCT8x9eZJC5u/L1UcL+7rIjfLolY3fEaFemFhJAcCITBlw251bc0SEcCMgDGUJKICV+vFlqM+HhCA6Fe/LAlpQ1pA0LNJxWMMo6x+HajapdU/RN7Vx1xTO+s0POWe4PxYXCLg==',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    params = {
    'q': product,
    'as': 'on',
    'as-show': 'on',
    'otracker': 'AS_Query_HistoryAutoSuggest_1_1_na_na_na',
    'otracker1': 'AS_Query_HistoryAutoSuggest_1_1_na_na_na',
    'as-pos': '1',
    'as-type': 'HISTORY',
    'suggestionId': ' ',
    'requestId': 'e531d899-5524-4ec2-8596-e1299140aa92',
    }

    response = requests.get('https://www.flipkart.com/search', params=params, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # Product names # # #
    productName = []
    names = soup.find_all("div", class_ = "_4rR01T")

    for i in range(5):
        name = names[i].text
        productName.append(name)

    # # # Product prices # # #
    productPrices = []

    prices = soup.find_all("div", class_ = "_30jeq3 _1_WHN1")

    for i in range(5):
        price = prices[i].text
        productPrices.append(price)

    # # # Product reviews # # #
    productReviews = []

    reviews = soup.find_all("div", class_ = "_3LWZlK")

    for i in range(5):
        review = reviews[i].text
        productReviews.append(review)

    # # # Product ratings # # # 
    productRatings = []

    ratings = soup.find_all("span", class_ = "_2_R_DZ")

    for i in range(5):
        productRatings.append(ratings[i].get_text())   

    diff_rating = len(productPrices) - len(productReviews)
    productReviews += ["-" for i in range(diff_rating)]

    diff_reviews = len(productPrices) - len(productRatings)
    productRatings += ["-" for i in range(diff_reviews)]

    # # # Product links # # #
    productLinks = []

    links = soup.find_all("a", class_ = "_1fQZEK")
    for i in range(5):
        link = links[i].get("href")
        productLinks.append("https://www.flipkart.com" + link)

    # # # Product images # # #
    productImages = []

    images = soup.find('img', attrs = {'class' : '_396cs4'})['src']
    for i in range(5):
        productImages.append(images)

    # # # Creating a dataframe # # #
    df = pd.DataFrame({"productName":productName, "productPrice":productPrices, "Ratings":productReviews, "Reviews":productRatings, "productURL":productLinks, "productImage":productImages})
    # print(df)

    # # # Converting dataframe to json # # #
    result_init = df.to_dict()
    result = [{
        'productName': productName[i],
        'productPrice': productPrices[i],
        'productRating': productReviews[i],
        'productImage': productImages[i],
        'productURL': productLinks[i]
    } for i in range(5)]
    # parsed = loads(result)
    # print(dumps(parsed, indent=4))

    return result

if __name__ == '__main__':
    print(flipElect("laptop"))