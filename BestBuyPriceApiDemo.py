import json

def search_bestbuy(counter):
    with open('BestBuy_output.json') as fp:
        data = json.load(fp)
    results = data.get("results", [])
    platform = data.get("platform")
    if platform == "bestbuy_search":
        if counter > len(results)-1:
            counter = len(results)-1
            product = results[counter]
            BestBuy_Name = product.get("name")
            BestBuy_Price = product.get("price")
            BestBuy_Url = product.get("url")
            BestBuy_Thumbanil = product.get("thumbnail")
            return BestBuy_Name,BestBuy_Price,BestBuy_Url,BestBuy_Thumbanil
        elif counter < 0 :
            counter = 0
            product = results[counter]
            BestBuy_Name = product.get("name")
            BestBuy_Price = product.get("price")
            BestBuy_Url = product.get("url")
            BestBuy_Thumbanil = product.get("thumbnail")
            return BestBuy_Name,BestBuy_Price,BestBuy_Url,BestBuy_Thumbanil
        else:
            product = results[counter]
            BestBuy_Name = product.get("name")
            BestBuy_Price = product.get("price")
            BestBuy_Url = product.get("url")
            BestBuy_Thumbanil = product.get("thumbnail")
            return BestBuy_Name,BestBuy_Price,BestBuy_Url,BestBuy_Thumbanil
    else:
        print("No Bestbuy Data to Provide the results for")