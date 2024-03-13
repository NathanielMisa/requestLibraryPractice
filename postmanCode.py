import requests

url = "https://www.postman-echo.com/get"

payload = {}
headers = {
    'Cookie': 'sails.sid=s%3AdXxCWyRsOdHZXTuAIMzUkf0o6BsAfdRw.vlSV64QlqPQYOBKPBqkqgp8qjVMfeYrblLXijUEN5AY'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
