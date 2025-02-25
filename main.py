from config import *
import tkinter as tk
from chat.interface import Interface

def main():
    # Initialisation window tkinter
    screen = tk.Tk()
    screen.title("AdviseBot | Developed by Axel")
    screen.geometry(WINDOW_SIZE)

    # Title in screen
    label = tk.Label(screen, text="Lacking inspiration ?", font=FONT)
    label.pack(pady=10)

    # Box messages
    message_history = tk.Text(screen, wrap=tk.WORD, width=50, height=15)
    message_history.pack(padx=10, pady=10)
    message_history.config(state=tk.DISABLED)

    # Box entry user
    message_entry = tk.Entry(screen, width=40)
    message_entry.pack(pady=5)

    # Set chatbot interface
    chatbot = Interface(screen, message_history, message_entry)

    # 'Click' Enter to send
    message_entry.bind("<Return>", lambda event: chatbot.send_message())

    # Button to send
    send_button = tk.Button(screen, text="Send", command=chatbot.send_message, font=FONT)
    send_button.pack(pady=4)

    # Button to reset
    reset_button = tk.Button(screen, text="Clear", command=chatbot.clear_messages, font=FONT)
    reset_button.pack()

    # Tkinter Loop
    screen.mainloop()

if __name__ == "__main__":
    main()
