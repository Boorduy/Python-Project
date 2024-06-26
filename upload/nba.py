import tkinter as tk
import requests
from PIL import Image, ImageTk
import os

def fetch_nba_data(year):
    url = f'https://api.sportradar.com/nba/trial/v8/en/games/{year}/REG/schedule.json?api_key=w0sCDGdGGx3aAcDDiT6rJ1eG1BCz7A659ZuClcey'
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        games = data.get('games', [])
        
        display_text = ""
        for game in games:
            date = game.get('scheduled', 'N/A')
            away = game.get('away', {}).get('name', 'N/A')
            away_alias = game.get('away', {}).get('alias', 'N/A')
            home = game.get('home', {}).get('name', 'N/A')
            home_alias = game.get('home', {}).get('alias', 'N/A')
            away_points = game.get('away_points', 'N/A')
            home_points = game.get('home_points', 'N/A')
            
            display_text += f"Date: {date}\nHome: {home} ({home_alias}) vs Away: {away} ({away_alias})\nHome Points: {home_points}, Away Points: {away_points}\n\n"
        
        return display_text
    else:
        return f"Error: {response.status_code}, {response.text}"

def fetch_and_display():
    year = year_entry.get()
    data = fetch_nba_data(year)
    data_text.config(state=tk.NORMAL)
    data_text.delete('1.0', tk.END)
    data_text.insert(tk.END, data)
    data_text.config(state=tk.DISABLED)

def run_tkapp():
    window.destroy()  # Close the current Tkinter window
    os.system('python tkapp.py')  # Run tkapp.py using the system command

# Create the main Tkinter window
window = tk.Tk()
window.title("NBA Season Summary")
window.geometry("1200x800")
image_icon = ImageTk.PhotoImage(file="basketball.png")
window.iconphoto(False, image_icon)

# Load and resize the background image
bg_image = Image.open("nba.png")
bg_image = bg_image.resize((1200, 800), Image.BILINEAR)  # Resize the image as per window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to set the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label and an entry for year input
year_label = tk.Label(window, text="Enter year for NBA season (2013-2023):", bg='white')
year_label.pack(pady=10)

year_entry = tk.Entry(window)
year_entry.pack()

# Create a button to fetch and display data
fetch_button = tk.Button(window, text="Fetch NBA Schedule", command=fetch_and_display)
fetch_button.pack(pady=10)

# Create a text widget to display NBA schedule
data_text = tk.Text(window, height=30, width=120)
data_text.pack(pady=20)
data_text.insert(tk.END, "Season Results will appear here -_-")

# Create a button to run tkapp.py
run_button = tk.Button(window, text="Main Menu", command=run_tkapp)
run_button.pack(pady=10)

# Start the Tkinter main loop
window.mainloop()