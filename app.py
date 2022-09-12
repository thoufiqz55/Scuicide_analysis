import json
import requests
headers = {"Authorization": "Bearer ya29.A0ARrdaM9XBvjXdL8WNZAgdn6lteXsw2K-APkhV6fSJhb8l7lxu00KxdeHkP_6I_wv0nAmojbW_5sIp42LJKiIM3ouZv4YWC-YDNWpIFysheAzaSbv_OO1lYFDiVR0vG9wDV4YgUIIOudNfY-86KeBrCBZBjBZ"}
para = {
    "name": "sampled.jpg",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./profile1.jpg", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
