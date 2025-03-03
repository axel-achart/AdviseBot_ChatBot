from config import *
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image
import pygame
from chat.interface import Interface
from chat.music import Music
pygame.mixer.init()


def main():
    # Initialisation window tkinter
    screen = tk.Tk()
    screen.title("AdviseBot | Developed by Axel")
    screen.geometry(WINDOW_SIZE)
    screen.configure(background=BACKGROUND)

    FONT = tkinter.font.Font(family="Courier", size=14, weight="bold")

    # Logo
    logo = Image.open(LOGO_ADVISEBOT)
    logo_resized = logo.resize((200,200))
    logo_correct = ImageTk.PhotoImage(logo_resized)
    logo_label = tk.Label(screen, image=logo_correct, background=BACKGROUND)
    logo_label.pack(side='left', padx=20)

    # Title in screen
    label = tk.Label(screen, text="AdviseBot | Lacking inspiration ?", font=FONT)
    label.configure(background=BACKGROUND)
    label.pack(pady=10)

    # Box messages
    message_history = tk.Text(screen, wrap=tk.WORD, width=50, height=15)
    message_history.pack(padx=10, pady=10)
    message_history.config(state=tk.DISABLED)

    # Box entry user
    message_entry = tk.Entry(screen, width=40)
    message_entry.pack(pady=5)

    # Set 
    chatbot = Interface(screen, message_history, message_entry)
    music = Music()

    # 'Click' Enter to send
    message_entry.bind("<Return>", lambda event: chatbot.send_message())

    # Button to send
    send_button = tk.Button(screen, text="Send", command=chatbot.send_message, font=FONT)
    send_button.pack(pady=4)

    # Button to reset
    reset_button = tk.Button(screen, text="Clear", command=chatbot.clear_messages, font=FONT)
    reset_button.pack(pady=4)

    # Button to mute/unmute sound
    music_button = tk.Button(screen, text="Pause Music", command=music.music_pause, font=FONT)
    music_button.pack(pady=4)
    music.music_play()


    # Tkinter Loop
    screen.mainloop()

if __name__ == "__main__":
    main()