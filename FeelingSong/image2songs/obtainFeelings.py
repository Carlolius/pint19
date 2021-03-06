import requests
http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "1jz_rcd_Fv5zm5ZYrP6mmRs3Tt0L1pG2"
secret = "cY6uVoAA_57vpcD_mY9F6gaPVjmnQNqv"


def obtainFeelings(request,imagen):
    # parameters
    image = {}  # inicialización de la variable vacía
    image_file = imagen
    image_url = imagen
    attributes = 'emotion'

    data = {
        'api_key': key,
        'api_secret': secret,
        'image_url': image_url,
        'return_attributes': attributes
    }

    if request.method == 'POST':
        image = {'image_file': open(image_file, 'rb')}
    else:
        data['image_url'] = image_url

    feelings = requests.post(http_url, params=data, files=image)
    return(feelings.json())
