import tkinter as tk


class Interface:
    def __init__(self, root, message_history, message_entry):
        self.root = root
        self.message_history = message_history
        self.message_entry = message_entry

    def send_message(self):
        message = self.message_entry.get()
        if message:
            # Affiche le message de l'utilisateur
            self.message_history.config(state=tk.NORMAL)
            self.message_history.insert(tk.END, f"You : {message}\n")
            self.message_history.config(state=tk.DISABLED)

            # Simule une réponse automatique (à remplacer par API plus tard)
            response = self.get_bot_response(message)

            # Affiche la réponse du bot
            self.message_history.config(state=tk.NORMAL)
            self.message_history.insert(tk.END, f"AdviseBot : {response}\n")
            self.message_history.config(state=tk.DISABLED)

            # Efface l'entrée utilisateur
            self.message_entry.delete(0, tk.END)
    
    def clear_messages(self):
        self.message_history.config(state=tk.NORMAL)
        self.message_history.delete("1.0", tk.END)
        self.message_history.config(state=tk.DISABLED)


    def get_bot_response(self, message):
        return "I'm not connect to an API yet"
