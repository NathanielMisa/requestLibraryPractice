# following nick russo video
import requests


def get_meraki(resource):
    api_path = "https://api.meraki.com/api/v1"
    headers = {
        "Content": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

    }
    get_response = requests.get(f"{api_path}/{resource}", headers=headers)
    get_response.raise_for_status()
    return get_response.json()


def main():
    orgs = get_meraki("organizations")
    devnet_id = 0
    for org in orgs:
        print(f"ID: {org['id']:<6} Name: {org['name']}")
        if "devnet" in org["name"].lower():
            devnet_id = org["id"]

    if devnet_id:
        networks = get_meraki(f"organizations/{devnet_id}/networks")

    print(f"\nNetworks seen for DevNet org ID {devnet_id}: ")

    devnet_network = ""
    for network in networks:
        print(f"Network ID: {network['id']} Name: {network['name']}")
        if "devnet" in network["name"].lower():
            devnet_network = network["id"]

    if devnet_network:
        devices = get_meraki(f"networks/{devnet_network}/devices")
        print(f"\nDevices seen on DevNet network {devnet_network}: ")

        for device in devices:
            print(f"Model: {device["model"]:<8} ip: {device['lanIp']}")


if __name__ == '__main__':
    main()

#a
