import json

def search_samsclub(counter):
    with open('SamsClub_output.json') as fp:
        data = json.load(fp)
    results = data.get("results", [])
    platform = data.get("platform")
    if platform == "samsclub_search":
        if counter > len(results)-1:
            counter = len(results)-1
            product = results[counter]
            SamsClub_Name = product.get("name")
            SamsClub_Price = product.get("price")
            SamsClub_Url = product.get("url")
            SamsClub_Thumbnail = product.get("thumbnail")
            return SamsClub_Name,SamsClub_Price,SamsClub_Url,SamsClub_Thumbnail
        elif counter < 0 :
            counter = 0
            product = results[counter]
            SamsClub_Name = product.get("name")
            SamsClub_Price = product.get("price")
            SamsClub_Url = product.get("url")
            SamsClub_Thumbnail = product.get("thumbnail")
            return SamsClub_Name,SamsClub_Price,SamsClub_Url,SamsClub_Thumbnail
        else:
            product = results[counter]
            SamsClub_Name = product.get("name")
            SamsClub_Price = product.get("price")
            SamsClub_Url = product.get("url")
            SamsClub_Thumbnail = product.get("thumbnail")
            return SamsClub_Name,SamsClub_Price,SamsClub_Url,SamsClub_Thumbnail
    else:
        print("No SamsClub Data to Provide the results for")
