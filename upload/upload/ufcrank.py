import tkinter as tk
import requests
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

                    display_text = ""
                    for competitor_ranking in competitor_rankings:
                        rank = competitor_ranking.get('rank')
                        competitor = competitor_ranking.get('competitor', {})
                        name = competitor.get('name')

                        display_text += f"Rank: {rank}, Name: {name}\n"

                    # Update text in the text widget
                    data_text.config(state=tk.NORMAL)
                    data_text.delete('1.0', tk.END)
                    data_text.insert(tk.END, display_text)
                    data_text.config(state=tk.DISABLED)
                    return

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def open_tkapp():
    window.destroy()  # Close the current Tkinter window
    os.system('python tkapp.py')  # Run tkapp.py using the system command

# Create the main Tkinter window
window = tk.Tk()
window.title("Men UFC")
window.geometry("1200x800")

image_icon = ImageTk.PhotoImage(file="mma.png")
window.iconphoto(False, image_icon)
# Load and resize the background image
bg_image = Image.open("octagon.png")
bg_image = bg_image.resize((1200, 800), Image.BILINEAR)  # Resize the image as per window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to set the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for instructions
instruction_label = tk.Label(window, text="Choose the ranking type:", bg='white')
instruction_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Define ranking options
ranking_options = {
    'Pound for Pound': 'pound_for_pound',
    'Flyweight': 'flyweight',
    'Bantamweight': 'bantamweight',
    'Featherweight': 'featherweight',
    'Lightweight': 'lightweight',
    'Welterweight': 'welterweight',
    'Middleweight': 'middleweight',
    'Heavyweight': 'heavyweight',
    'Light Heavyweight': 'light_heavyweight',
}

# Create a dropdown menu to select ranking type
selected_ranking = tk.StringVar(window)
selected_ranking.set('ChooseOneofTheOptions')  # Default value

ranking_menu = tk.OptionMenu(window, selected_ranking, *ranking_options.keys())
ranking_menu.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Create a button to fetch rankings
fetch_button = tk.Button(window, text="Fetch Rankings", command=lambda: get_rankings(ranking_options[selected_ranking.get()]))
fetch_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

# Create a text widget to display MMA rankings
data_text = tk.Text(window, height=20, width=100, bg='white', bd=1, relief=tk.SOLID)
data_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
data_text.insert(tk.END, "Results will appear here (-.-)")
data_text.config(state=tk.DISABLED)

# Create a button to open tkapp.py
open_button = tk.Button(window, text="Main Menu", command=open_tkapp)
open_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Start the Tkinter main loop
window.mainloop()