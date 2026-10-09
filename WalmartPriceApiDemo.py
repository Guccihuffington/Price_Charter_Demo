import json

def search_walmart(counter):
    with open('Walmart_output.json') as fp:
        data = json.load(fp)
    results = data.get("results", [])
    platform = data.get("platform")
    if platform == "walmart_search":
        if counter > len(results)-1:
            counter = len(results)-1
            product = results[counter]
            Walmart_Name = product.get("name")
            Walmart_Price = product.get("price")
            Walmart_Url = product.get("url")
            Walmart_Thumbnail = product.get("thumbnail")
            return Walmart_Name,Walmart_Price,Walmart_Url,Walmart_Thumbnail
        elif counter < 0 :
            counter = 0
            product = results[counter]
            Walmart_Name = product.get("name")
            Walmart_Price = product.get("price")
            Walmart_Url = product.get("url")
            Walmart_Thumbnail = product.get("thumbnail")
            return Walmart_Name,Walmart_Price,Walmart_Url,Walmart_Thumbnail
        else:
            product = results[counter]
            Walmart_Name = product.get("name")
            Walmart_Price = product.get("price")
            Walmart_Url = product.get("url")
            Walmart_Thumbnail = product.get("thumbnail")
            return Walmart_Name,Walmart_Price,Walmart_Url,Walmart_Thumbnail
    else:
        print("No Walmart Data to Provide the results for")

