import json
def search_amazon(counter):
    with open('Amazon_output.json') as fp:
        data = json.load(fp)
    results = data.get("results", [])
    platform = data.get("platform")
    if platform == "amazon_search":
        if counter > len(results)-1:
            counter = len(results)-1
            product = results[counter]
            Amazon_Name = product.get("name")
            Amazon_Price = product.get("price")
            Amazon_Url = product.get("url")
            Amazon_Thumbnail = product.get("thumbnail")
            return Amazon_Name,Amazon_Price,Amazon_Url,Amazon_Thumbnail
        elif counter < 0 :
            counter = 0
            product = results[counter]
            Amazon_Name = product.get("name")
            Amazon_Price = product.get("price")
            Amazon_Url = product.get("url")
            Amazon_Thumbnail = product.get("thumbnail")            
            return Amazon_Name,Amazon_Price,Amazon_Url,Amazon_Thumbnail
        else:
            product = results[counter]
            Amazon_Name = product.get("name")
            Amazon_Price = product.get("price")
            Amazon_Url = product.get("url")
            Amazon_Thumbnail = product.get("thumbnail")            
            return Amazon_Name,Amazon_Price,Amazon_Url,Amazon_Thumbnail
    else:
        print("No Amazon Data to Provide the results for")
