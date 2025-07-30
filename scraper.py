import requests
from bs4 import BeautifulSoup

def obtener_precio(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    precio = soup.find('span', {'class': 'price'})
    print("Precio:", precio.text if precio else "No encontrado")

obtener_precio("https://example.com")
