import tkinter as tk
import requests
from tkinter import PhotoImage, Label, Button
from PIL import Image, ImageTk
import os

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

        json_data = requests.get(url, params=params, headers=headers).json()
        coins_data = json_data['data']

        display_text = ""
        for coin in coins_data: 
            symbol = coin['symbol']
            price = coin['quote']['USD']['price']
            percent_change = coin['quote']['USD']['percent_change_1h']
            display_text += f"Symbol: {symbol}, Price: ${price:.2f}, 1h Change: {percent_change:.2f}%\n"

        label.config(text=display_text)
    except Exception as e:
        label.config(text="Failed to fetch data. Please try again.")

def open_tkapp_and_exit():
    root.destroy()  # Close the current Tkinter window
    os.system('python tkapp.py')  # Open tkapp.py

# Create the main window
root = tk.Tk()
root.title("CryptoCurrency Price and Rate Change")
root.geometry("1200x800")  # Set window size to 1200x800
root.resizable(False, False)
image_icon = ImageTk.PhotoImage(file="cryptowallet.png")
root.iconphoto(False, image_icon)
# Load and resize the background image
original_image = Image.open("cryptobackground.png")
resized_image = original_image.resize((1200, 800), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(resized_image)
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, width=1200, height=800)

# Create a label for displaying data
label = Label(root, text="LIVE Top 5 Crypto's",
              justify='left', padx=10, pady=10, bg='#1e1e1e', fg='white', font=('Helvetica', 12, 'bold'))
label.pack(pady=20)

# Create a button to fetch and display data
button = Button(root, text="Display Top 5 Cryptos", command=fetch_and_display,
                padx=10, pady=10, bg='#ffcc00', fg='black', font=('Helvetica', 12, 'bold'))
button.pack(pady=10)

# Create a button to open tkapp.py and exit
tkapp_button = Button(root, text="Main menu", command=open_tkapp_and_exit,
                      padx=10, pady=10, bg='#4CAF50', fg='white', font=('Helvetica', 12, 'bold'))
tkapp_button.pack(pady=10)

root.mainloop()