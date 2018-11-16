# Estuve probando para pasarle imágenes a la API de face++ y por medio de un archivo hay que pasarlo como
# multipart/form-data y no se como se hace y si se lo pasas como URL te cambia las / y no lo encuentra.
# Probablemente sea una tontería, pero no lo veo, si ejecutáis el código veis la petición que hace y el error 400.

import requests

http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "GHXsh3Reqt-FKu5Mbjw9NtUXeG-TUsrM"
secret = "HvD3fbbVWiL3aquA6pDvO-GjIa9nYQ-i"
# parameters
image = "https://upload.wikimedia.org/wikipedia/commons/d/d7/Mariano_Rajoy_in_2018.jpg"
attributes = 'emotion'

print(image)

data = {
        'api-key': key,
        'api-secret': secret,
        'image_url': image,
        'return_attributes': attributes
        }

r = requests.Request('POST', http_url, params=data)
prepared = r.prepare()

a = requests.post(http_url, params=data)
print(a.status_code, a.reason)

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

pretty_print_POST(prepared)
