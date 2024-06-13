import tkinter 
from tkinter import *
import requests

headers = {
  'X-CMC_PRO_API_KEY': 'e3242c02-8971-44cd-8b2f-625995df3dbc',
  'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()


coinstime = json['status']
coinsda = json['data']

for x in coinsda: 
 xx =(x['symbol'], x['quote']['USD']['price'])
 x =(x['symbol'], x['quote']['USD']['percent_change_1h'])

#print(xx,x)

#API Found ready to work properly now time to use tkinter
root = Tk()

root.title("CryptoCurrency Price and ratechange")
root.geometry("400x650+400+100")

root.resizable(False,False)
image_icon = PhotoImage(file="cryptowallet.png")
root.iconphoto(False,image_icon)
root.mainloop()