import requests
from icecream import ic
# search_title =input("Enter the title of the product: ")


def get_details(product):
    details = {}
    details['productName'] = product.get('title')
    details['productPrice'] = product.get('price')
    details['productImage'] = product.get('image')[0].get('src')
    details['productURL'] = "https://www2.hm.com"+product.get('link')
    # print(product)
    return details


def search(query):
    headers = {
        'authority': 'www2.hm.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'preshoppingUser=false; searchType=\'\'; OptanonAlertBoxClosed=2023-03-24T04:05:34.324Z; agCookie=4984ee9f-7a44-487e-ba0e-d8654ab7ed62; hm-india-cart=96cb3813-1822-4ca9-b06b-e31acf081e1b; akainst=APAC; INGRESSCOOKIE=1683035017.515.69.26606|7bbf721d92a09b08c42eb8596390c8cc; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+02+2023+19%3A13%3A39+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&isIABGlobal=false&hosts=&consentId=4a25b8b9-a88c-46a6-bb4b-07f44acce342&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; bm_sz=B80FCAE70A97A791C6BB3D3E5221B725~YAAQH9ksMd2ELOaHAQAAi2r26RPMC9q+7Wkc1+wSRWGotg9mTjmqJMDtXKgH75XgR1OtbBzTKsxWd/ern4GAB3RE3BwFvadc2bEE73zxGSqOx60ho2uvMgy/8kuTJTaSQd0qjOrrMBg6xyFMRiNsTSmxhJuGocumA62r+lTqf6njMJrBxAH34TKtEUrUxDY2y0MxlqdqNIb0DJC7NNhhFGIc5VuP58MUjWLhVHU/UkS4npknPy/FC0jLMCRfMmbJWjLXKT8Zfa2GNRR18M17G13xjN+7dfC3WJfV6077mw==~3359302~3294017; bm_mi=A029CA17E85ACB0F63099E6F4F4B861C~YAAQH9ksMaWFLOaHAQAARb326RMbz3Qh0sNOkxlNWUHHci8SGvZJdKgxkigsDBwSUPK9xAHUB27bsZ48SxQ8i4qBwNIEhYHufJ6mYXkDREfuA3zPIyMaK0z2apmFxnHb3a6kA/JGyQC7a3odqNfz3Duonq/nDdCm2M7LagNj3DWC7MRSRDb6HEwxFfN9Mu9XdcZBAvor6vUTEZokseCY53mEIgLBIHfa+G6KG6aARvWPkeSbkGpi5vmjo8b342f7qQYYb15GxJvNBrJSEfaxctZP4HEjxHXywhUBNPkWMA8XYUm+frthJco2PxJf4joX9w5l4tBmYaMD/OHEZy/Jdsh256ycUNB8fe7b1TaG~1; JSESSIONID=AD8F1394F4CF93A9196C23EF44ABC2664C307A30697B5E07DAC0F8D26B90CCC82C81CCA61BB3F9C9BD629CFAA2696C18550DF33671CF2D8C474E379192D8C85D.hybris-ecm-web-8696554db7-b45pv; hm-india-favourites=""; userCookie=##eyJjYXJ0Q291bnQiOjB9##; ak_bmsc=E94D7F8B500C94029A01A7385BA6316F~000000000000000000000000000000~YAAQH9ksMcCFLOaHAQAAR8r26RNMaSnSha0uG8I9lf/i1fVFBYzpva3v/9dEUfCUS7PbDAwkqmVFgmdt2NoqCUanr6p42J4HHUwc5eYQJDywq93pYehmm/SItrX2anfcG0zPt9qC5pZaTFfZw5GRJp6+i3zBrKrdil5euu5scAVKGEMbUMw9oObUTK3+8ec+bCq5GiqBLiVtGTa85tKXPelwC2exEil7lyNLdwhssvcrvEPr3kkOf+X0EgWHM8sG/8i0C8/S23RIcZGyLfjhBqcmJTFdtgeCQBlr8vFjlr2tflbExxzFRJSQuK3myV7h3ybgxsER96hir8qRex4ZRRlDpqdx6YW4ksGkEcN08fm6XjIeoPtCj9qOEjqlm45GU3GhBlZy4PYuvRb+8pQBj1CoqhtWAysRi0QCMKFS5pw31yMsKrryPNJwtgkCbSYVMWSJGvz0aDSuJyyedokKWRnFg7DXAEdbYE2V+yVa8Nn7VD01ZL1f; _abck=86488D94E41C1303ED1A128ADD56B0E8~0~YAAQF/Y3F6f/UKGHAQAA/uI36gmuPXxLN1sWHh19KetuXx3L8jZ7CLUIDblXAJnbhlMVeyc1wU7RHPZdIzKlbQgDc7c2dxkqqEoUV5oDTNl1XGo3H91tqMv5vJlKHDbfLru4OW4VoI52DXHouvRARFSOVRmGQcoHIyDsOKKBSoYb3GAq+8wFGYfdWQCESjzMis6fvkYz3RbLOLZznzYvmYJOQBZlchoqUIXTk6S1jrrAV4+H/kKqpRRLwrLzb4dkiqp+7/VomybXj3vPTbHqkPbBIqelNBr53hQ80FL3ZB09q9HxuEZGfNouQvoLh1DPehpYoAkEfRcFdRYfHEKzEE15hZuvQrpOzIn6wkKj9pKPCjCZkkT2LP0Rbm5iq1nX9yr+8V7J1L+8xaj35M1E41nJwq8=~-1~-1~1683265303; AKA_A2=A; searchType=AUTOSUGGESTION; akamref=en_in; akavpau_www2_en_in=1683263842~id=5a65e6a3a697b1ff5c2af46114a4ad54; bm_sv=C2339B336B5EF84F5BF65909C9FBCC4C~YAAQF/Y3FzIIUaGHAQAAL1ZT6hPCEYlyI4Wx2EUaau4V+s+/vhlHZ4QCeooOLQgEradAZzr4lG2mzQsd9dhqkWp9e/AZkQMdTBGQPv3+Kqxc92xjtG+R5vNuVd8TR7Sg2C4K6cKdd+tuxThMypOw8G3a97yv6G4wtCsjVlGow0/3hLvkVNXxZDmtjrcmVlbEIELOhZhZMdBWAVg3ZIBOs2BrSLo4dgjqQ019WKc5tPLKQpZqrpGXR7K1D+F6~1; RT="sl=2&ss=lha2qj6w&tt=7fc&z=1&dm=hm.com&si=4a3501f4-35f4-4365-907a-17b2d4fc25a0&bcn=%2F%2F684d0d43.akstat.io%2F&ld=wz8o"; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+05+2023+10%3A42%3A23+GMT%2B0530+(India+Standard+Time)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=4a25b8b9-a88c-46a6-bb4b-07f44acce342&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; utag_main=v_id:018711cafe9a008960280d7b6c980506f0024067007e8$_sn:21$_se:106$_ss:0$_st:1683265355418$c_consent:C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0$ses_id:1683257460480%3Bexp-session$_pn:12%3Bexp-session$ses_id_r:s_4913656851062771.1683257460480%3Bexp-session$segment:normal%3Bexp-session$cart_active:No%3Bexp-session$prevpage:%2FSEARCH%2FSEARCH_PAGE%3Bexp-1683267142786',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'q': query,
        'sort': 'stock',
        'image-size': 'small',
        'image': 'stillLife',
        'offset': '40',
        'page-size': '40',
    }

    response = requests.get(
        'https://www2.hm.com/en_in/search-results/_jcr_content/search.display.json',
        params=params,
        headers=headers,
    )
    products = response.json().get('products')
    product_info = [get_details(product) for product in products[:5]]

    return product_info

# ic(search("satin dress"))
