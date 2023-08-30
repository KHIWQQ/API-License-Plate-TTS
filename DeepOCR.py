import requests
 
url = "https://api.aiforthai.in.th/panyapradit-ocr"
 
files = {'uploadfile':open('6.jpg', 'rb')}
 
headers = {
    'Apikey': "hPVns5FnJHma0iYoJ9TFvIbtLlxAoSlc",
    }
 
response = requests.post(url, files=files, headers=headers)
 
print(response.json())