from email import header
import requests
import time
from bs4 import BeautifulSoup
import lxml
import os
from os import system
stock=False
def stockChecker():
    bestbuy="https://www.bestbuy.com/site/nvidia-geforce-rtx-4090-24gb-gddr6x-graphics-card-titanium-and-black/6521430.p?skuId=6521430&ref=186&loc=nvidia_site"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }
    response = requests.get(bestbuy, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    find_status = soup.find('button', attrs={'class':'c-button c-button-disabled c-button-lg c-button-block add-to-cart-button'})
    status = find_status.text
    if status.find("Sold Out") !=-1:
        soldout=True
    else:
        soldout=False

    #print(status)
    if soldout==True:
        print("Out of stock")
    if soldout==False:
        print("In stock")

os.system('cls')
stockChecker()
while stock==False:
    time.sleep(60)
    os.system('cls')

    
