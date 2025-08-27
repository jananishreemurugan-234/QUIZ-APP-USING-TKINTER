import tkinter as tk
from tkinter import messagebox

# ---------- Questions (Hardcoded) ----------
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": 0
    },
    {
        "question": "Which language is widely used for AI?",
        "options": ["Python", "C", "Java", "HTML"],
        "answer": 0
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "7", "6"],
        "answer": 1
    }
]

# ---------- Variables ----------
q_no = 0
score = 0
selected_option = None

# ---------- Functions ----------
def display_question():
    """Display the current question and options."""
    global selected_option
    selected_option.set(-1)
    question_label.config(text=questions[q_no]['question'])
    for i in range(4):
        radio_buttons[i].config(text=questions[q_no]['options'][i])

def next_question():
    """Check answer and go to next question or show score."""
    global q_no, score
    if selected_option.get() == questions[q_no]['answer']:
        score += 1
    q_no += 1
    if q_no == len(questions):
        show_score()
    else:
        display_question()

def show_score():
    """Show final score and exit."""
    messagebox.showinfo("Score", f"Your score: {score}/{len(questions)}")
    root.destroy()

# ---------- Tkinter GUI ----------
root = tk.Tk()
root.title("Quiz App")
root.geometry("500x300")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
question_label.pack(pady=20)

selected_option = tk.IntVar()
selected_option.set(-1)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_option, value=i, font=("Arial", 12))
    rb.pack(anchor="w", padx=50)
    radio_buttons.append(rb)

next_button = tk.Button(root, text="Next", command=next_question, font=("Arial", 12))
next_button.pack(pady=20)

display_question()
root.mainloop()