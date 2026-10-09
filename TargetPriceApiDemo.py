import json

def search_target(counter):
    with open('Target_output.json') as fp:
        data = json.load(fp)
    results = data.get("results", [])
    platform = data.get("platform")
    if platform == "target_search":
        if counter > len(results)-1:
            counter = len(results)-1
            product = results[counter]
            Target_Name = product.get("name")
            Target_Price = product.get("price")
            Target_Url = product.get("url")
            Target_Thumbnail = product.get("thumbnail")
            return Target_Name,Target_Price,Target_Url,Target_Thumbnail
        elif counter < 0 :
            counter = 0
            product = results[counter]
            Target_Name = product.get("name")
            Target_Price = product.get("price")
            Target_Url = product.get("url")
            Target_Thumbnail = product.get("thumbnail")
            return Target_Name,Target_Price,Target_Url,Target_Thumbnail
        else:
            product = results[counter]
            Target_Name = product.get("name")
            Target_Price = product.get("price")
            Target_Url = product.get("url")
            Target_Thumbnail = product.get("thumbnail")
            return Target_Name,Target_Price,Target_Url,Target_Thumbnail
    else:
        print("No Amazon Data to Provide the results for")