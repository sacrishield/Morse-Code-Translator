import tkinter as tk

morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}

BACKGROUND_COLOR = "#DFF6FF"
FONT_NAME = "Arial"
FONT_COLOR = "#06283D"


def encrypt(*args):
    # Turns the StringVar into a list, separates the string into individual characters
    string = list(input_var.get())
    encoded_word = []

    # Checks each element, and it's equivalent from the morse code dictionary
    # if character is not in dictionary, it will not be converted
    for character in string:
        if character.upper() in morse_dict:
            encoded_word.append(morse_dict[character.upper()])
            encoded_word.append(" ")
        if character == " ":
            encoded_word.append(" / ")

    encoded_word = "".join(encoded_word)
    output_var.set(encoded_word)
    output_string["text"] = output_var


window = tk.Tk()
input_var = tk.StringVar()
output_var = tk.StringVar()

window.title("Morse Code Translator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

title = tk.Label(text="TRANSLATE TO MORSE CODE \n", font=(FONT_NAME, 24, "bold"), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
title.grid(row=0, column=0, columnspan=2)

label_input = tk.Label(text="Enter a word/sentence here:", bg=BACKGROUND_COLOR, font=(FONT_NAME, 13, "bold"),
                       fg=FONT_COLOR)
label_input.grid(row=3, column=0, columnspan=1, sticky="W")

input_string = tk.Entry(width=70, font=(FONT_NAME, 13), textvariable=input_var, fg=FONT_COLOR)
input_string.grid(row=4, column=0, columnspan=2)

label_output = tk.Label(text="\nIt gets translated here:", bg=BACKGROUND_COLOR, font=(FONT_NAME, 13, "bold"),
                        fg=FONT_COLOR)
label_output.grid(row=5, column=0, columnspan=1, sticky="W")

output_string = tk.Label(textvariable=output_var, bg=BACKGROUND_COLOR, font=(FONT_NAME, 13, "bold"), wraplength=640,
                         fg=FONT_COLOR)
output_string.grid(row=6, column=0, columnspan=2, sticky="W")

# Updates the output RealTime
input_var.trace_add("write", encrypt)

window.mainloop()
