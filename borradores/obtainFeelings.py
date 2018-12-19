import requests
http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "GHXsh3Reqt-FKu5Mbjw9NtUXeG-TUsrM"
secret = "HvD3fbbVWiL3aquA6pDvO-GjIa9nYQ-i"
image = {}  # inicialización de la variable vacía

# parameters
image_file = './prueba.jpg'
image_url = 'https://t1.uc.ltmcdn.com/images/8/5/3/img_como_usar_el_aceite_de_arbol_de_te_en_la_cara_43358_600.jpg'
image_type = 'url'
attributes = 'emotion'

data = {
    'api_key': key,
    'api_secret': secret,
    'image_url': image_url,
    'return_attributes': attributes
}

if image_type == 'file':
    image = {'image_file': open(image_file, 'rb')}
else:
    data['image_url'] = image_url


def obtainFeelings():
    feelings = requests.post(http_url, params=data, files=image)
    return(feelings.json())
