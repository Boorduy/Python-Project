import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import requests

def fetch_and_display():
    try:
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

        coinsda = json['data']

        display_text = ""
        for x in coinsda: 
            symbol = x['symbol']
            price = x['quote']['USD']['price']
            percent_change = x['quote']['USD']['percent_change_1h']
            display_text += f"Symbol: {symbol}, Price: ${price:.2f}, 1h Change: {percent_change:.2f}%\n"

        label.config(text=display_text)
    except Exception as e:
        label.config(text="Failed to fetch data. Please try again.")

# Create the main window
root = tk.Tk()

root.title("CryptoCurrency Price and Rate Change")
root.geometry("400x650+400+100")
root.resizable(False, False)

# Set window icon
image_icon = PhotoImage(file="cryptowallet.png")
root.iconphoto(False, image_icon)

# Set background color
root.configure(bg='#1e1e1e')

#resizebackground
original_image = Image.open("cryptobackground.png")
resized_image = original_image.resize((400,650), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(resized_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, width=400, height=650)

label = tk.Label(root, text="Press the button to display top 5 cryptocurrencies",
                 justify='left', padx=10, pady=10, bg='#1e1e1e', fg='white', font=('Helvetica', 12, 'bold'))
label.pack(pady=20)
# Add a background image (optional)
# Uncomment the following lines to use a background image

# Customize label


# Customize button
button = tk.Button(root, text="Display Top 5 Cryptos", command=fetch_and_display,
                   padx=10, pady=10, bg='#ffcc00', fg='black', font=('Helvetica', 12, 'bold'))
button.pack(pady=10)

root.mainloop()