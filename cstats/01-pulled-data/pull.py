import requests
import json

cdata_site = "https://api.coinstats.app/public/v1/coins?skip=0&limit=1000000"


def printj(obj):
    text = json.dumps(obj, sort_keys=True,indent=4)
    print(text)

def get_cdata():
    response = requests.get(cdata_site)
    print(response)

    if response.status_code == 200:
        print("200")
        printj(response.json())
    else:
        print(response.status_code)


def main():
    get_cdata()

main()