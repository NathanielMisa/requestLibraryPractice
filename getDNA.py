import requests
import json
from tokenCode import get_token


def jsonFunc(myFile):
    extract = myFile.json()
    for i in extract["response"]:
        print(f"{i['type']} with a Mac Address of {
              i['macAddress']} | ID: {i['id']}")


print("running")


def main():
    token = get_token()
    api_path = "https://sandboxdnac.cisco.com/api/v1/network-device"
    headers = {"Content-type": "application/json", "X-Auth-Token": token}

    get_resp = requests.get(
        f"{api_path}", headers=headers, verify=False)

    jsonFunc(get_resp)


if __name__ == "__main__":
    main()
