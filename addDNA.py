# following nick russo's course
import requests
import time
from tokenCode import get_token


def main():
    token = get_token()
    api_path = "https://sandboxdnac.cisco.com/api/v1/network-device"
    headers = {"Content-type": "application/json", "X-Auth-Token": token}

    new_device = {
        "ipAddress": ["10.0.0.1"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "bob",
        "password": "password123!",
        "enablePassword": "password123!",

    }

    add_device = requests.post(
        f"{api_path}", headers=headers, json=new_device, verify=False)

    if add_device.ok:
        print(f"status code: {add_device.status_code}")
        time.sleep(10)

        task = add_device.json()["response"]["taskID"]
        task_resp = requests.get(
            f"https://sandboxdnac.cisco.com/api/v1/task{task}", headers=headers, verify=False)

        if task_resp.ok:
            task_data = task_resp.json()["response"]
            if not task_data["isError"]:
                print("New device added")
            else:
                print(f"Task error: {task_data['progress']}")
        else:
            print(f"Async GET failed, {task_resp.status_code}")
    else:
        print(f"Device failed with code {add_device.status_code}")
        print(f"Failure body: {add_device.text}")


if __name__ == "__main__":
    main()
