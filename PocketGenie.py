import tkinter as tk
from tkinter import ttk
import random

def getjokes():
    jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "What do you get when you cross a snowman with a vampire? Frostbite!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What’s orange and sounds like a parrot? A carrot!",
    "Why can’t your nose be 12 inches long? Because then it would be a foot!",
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "What’s brown and sticky? A stick!",
    "What did one wall say to the other? I'll meet you at the corner!",
    "Why couldn’t the pony sing a lullaby? Because she was a little hoarse!",
    "Why do bees have sticky hair? Because they use honeycombs!",
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
    "What do you call fake spaghetti? An impasta!",
    "Why don’t oysters donate to charity? Because they are shellfish!",
    "Why do cows wear bells? Because their horns don’t work!",
    "What do you call cheese that isn’t yours? Nacho cheese!",
    "What kind of shoes do ninjas wear? Sneakers!",
    "Why did the math book look sad? Because it had too many problems!",
    "What do you call a factory that makes okay products? A satisfactory!",
    "Why don’t elephants use computers? They’re afraid of the mouse!",
    "Why couldn’t the leopard play hide and seek? Because he was always spotted!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the cookie go to the doctor? Because it felt crumby!",
    "Why did the computer go to the therapist? Because it had too many bytes!",
    "Why don’t eggs tell jokes? They might crack up!",
    "What did the janitor say when he jumped out of the closet? Supplies!",
    "Why can’t you give Elsa a balloon? Because she’ll let it go!"
]
    joke = random.choice(jokes)
    label133.config(text=joke)

def randomQuote():
    quotes = [
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "Your time is limited, so don't waste it living someone else's life.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "The Earth has music for those who listen.",
        "Look deep into nature, and then you will understand everything better.",
        "Adopt the pace of nature: her secret is patience.",
        "In every walk with nature, one receives far more than he seeks.",
        "Nature does not hurry, yet everything is accomplished.",
        "The poetry of the Earth is never dead.",
        "The mountains are calling and I must go.",
        "To sit in the shade on a fine day and look upon verdure is the most perfect refreshment.",
        "Heaven is under our feet as well as over our heads.",
        "Choose only one master—nature.",
        "Do not go where the path may lead, go instead where there is no path and leave a trail.",
        "Happiness is not something ready made. It comes from your own actions.",
        "The only limit to our realization of tomorrow will be our doubts of today.",
        "The best way to predict the future is to create it.",
        "Life is what happens when you're busy making other plans.",
        "You miss 100% of the shots you don't take.",
        "Do what you can, with what you have, where you are.",
        "The purpose of our lives is to be happy.",
        "Speed thrills but kills.",
        "Better late than never, arrive alive.",
        "Stay alert, accidents hurt.",
        "Drive like you want to arrive alive.",
        "Night doubles traffic troubles.",
        "Do not mix drinking and driving.",
        "Alert today – Alive tomorrow.",
        "Fast drive could be the last drive.",
        "Use your signals or face the signals.",
        "Take caution, avoid the caution tape.",
        "Safe driving is a responsible choice.",
        "Mind your speed, save your life.",
        "Every drop counts—conserve water, reduce pollution.",
        "Pollution is the price of ignorance, and nature pays the debt.",
        "Recycle today for a cleaner tomorrow.",
        "Say no to single-use plastics, yes to green habits.",
        "We breathe what we create—don’t pollute the air.",
        "Smog chokes cities; let’s clear the skies for our children.",
        "Pollution ends where compassion begins.",
        "Don’t trash our future; keep the Earth free of pollution.",
        "Protect nature; prevent pollution before it’s too late.",
        "A clean planet is a healthy planet—let’s make it happen.",
        "Pollution-free is the way to be."
    ]
    quote = random.choice(quotes)
    label123.config(text=quote)

def Calculate():
    try:
        num1 = int(spinbox.get())
        operation = combobox.get()
        num2 = int(spinbox2.get())
        if operation == 'Addition':
            result = num1 + num2
        elif operation == 'Subtraction':
            result = num1 - num2
        elif operation == 'Multiplication':
            result = num1 * num2
        elif operation == 'Division':
            result = num1 / num2
        else:
            result = "Invalid Operation"
        result_label.config(text=f"Result: {result}", fg='#2E8B57')
    except ValueError:
        result_label.config(text="Error: Enter valid numbers!", fg='red')

screen = tk.Tk()
screen.title("PocketGenie")
screen.geometry("2000x1000")
screen.configure(bg="#D8BFD8")

frame = tk.Frame(screen, bg='#D3E4CD')

label123 = tk.Label(screen, text='Qoute will appear here', bg='#D8BFD8', fg='#9370DB', font=('Arial', 16, 'italic'))
label123.pack(pady=20)

button = tk.Button(screen, text="Get Random Quote", command=randomQuote, bg='#C4A4C4', fg='white', font=('Arial', 12, 'bold'), relief='ridge')
button.pack(pady=30)

# Styles
style = ttk.Style()
style.configure('Custom.TCombobox', fieldbackground='#F9F9F9', background='#A1C181', foreground='black', font=('Arial', 12))

# Header
header = tk.Label(frame, text="Stylish Calculator", bg='#3A6351', fg='#FFFFFF', font=('Helvetica', 20, 'bold'))
header.pack(fill='x', pady=10)

# Input Frame
input_frame = tk.Frame(frame, bg='#D3E4CD')
input_frame.pack(pady=20)

# Spinbox 1
value = tk.StringVar(value="0")
spinbox = tk.Spinbox(input_frame,relief='flat', textvariable=value, from_=-999, to=999, font=('Arial', 14), width=10, justify='center')
spinbox.grid(row=0, column=0, padx=10)

# Combobox for Operations
combobox = ttk.Combobox(input_frame, style='Custom.TCombobox', values=['Addition', 'Subtraction', 'Multiplication', 'Division'], state='readonly', width=12)
combobox.grid(row=0, column=1, padx=10)

# Spinbox 2
value2 = tk.StringVar(value="0")
spinbox2 = tk.Spinbox(input_frame,relief='flat' , textvariable=value2, from_=-999, to=999, font=('Arial', 14), width=10, justify='center')
spinbox2.grid(row=0, column=2, padx=10)

# Calculate Button
button = tk.Button(frame, text="Calculate", bg='#A1C181', fg='white', font=('Arial', 12, 'bold'), relief='ridge', command=Calculate)
button.pack(pady=10)

# Result Label
result_label = tk.Label(frame, text="Result will appear here", bg='#D3E4CD', fg='#3A6351', font=('Arial', 14))
result_label.pack(pady=20)

frame2 = tk.Frame(screen, bg='#87CEEB')

label133 = tk.Label(frame2, text='Joke will appear here', bg='#87CEEB', fg='#4682B4', font=('Helvetica', 16, 'bold'))
label133.pack(pady=20)

button = tk.Button(frame2, text="Dispense Joke", command=getjokes, bg='#4682B4', fg='white', font=('Arial', 12, 'bold'), relief='ridge')
button.pack(pady=40)

frame2.pack(expand=False, fill='both')
frame.pack(expand=True, fill="both")
screen.mainloop()