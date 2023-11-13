import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk

# Download the NLTK resources (if not already downloaded)
nltk.download('punkt')
# Create the main window
root = tk.Tk()              # Create the main window and store it in 'root' variable
root.title("Text Summarizer")  # Set the title of the window to "Text Summarizer"
root.geometry("600x400")      # Set the initial dimensions of the window to 600x400 pixels

# Function to summarize text and calculate word count
def summarize_text():
    input_text = input_textbox.get("1.0", "end-1c")  # Get the text from the input_textbox widget

    # Calculate the initial word count
    initial_word_count = len(input_text.split())

    # Create a parser for the input text
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))

    # Choose a summarization method (e.g., LexRank)
    summarizer = LexRankSummarizer()

    # Summarize the text
    summarized_sentences = summarizer(parser.document, 6)  # Summarize the text into 6 sentences

    # Join the summarized sentences
    summarized_text = "\n".join(str(sentence) for sentence in summarized_sentences)

    # Calculate the final word count
    final_word_count = len(summarized_text.split())

    # Display the initial and final word counts and the summarized text
    output_textbox.delete("1.0", "end")    # Clear the existing content in the output_textbox
    output_textbox.insert("1.0", f"Initial Word Count: {initial_word_count}\n\n")  # Display initial word count
    output_textbox.insert("end", f"Final Word Count: {final_word_count}\n\n")      # Display final word count
    output_textbox.insert("end", "Summarized Text:\n")    # Display a label for summarized text
    output_textbox.insert("end", summarized_text)          # Display the summarized text

# Create a colorful and vibrant UI
style = ttk.Style()   # Create an instance of ttk.Style()

# Configure the style for buttons, labels, and text widgets
style.configure("TButton", foreground="white", background="#4CAF50", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TText", font=("Arial", 12))

# Create input and output text areas
input_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
input_textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Create and position the input text area

output_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
output_textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Create and position the output text area

# Create a "Summarize" button
summarize_button = ttk.Button(root, text="Summarize", command=summarize_text)  # Create a button with "Summarize" text
summarize_button.grid(row=2, column=0, padx=10, pady=10)  # Position the button

# Make the text areas expand when resizing the window
root.grid_rowconfigure(0, weight=1)  # Make the first row expandable
root.grid_rowconfigure(1, weight=1)  # Make the second row expandable
root.grid_columnconfigure(0, weight=1)  # Make the first column expandable

# Run the GUI
root.mainloop()  # Start the main event loop of the tkinter application


