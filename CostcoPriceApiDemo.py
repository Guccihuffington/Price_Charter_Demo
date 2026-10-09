import json

def search_costco(counter):
    with open('Costco_output.json') as fp:
        data = json.load(fp)
    results = data.get("results", [])
    platform = data.get("platform")
    if platform == "costco_search":
        if counter > len(results)-1:
            counter = len(results)-1
            product = results[counter]
            Costco_Name = product.get("name")
            Costco_Price = product.get("price")
            Costco_Url = product.get("url")
            Costco_Thumbnail = product.get("thumbnail")
            return Costco_Name,Costco_Price,Costco_Url,Costco_Thumbnail
        elif counter < 0 :
            counter = 0
            product = results[counter]
            Costco_Name = product.get("name")
            Costco_Price = product.get("price")
            Costco_Url = product.get("url")
            Costco_Thumbnail = product.get("thumbnail")
            return Costco_Name,Costco_Price,Costco_Url,Costco_Thumbnail
        else:
            product = results[counter]
            Costco_Name = product.get("name")
            Costco_Price = product.get("price")
            Costco_Url = product.get("url")
            Costco_Thumbnail = product.get("thumbnail")
            return Costco_Name,Costco_Price,Costco_Url,Costco_Thumbnail
    else:
        print("No Costco Data to Provide the results for")
