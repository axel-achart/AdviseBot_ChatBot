from config import *
import tkinter as tk
from chat.interface import Interface 

def main():
    # Initialisation de la fenêtre Tkinter
    screen = tk.Tk()
    screen.title("AdviseBot | Developed by Axel")
    screen.geometry(WINDOW_SIZE)


    # Titre
    label = tk.Label(screen, text="Discuss with your bot !", font=FONT)
    label.pack(pady=10)

    # Zone d'affichage des messages
    message_history = tk.Text(screen, wrap=tk.WORD, width=50, height=15)
    message_history.pack(padx=10, pady=10)
    message_history.config(state=tk.DISABLED)

    # Zone d'entrée de l'utilisateur
    message_entry = tk.Entry(screen, width=40)
    message_entry.bind("<Return>", lambda event: chatbot.send_message())
    message_entry.pack(pady=5)

    # Instanciation de l'interface chatbot
    chatbot = Interface(screen, message_history, message_entry)

    # Bouton d'envoi
    send_button = tk.Button(screen, text="Send", command=chatbot.send_message, font=FONT)
    send_button.pack(pady=4)

    # Bouton de réinitialisation
    reset_button = tk.Button(screen, text="Clear", command=chatbot.clear_messages, font=FONT)
    reset_button.pack()



    # Lancer la boucle Tkinter
    screen.mainloop()

if __name__ == "__main__":
    main()
