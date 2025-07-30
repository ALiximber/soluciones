import requests

r = requests.get("https://api.exchangerate.host/latest?base=USD")
data = r.json()
euros = float(input("USD: ")) * data['rates']['EUR']
print(f"EUR: {euros:.2f}")
