import requests
 
url = "https://api.aiforthai.in.th/lpr-v2"
payload = {'crop': '1', 'rotate': '1'}
files = {'image':open('rod.jpg', 'rb')}
 
headers = {
    'Apikey': "hPVns5FnJHma0iYoJ9TFvIbtLlxAoSlc",
    }
 
response = requests.post( url, files=files, data = payload, headers=headers)
 
print(response.json())
A = response.json()
payload = A[0]
tabain = payload["lpr"]
print(tabain)

from gtts import gTTS
import os

tts=gTTS(text='รถทะเบียน'+tabain,lang='th')
tts.save('Hello.mp3')

file = "Hello.mp3"
print("Play mp3")
os.system("mpg123 "+file)

# def listToString(s):
#     str1 = "" 
#     for ele in s:
#         str1 += ele
#     return str1

# payload = A[0]
# tabain = payload["lpr"]
# print(tabain)
# word = list(tabain)
# thai_number = {"ก":"กอไก่",
# "ร":"รอเรือ","0":"ศูนย์", "1":"หนึ่ง", "2":"สอง", "3":"สาม", "4":"สี่", "5":"ห้า", "6":"หก", "7":"เจ็ด", "8":"แปด", "9":"เก้า"}
# wordToSpell = listToString([[v for k,v in thai_number.items() if k in str(y)][0] or 'no match' for y in word])
# print("wordToSpell:",wordToSpell)

# cvt = tabain[0]+"อ"+tabain[1]+"อ"
# Z = tabain[2]
# X = tabain[3]
# C = tabain[4]
# V = tabain[5]

# two = thai_number[Z]
# three = thai_number[X]
# four = thai_number[C]
# five = thai_number[V]

# if tabain[2] in (thai_number): 
#   cvt = tabain[0]+"อ"+tabain[1]+"อ"+ two

# if tabain[3] in (thai_number):
#   cvt = tabain[0]+"อ"+tabain[1]+"อ"+ two + three

# if tabain[4] in (thai_number):
#   cvt = tabain[0]+"อ"+tabain[1]+"อ"+ two + three + four

# if tabain[5] in (thai_number):
#   cvt = tabain[0]+"อ"+tabain[1]+"อ"+ two + three + four + five
#   print(cvt)  

# test = "กอไก่ รอเรือ ห้า เก้า หก ห้า"
# from pythaitts import TTS
# tts = TTS()
# file = tts.tts(wordToSpell, filename="cat.wav") # It will get wav file path.
# # wave = tts.tts(cvt,return_type="waveform") # It will get waveform.

# import os
 
# file = "cat.wav"
# print('playing sound using native player')
# os.system("aplay " + file)


