""" code learnt from Nick Russo """

import requests

def get_token():
    api_path = "https://sandboxdnac.cisco.com/dna"
    auth = ("devnetuser", "Cisco123!")
    headers = {"Content-Type": "application/json"}

    auth_resp = requests.post(f"{api_path}/system/api/v1/auth/token,", auth=auth, headers=headers)

    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return token

def main():
    token = get_token()
    print(token)


if __name__ == "__main__":
    main()

    