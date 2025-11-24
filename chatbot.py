import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# ---------------------------
# Simple Rule-Based Chatbot Logic
# ---------------------------
def get_bot_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"

    elif "time" in user_input:
        return "The current time is: " + datetime.now().strftime("%H:%M:%S")

    elif "help" in user_input:
        return "Sure! You can ask me about the time, greetings, or say exit to close."

    elif any(bye in user_input for bye in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"

    else:
        return "I'm not sure I understand, but I'm learning!"


# ---------------------------
# GUI Chatbot Application
# ---------------------------
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("💬 Smart Rule-Based Chatbot")
        self.root.geometry("600x650")
        self.root.configure(bg="#c8e6f5")  # Attractive background color

        # Title label
        title = tk.Label(root, text="Smart Chatbot", font=("Arial", 28, "bold"), bg="#c8e6f5", fg="#003e6b")
        title.pack(pady=15)

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
        self.chat_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.config(state='disabled', bg="#f7f9fc")

        # Entry field frame
        entry_frame = tk.Frame(root, bg="#c8e6f5")
        entry_frame.pack(pady=10)

        # Input field
        self.user_input = tk.Entry(entry_frame, width=40, font=("Arial", 14))
        self.user_input.grid(row=0, column=0, padx=10)

        # Send button
        send_btn = tk.Button(entry_frame, text="Send", font=("Arial", 14), bg="#007acc", fg="white", command=self.send_message)
        send_btn.grid(row=0, column=1)

        self.root.bind('<Return>', lambda event: self.send_message())

    # Function to display messages in UI
    def display_message(self, message, sender="bot"):
        self.chat_area.config(state='normal')

        # Right-aligned user message
        if sender == "user":
            self.chat_area.tag_configure("user", justify='right', foreground="#00509e", font=("Arial", 12, "bold"))
            self.chat_area.insert(tk.END, message + "\n", "user")

        # Left-aligned bot message
        else:
            self.chat_area.tag_configure("bot", justify='left', foreground="#000", font=("Arial", 12))
            self.chat_area.insert(tk.END, message + "\n", "bot")

        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    # Send message and get response
    def send_message(self):
        user_text = self.user_input.get().strip()
        if user_text == "":
            return

        # Display user message
        self.display_message(user_text, "user")
        self.user_input.delete(0, tk.END)

        # Check for exit
        if user_text.lower() == "exit":
            self.root.destroy()
            return

        # Get chatbot response
        bot_response = get_bot_response(user_text)
        self.display_message(bot_response, "bot")


# ---------------------------
# Run Chatbot App
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
