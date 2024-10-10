import requests

url = "https://prod-planservices.flexiroam.com/api/plan/share"
headers = {
    "Host": "prod-planservices.flexiroam.com",
    "content-length": "97",
    "lang": "en-us",
    ##but here ur auth
    "authorization": "Bearer ",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-A528B Build/PQ3A.190605.05081124; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://www.flexiroam.com",
    "x-requested-with": "com.flexiroamx",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.flexiroam.com/",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9"
}

data = {
    #account ID
    "account_id": "UBCS2UUBBR",
    #with MB
    "data_value": 100,
    "sim_plan_id": 4252043,
    "sim_plan_data_txn_id": 4255232
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())  # لطباعة الرد في شكل JSON
