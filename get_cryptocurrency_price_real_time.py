# -*- coding: utf-8 -*-
"""get_cryptocurrency_price_real_time.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ixA5yAbmS-SWHywTeRJdHHOg8QvFK2Z
"""

# Description: This program gets the price of cryptocurrencies in real timeA

# Import the libraries
from bs4 import BeautifulSoup
import requests
import time

# Get the URL for example:
#     https://www.google.com/search?q=litecoin+price+usd
url = 'https://www.google.com/search?q=bitcoin+price+usd'

# Make a request to the website
HTML = requests.get(url)

#Parse the HTML 
soup = BeautifulSoup(HTML.text, 'html.parser')

# Print soup to find where the text is that contains the price of the cryptocurrency
print(soup.prettify())

# <div class="BNeawe iBp4i AP7Wnd">

# Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):

  # Get the URL for example:
  #      https://www.google.com/search?q=litecoin+price+usd
  url = 'https://www.google.com/search?q='+coin+'+price+usd'

  # Make a request to the website
  HTML = requests.get(url)

  #Parse the HTML 
  soup = BeautifulSoup(HTML.text, 'html.parser')
  
  # Find the current price
  text = soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text

  # Return the text
  return text

# Get the price of a cryptocurrency
price = get_crypto_price('bitcoin')

print(price)

# Create a function to consistently show the price if the cryptocurrency when it changes
def main():
  last_price = -1
  # Create a loop to continuously show the price
  while True:
    # Choose the cryptocurrency that i want to get the price for
    crypto='bitcoin'
    # Get the price of the cryptocurrency
    price=get_crypto_price(crypto)
    # Check if the price changed
    if price != last_price:
      print(crypto+' price: ',price)
      last_price=price
    time.sleep(3)

# Run/execute the main function
main()

