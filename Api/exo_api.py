import pandas as pd
import requests as req
from bs4 import BeautifulSoup

def main() :

    ids = column_from_csv("akinator.csv")
    url_ids = get_url_with_id(ids)
    print(url_ids)
    apis_json = get_api_json(url_ids)
    print(apis_json)
    get_name(apis_json)



def column_from_csv(csv) :

    file = pd.read_csv(csv)
    df = pd.DataFrame(file)
    ids = list(df["github name"])

    return ids

def get_url_with_id(ids) :

    url_ids = []

    for i in ids :
        if i != "nan" :
            url_ids.append(f"https://api.github.com/users/{i}")

    return url_ids


def get_api_json(url_ids) :
    apis_json = []
    for i in url_ids :
        api = req.get(i)
        api_json = api.json()
        apis_json.append(api_json)

    return apis_json

def get_name(apis_json) :

    for api_json in apis_json :

        for i in api_json :

            if i == "name" :

                print(api_json[i])

main()
