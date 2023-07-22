
from bs4 import BeautifulSoup
import requests
import json

def search(search_term):

    URL = 'https://www.amazon.in/s?k=' + search_term

    HEADERS = {
        'authority': 'www.amazon.in',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        # 'cookie': 'session-id=261-8655342-5464504; urtk=%7B%22at%22%3A%22Atna%7CEwICIPUQMuzlW1Z6-VrxXKhouAmEYxXRpyNtvZUCsliT1Q1aVRbdvku1tNBHS4FrsEQqKe5pqtqU4GzMT6paV1uIwCDLnw2dviNnwr10opA6IQYEeP91VMrVwK-a5d4Fq_VebajC1Ouq7nmHPhFa2dmMrv-hO3ERiUM5pw1MpeGevzN7Wl6owkDSidwPAEgGBoHLRJK2Gcz3lERvNE6TAhBukE8iXW3EjbrHtGkULiGyzZnIc3CaMJouu0WcQYiCQqUQ90CgbeNPFrMBhuihAABiFG8puPLURQbrP5HgUjOs2mY7s7dMEP5EumVC-tjMuhfl-74%22%2C%22atTtl%22%3A1678045110760%2C%22rt%22%3A%22Atnr%7CEwICIGIcIZ4LVIlmiadU2-z7Ge_0eUH3aIvfz12TrnMJ3gxHeTF8mKaeWg086dA3lkZ2aCa8ntAx13hKexNg_6JjjoO4JDRZlR-zd6hxEZt4Peedtiw1Ays5aDCtNpQm1jFwoBEt6usiKpGyC7SkcxyengFaRlq-Uc7vmogLqmHhij-jsH4-XF6W9VXoWE4Y7vxOCXRzS_zTi2PY14AnD0fGhQ-LisNImDl5b3C9xBMnqH9dG4O6PmDZn8mOlVs9-Kdj2Fof9qWHJtvJ_HZ-QUq0emd7CYUN1HR535xFbS11j5XARXLYGDuf20CI9I79hHbqNDE-pCtXd2Vk54eecDdC2VID%22%7D; ubid-acbin=262-4291680-7227235; lc-acbin=en_IN; x-acbin="rDBfP4lsd9o@1D40p2cdB91pE7KDLrd9MtGn2LBnjG7M01uxa1NmkltS7hbnkxtv"; at-acbin=Atza|IwEBIIw-XEu9-Gm_hMSaXJ7Jfz-84GgYNS-9AZqGMdCro17AX4pJATl99A8wRx9atURjAFvrB6TZgdGly2t3zXYvQ7JS9uzzDfNFPzbWgqcG34-ISGK3Evu98PkHPElRzaFskPaxlfBKxU6uYUZ8kNVoHEKePBkwbWpShkU8Wq5SO2GRn2YiufRo0w8caU7zoTDvLOsIc27uNBfSCnjgopv1QnwEE1gKIne2XFIGFkQkckG37ij9gzUjGoNv-AOvf4FNF-0; sess-at-acbin="mCXhXbLBqa/Ff5ErpLQDoLZ55A4V2i2uVh06XjYXfS0="; sst-acbin=Sst1|PQEOJpkuPTyjuVQmSZwgjRwNCTgLBZARHr1cvM2P_lO6MANK0PJ_UX4oC3h84iYt8v2vqshth5PNuIjo1Gqbs-9zgTflgh-i5b0IpJDQhRhUz3xVFdMfSYmP9CS65hrZuS-3HiQbSnE7xjISh9Y7bDs1JcHpiVwMUoCGE2Oo-sKX1RSA8SqlOnES2Yr2lj05NZCYzsI87B2HOoWfWO4yHUALE6wlxXAkYRjUfxmbolpGeNuFSKSp-PZgD1V4MMzeo6HVKiEqnY1bm8Y_lItWostcSx4hcwmMHegKZzhx3WjGeLU; session-id-time=2082787201l; i18n-prefs=INR; s_cc=true; s_ppv=83; s_vnum=2110636960497%26vn%3D2; s_sq=%5B%5BB%5D%5D; s_nr=1678713898289-Repeat; s_dslv=1678713898291; session-token=gzspJtXGsfm2ByZPe2zVZYJ4E0iHf5VFY3qZ3w17WYJvybkNdaxU11UUu55kf2i5nh7XpOhNlcTIiqvA3vrgFha09T65j7pV6ojP2eo7WhBQox2qddswDv8KBi8WfeZCmMak/Np6LAAvET0vnO6ryW9/M4rw/6gaSOtsOXSiaqqYa3uYF51wSgmCPoUByN4TQP3GzAoXUm4YiVEv5V78bDfWLuYhh+c+mEPvCqNqyZzWlPe2SMhCwg==; csm-hit=tb:s-FX5M2HB8KMQ6K04MBQ67|1684683104230&t:1684683108274&adb:adblk_no',
        'device-memory': '8',
        'dnt': '1',
        'downlink': '1.4',
        'dpr': '1',
        'ect': '4g',
        'pragma': 'no-cache',
        'rtt': '300',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-viewport-width': '1920',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'service-worker-navigation-preload': 'true',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'viewport-width': '1920',
    }

    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    # Products
    
    products = soup.findAll('div', attrs={"data-component-type": "s-search-result"})

    return_products = []

    for product in products[:5]:
        product_name = product.find('span', attrs={"class": 'a-size-medium a-color-base a-text-normal'}).text.strip()
        product_price = product.find('span', attrs={"class": 'a-price'}).find('span', attrs={"class": 'a-offscreen'}).text.strip()
        product_rating = product.find('span', attrs={"class": 'a-icon-alt'}).text.strip().split()[0]
        product_img = product.find('img', attrs={"class": 's-image'})['src']
        product_url = product.find('a', attrs={"class": 'a-link-normal'})['href']

        current_product = {
            'productName': product_name,
            'productPrice': product_price,
            'productRating': product_rating,
            'productImage': product_img,
            'productURL': "https://amazon.in/" + product_url,
        }

        return_products.append(current_product)

    return return_products


if __name__=='__main__':
    print(search("oneplus nord ce2"))