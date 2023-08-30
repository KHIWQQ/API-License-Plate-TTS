tabain = 'ศข9922'
thai_number = {"0":"ศูนย์", "1":"หนึ่ง", "2":"สอง", "3":"สาม", "4":"สี่", "5":"ห้า", "6":"หก", "7":"เจ็ด", "8":"แปด", "9":"เก้า"}



# print(type(thai_number))
# print(thai_number[0])

# one = print(tabain[0])

cvt = tabain[0]+"อ"+tabain[1]+"อ"
# print(cvt)
# print(type(tabain[2]))

Z = tabain[2]
X = tabain[3]
C = tabain[4]
V = tabain[5]

two = thai_number[Z]
three = thai_number[X]
four = thai_number[C]
five = thai_number[V]
# print(type(Z))


if tabain[2] in (thai_number): 
#   print(two)
  cvt = tabain[0]+"อ"+tabain[1]+"อ"+ two
#   print(cvt)
  

if tabain[3] in (thai_number):
#   print(three)
  cvt = tabain[0]+"อ"+tabain[1]+"อ"+ two + three
#   print(cvt)

if tabain[4] in (thai_number):
#   print(four)
  cvt = tabain[0]+"อ"+tabain[1]+"อ"+ two + three + four
#   print(cvt)

if tabain[5] in (thai_number):
#   print(five)
  cvt = tabain[0]+"อ"+""+tabain[1]+"อ"+""+ two + three + four + five
  print(cvt)  


# import required module
import os
 
# play sound
file = "cat.wav"
print('playing sound using native player')
os.system("aplay " + file)