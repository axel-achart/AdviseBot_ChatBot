import tkinter as tk
import random 
from chatbot import ConnectToAPI
from chat.music import Music

class Interface:
    def __init__(self, root, message_history, message_entry):
        self.root = root
        self.message_history = message_history
        self.message_entry = message_entry
        self.api_connector = ConnectToAPI()
        self.music = Music()

    def send_message(self):
        message = self.message_entry.get().lower().strip()
        if message:
            self.message_history.config(state=tk.NORMAL)
            self.message_history.insert(tk.END, f"You : {message}\n")
            self.message_history.see(tk.END)
            self.message_history.config(state=tk.DISABLED)

            response = self.get_bot_response(message)

            self.message_history.config(state=tk.NORMAL)
            self.message_history.insert(tk.END, f"AdviseBot : {response}\n")
            self.message_history.see(tk.END)
            self.message_history.config(state=tk.DISABLED)

            self.message_entry.delete(0, tk.END)

    def clear_messages(self):
        self.message_history.config(state=tk.NORMAL)
        self.message_history.delete("1.0", tk.END)
        self.message_history.config(state=tk.DISABLED)

    def get_bot_response(self, message):

        genres = ["action", "comedy", "drama", "horror", "romance", "thriller", "animation", "fantasy", "sci-fi", "mystery"]
        detected_genre = None
        detected_year = None

        words = message.split()

        # Detect a genre and year
        for word in words:
            if word.isdigit() and len(word) == 4:  # Vérifie si le mot est une année (4 chiffres)
                detected_year = word
            if word in genres:
                detected_genre = word

        if not detected_genre and not detected_year:
            return "Please specify a genre or a year for movie recommendations."

        # Take a film from API
        movies = self.api_connector.fetch_movies_by_genre_and_year(detected_genre, detected_year)

        if movies:
            film = random.choice(movies) 
            return f"🎬 I recommand you : {film['Title']} ({film['Year']})"

        return "I don't find a good movie with your request. Please retry and use words, not only years."
