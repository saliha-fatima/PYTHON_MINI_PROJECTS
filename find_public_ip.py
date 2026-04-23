import requests

response = requests.get("https://api.ipify.org")
if response.status_code == 200:
     print("Your public IP address is:", response.text)
else:
     print("Unable to fetch public IP address.")