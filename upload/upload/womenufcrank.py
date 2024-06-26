import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

def get_rankings(ranking_name):
    # Define the URL with the API key embedded
    url = "https://api.sportradar.com/mma/trial/v2/en/rankings.json?api_key=w0sCDGdGGx3aAcDDiT6rJ1eG1BCz7A659ZuClcey"

    # Define the headers
    headers = {
        "accept": "application/json"
    }

    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            
            rankings = data.get('rankings', [])

            # Filter for the specified ranking
            for ranking in rankings:
                if ranking.get('name') == ranking_name:
                    competitor_rankings = ranking.get('competitor_rankings', [])
                    return [(cr.get('rank'), cr.get('competitor', {}).get('name')) for cr in competitor_rankings]
        else:
            messagebox.showerror("Error", f"Error: {response.status_code} - {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request error", f"Request error: {e}")
        return []

def display_rankings():
    ranking_name = ranking_options[ranking_var.get()]
    rankings = get_rankings(ranking_name)
    if rankings:
        text_widget.config(state=tk.NORMAL)
        text_widget.delete(1.0, tk.END)
        for rank, name in rankings:
            text_widget.insert(tk.END, f"Rank: {rank}, Name: {name}\n")
        text_widget.config(state=tk.DISABLED)
    else:
        text_widget.config(state=tk.NORMAL)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "No rankings found.")
        text_widget.config(state=tk.DISABLED)

def open_tkapp():
    root.destroy()  # Close the current Tkinter window
    os.system('python tkapp.py')  # Run tkapp.py using the system command

# Create the main window
root = tk.Tk()
root.title("Women UFC")
root.geometry("1200x800")
image_icon = ImageTk.PhotoImage(file="ufc2.png")
root.iconphoto(False, image_icon)


# Load and resize the background image
bg_image = Image.open("octagon2.png")
bg_image = bg_image.resize((1200, 800), Image.BILINEAR)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to set the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a dropdown menu for ranking types
ranking_options = {
    'strawweight': 'womens_strawweight',
    'flyweight': 'womens_flyweight',
    'bantamweight': 'womens_bantamweight',
    'featherweight': 'womens_featherweight',
}

ranking_var = tk.StringVar()
ranking_var.set('choose')  # default value

ranking_label = tk.Label(root, text="Choose the ranking type:", bg='white')
ranking_label.pack(pady=10)

ranking_menu = ttk.Combobox(root, textvariable=ranking_var, values=list(ranking_options.keys()))
ranking_menu.pack(pady=5)

# Create a button to fetch and display rankings
fetch_button = tk.Button(root, text="Fetch Rankings", command=display_rankings)
fetch_button.pack(pady=10)

# Create a text widget to display the rankings
text_widget = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, width=50, height=20, bg='white')
text_widget.pack(pady=10)

# Create a button to open tkapp.py
open_button = tk.Button(root, text="Main Menu", command=open_tkapp)
open_button.pack(pady=10)

# Run the application
root.mainloop()