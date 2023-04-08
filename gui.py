from tkinter import CENTER

import customtkinter as ctk
import co


window = ctk.CTk()
window.wm_title("AI chat")
window.geometry("300x500")
window.resizable(True, True)


font = ctk.CTkFont("Arial", size=35)
font2 = ctk.CTkFont("Arial", size=10)
font3 = ctk.CTkFont("Arial", size=20)

header = ctk.CTkLabel(text="Co:here Assistant", font=font, master=window)
header.place(relx=0.5, rely=0.1, anchor=CENTER)

info_label = ctk.CTkLabel(master=window, text="", font=font2)
info_label.place(relx=0.5, rely=0.3, anchor=CENTER)


def respond():
    sr = co.stt()
    ai_response = co.respond(sr)
    info_label.configure(text=f"You: {sr}\n AI: {ai_response}")
    tts = co.tts(text=ai_response)


speak_button = ctk.CTkButton(master=window, text="  🎙  ", font=font3, width=10, command=respond)
speak_button.place(relx=0.5, rely=0.9, anchor=CENTER)

window.mainloop()
