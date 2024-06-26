import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

# Function to handle button clicks
def button_click(image_path):
    root.destroy()  # Close the current Tkinter window
    if image_path == "mma.png":
        os.system('python ufcrank.py')  # Open ufcrank.py for mma_button
    elif image_path == "womenmma.png":
        os.system('python womenufcrank.py')  # Open womenufcrank.py for womenmma_button
    elif image_path == "nba.png":
        os.system('python nba.py')  # Open nba.py for nba_button
    elif image_path == "bitcoinman.png":
        os.system('python top5crypto.py')

# Create the main application window
root = tk.Tk()
root.title("Mohandes Boorduy Qomi App")
root.geometry("1200x800")
root.resizable(False, False)
#boop

image_icon = ImageTk.PhotoImage(file="run.png")
root.iconphoto(False, image_icon)


# Load and resize the background image
bg_image = Image.open("back.png")
bg_image = bg_image.resize((1200, 800), Image.BILINEAR)
background_image = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place at (0, 0) and stretch to cover the window

# Load button images
womenmma_image = Image.open("womenmma.png").resize((300, 200))  # Resize as needed
mma_image = Image.open("mma.png").resize((300, 250))      # Resize as needed
nba_image = Image.open("nba.png").resize((300, 200))            # Resize as needed

crypto_image = Image.open("bitcoinman.png").resize((300, 300))            # Resize as needed

# Convert images to PhotoImage objects
womenmma_photo = ImageTk.PhotoImage(womenmma_image)
mma_photo = ImageTk.PhotoImage(mma_image)
nba_photo = ImageTk.PhotoImage(nba_image)
crypto_photo = ImageTk.PhotoImage(crypto_image)

# Create buttons with images
womenmma_button = tk.Button(root, image=womenmma_photo, borderwidth=0, command=lambda: button_click("womenmma.png"))
mma_button = tk.Button(root, image=mma_photo, borderwidth=0, command=lambda: button_click("mma.png"))
nba_button = tk.Button(root, image=nba_photo, borderwidth=0, command=lambda: button_click("nba.png"))

crypto_button = tk.Button(root, image=crypto_photo, borderwidth=0, command=lambda: button_click("bitcoinman.png"))

#
label = Label(root, text="MMA Ranking",
              justify='left', padx=10, pady=10, bg='red', fg='black', font=('Helvetica', 17, 'bold'))
label.pack(pady=15)
label.place(relx=0.45,rely=0.03)

label2 = Label(root, text="Basketball Season Summary",
              justify='left', padx=10, pady=10, bg='gray', fg='orange', font=('Helvetica', 13, 'bold'))
label2.pack(pady=15)
label2.place(relx=0.725,rely=0.035)

label3 = Label(root, text="WMMA Ranking",
              justify='left', padx=10, pady=10, bg='pink', fg='black', font=('Helvetica', 14, 'bold'))
label3.pack(pady=15)
label3.place(relx=0.162,rely=0.03)

label4 = Label(root, text="Crypto LIVE Price",
              justify='left', padx=10, pady=10, bg='black', fg='yellow', font=('Helvetica', 20, 'bold'))
label4.pack(pady=15)
label4.place(relx=0.421,rely=0.5)



womenmma_button.place(relx=0.1, rely=0.1)
mma_button.place(relx=0.4, rely=0.1)
nba_button.place(relx=0.7, rely=0.1)
crypto_button.place(relx=0.4, rely=0.6)


root.mainloop()