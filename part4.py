import requests
 
print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/micheal-chow/Lab1/master/part4.py")

print(r.text)
