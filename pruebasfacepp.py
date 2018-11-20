import requests
http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "GHXsh3Reqt-FKu5Mbjw9NtUXeG-TUsrM"
secret = "HvD3fbbVWiL3aquA6pDvO-GjIa9nYQ-i"
# parameters
image = 'https://upload.wikimedia.org/wikipedia/commons/d/d7/Mariano_Rajoy_in_2018.jpg'
attributes = 'emotion'

data = {
        'api_key': key,
        'api_secret': secret,
        'image_url': image,
        'return_attributes': attributes
        }

a = requests.post(http_url, params=data)
print(a.status_code, a.reason)
print(a.text)
